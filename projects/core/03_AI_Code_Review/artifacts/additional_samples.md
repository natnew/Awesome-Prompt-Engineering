# Additional Code Review Samples

More code to practice your review skills. Each has multiple issues.

---

## Sample 7: File Download Handler

```python
import os
import requests

def download_file(url, save_path):
    """Download a file from URL and save to disk."""
    response = requests.get(url)
    
    with open(save_path, 'wb') as f:
        f.write(response.content)
    
    return save_path
```

**Your Review:**
- Issues found:
- Severity:
- Confidence:

<details>
<summary>Click to reveal issues</summary>

**Issues:**
1. **No URL validation** (Critical): Could be used for SSRF attacks
2. **Path traversal vulnerability** (Critical): save_path not sanitized
3. **No error handling** (High): Network errors, file errors not caught
4. **No timeout** (High): Could hang indefinitely
5. **Loads entire file in memory** (Medium): Won't work for large files
6. **No status code check** (High): 404/500 responses still "succeed"
7. **No content-type validation** (Medium): Could download malicious files

**Improved version:**
```python
import os
import requests
from urllib.parse import urlparse

ALLOWED_DOMAINS = ['trusted-cdn.example.com']
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB

def download_file(url, save_dir, allowed_extensions=None):
    """Download a file from a trusted URL and save to disk."""
    # Validate URL
    parsed = urlparse(url)
    if parsed.netloc not in ALLOWED_DOMAINS:
        raise ValueError(f"Domain not allowed: {parsed.netloc}")
    
    # Get filename from URL (sanitized)
    filename = os.path.basename(parsed.path)
    if not filename or '..' in filename:
        raise ValueError("Invalid filename in URL")
    
    if allowed_extensions:
        ext = os.path.splitext(filename)[1].lower()
        if ext not in allowed_extensions:
            raise ValueError(f"Extension not allowed: {ext}")
    
    # Ensure save path is within allowed directory
    save_path = os.path.join(save_dir, filename)
    if not os.path.abspath(save_path).startswith(os.path.abspath(save_dir)):
        raise ValueError("Path traversal detected")
    
    # Download with streaming and size limit
    response = requests.get(url, stream=True, timeout=30)
    response.raise_for_status()
    
    # Check content length
    content_length = int(response.headers.get('content-length', 0))
    if content_length > MAX_FILE_SIZE:
        raise ValueError(f"File too large: {content_length} bytes")
    
    # Stream to file
    downloaded = 0
    with open(save_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            downloaded += len(chunk)
            if downloaded > MAX_FILE_SIZE:
                os.remove(save_path)
                raise ValueError("File exceeded size limit during download")
            f.write(chunk)
    
    return save_path
```
</details>

---

## Sample 8: Password Reset Token

```python
import random
import string
from datetime import datetime

def generate_reset_token(user_id):
    """Generate a password reset token."""
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    expiry = datetime.now().timestamp() + 3600  # 1 hour
    
    return {
        'user_id': user_id,
        'token': token,
        'expiry': expiry
    }

def verify_reset_token(stored_token, provided_token):
    """Verify a password reset token."""
    if stored_token['token'] == provided_token:
        if datetime.now().timestamp() < stored_token['expiry']:
            return True
    return False
```

**Your Review:**
- Issues found:
- Severity:
- Confidence:

<details>
<summary>Click to reveal issues</summary>

**Issues:**
1. **Insecure random** (Critical): `random` is not cryptographically secure
2. **Timing attack** (High): String comparison is not constant-time
3. **Token not hashed** (High): Tokens stored in plain text can be stolen
4. **No rate limiting** (Medium): Brute force possible
5. **No single-use enforcement** (Medium): Token can be reused
6. **Expiry not checked first** (Low): Minor optimization

**Improved version:**
```python
import secrets
import hashlib
import hmac
from datetime import datetime, timedelta

def generate_reset_token(user_id):
    """Generate a secure password reset token."""
    # Use cryptographically secure random
    token = secrets.token_urlsafe(32)
    
    # Hash the token for storage (only hash is stored)
    token_hash = hashlib.sha256(token.encode()).hexdigest()
    
    expiry = datetime.utcnow() + timedelta(hours=1)
    
    return {
        'token_for_user': token,  # Send to user
        'stored_data': {
            'user_id': user_id,
            'token_hash': token_hash,
            'expiry': expiry.isoformat(),
            'used': False
        }
    }

def verify_reset_token(stored_data, provided_token):
    """Verify a password reset token securely."""
    # Check expiry first (fast rejection)
    expiry = datetime.fromisoformat(stored_data['expiry'])
    if datetime.utcnow() > expiry:
        return False
    
    # Check if already used
    if stored_data.get('used', False):
        return False
    
    # Hash provided token and compare
    provided_hash = hashlib.sha256(provided_token.encode()).hexdigest()
    
    # Constant-time comparison
    return hmac.compare_digest(stored_data['token_hash'], provided_hash)
```
</details>

---

## Sample 9: Cache Implementation

```python
class Cache:
    """Simple in-memory cache with expiration."""
    
    def __init__(self):
        self.data = {}
    
    def get(self, key):
        """Get a value from cache."""
        if key in self.data:
            value, expiry = self.data[key]
            if time.time() < expiry:
                return value
            else:
                del self.data[key]
        return None
    
    def set(self, key, value, ttl=300):
        """Set a value in cache with TTL in seconds."""
        expiry = time.time() + ttl
        self.data[key] = (value, expiry)
    
    def delete(self, key):
        """Delete a key from cache."""
        del self.data[key]
```

**Your Review:**
- Issues found:
- Severity:
- Confidence:

<details>
<summary>Click to reveal issues</summary>

**Issues:**
1. **Not thread-safe** (High): Race conditions on concurrent access
2. **Memory leak** (High): Expired entries only removed on access
3. **Missing import** (Low): `time` not imported
4. **delete() raises KeyError** (Medium): No check if key exists
5. **No size limit** (Medium): Cache can grow unbounded
6. **No type checking** (Low): Keys could be unhashable

**Improved version:**
```python
import time
import threading
from collections import OrderedDict

class Cache:
    """Thread-safe in-memory cache with expiration and size limit."""
    
    def __init__(self, max_size=1000, cleanup_interval=60):
        self._data = OrderedDict()
        self._lock = threading.RLock()
        self._max_size = max_size
        self._cleanup_interval = cleanup_interval
        self._last_cleanup = time.time()
    
    def get(self, key, default=None):
        """Get a value from cache."""
        with self._lock:
            if key in self._data:
                value, expiry = self._data[key]
                if time.time() < expiry:
                    # Move to end (LRU)
                    self._data.move_to_end(key)
                    return value
                else:
                    del self._data[key]
            return default
    
    def set(self, key, value, ttl=300):
        """Set a value in cache with TTL in seconds."""
        with self._lock:
            self._maybe_cleanup()
            
            # Evict oldest if at capacity
            while len(self._data) >= self._max_size:
                self._data.popitem(last=False)
            
            expiry = time.time() + ttl
            self._data[key] = (value, expiry)
            self._data.move_to_end(key)
    
    def delete(self, key):
        """Delete a key from cache."""
        with self._lock:
            self._data.pop(key, None)
    
    def _maybe_cleanup(self):
        """Periodically remove expired entries."""
        now = time.time()
        if now - self._last_cleanup < self._cleanup_interval:
            return
        
        self._last_cleanup = now
        expired = [k for k, (v, exp) in self._data.items() if now >= exp]
        for key in expired:
            del self._data[key]
```
</details>

---

## Sample 10: Webhook Handler

```python
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    """Handle incoming webhook."""
    data = request.json
    
    # Run deployment script
    branch = data['ref'].split('/')[-1]
    result = subprocess.run(
        f'./deploy.sh {branch}',
        shell=True,
        capture_output=True
    )
    
    return {'status': 'ok', 'output': result.stdout.decode()}
```

**Your Review:**
- Issues found:
- Severity:
- Confidence:

<details>
<summary>Click to reveal issues</summary>

**Issues:**
1. **Command injection** (Critical): `branch` directly in shell command
2. **No authentication** (Critical): Anyone can call webhook
3. **No signature verification** (Critical): Can't verify request is from trusted source
4. **No input validation** (High): Assumes `data['ref']` exists
5. **Sensitive output exposure** (High): Returns command output
6. **Synchronous execution** (Medium): Blocks during deployment
7. **shell=True** (High): Enables shell injection

**Improved version:**
```python
import hmac
import hashlib
import subprocess
import re
from flask import Flask, request, jsonify

app = Flask(__name__)
WEBHOOK_SECRET = os.environ.get('WEBHOOK_SECRET')
ALLOWED_BRANCHES = {'main', 'staging', 'production'}

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    """Handle incoming webhook with security checks."""
    # Verify signature
    signature = request.headers.get('X-Hub-Signature-256')
    if not signature:
        return jsonify({'error': 'Missing signature'}), 401
    
    expected_sig = 'sha256=' + hmac.new(
        WEBHOOK_SECRET.encode(),
        request.data,
        hashlib.sha256
    ).hexdigest()
    
    if not hmac.compare_digest(signature, expected_sig):
        return jsonify({'error': 'Invalid signature'}), 401
    
    # Parse and validate input
    data = request.json
    if not data or 'ref' not in data:
        return jsonify({'error': 'Invalid payload'}), 400
    
    # Extract and validate branch name
    ref = data['ref']
    if not ref.startswith('refs/heads/'):
        return jsonify({'error': 'Not a branch push'}), 400
    
    branch = ref.split('/')[-1]
    
    # Whitelist validation
    if branch not in ALLOWED_BRANCHES:
        return jsonify({'error': f'Branch not allowed: {branch}'}), 403
    
    # Additional sanitization (defense in depth)
    if not re.match(r'^[a-zA-Z0-9_-]+$', branch):
        return jsonify({'error': 'Invalid branch name'}), 400
    
    # Run deployment (no shell, explicit args)
    try:
        result = subprocess.run(
            ['./deploy.sh', branch],
            capture_output=True,
            timeout=300,
            check=True
        )
        return jsonify({'status': 'ok'})
    except subprocess.CalledProcessError:
        return jsonify({'status': 'failed'}), 500
    except subprocess.TimeoutExpired:
        return jsonify({'status': 'timeout'}), 500
```
</details>

---

## Sample 11: Data Export

```python
import csv

def export_users_to_csv(users, filepath):
    """Export user data to CSV file."""
    with open(filepath, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'name', 'email', 'password', 'ssn'])
        
        for user in users:
            writer.writerow([
                user['id'],
                user['name'],
                user['email'],
                user['password'],
                user['ssn']
            ])
```

**Your Review:**
- Issues found:
- Severity:
- Confidence:

<details>
<summary>Click to reveal issues</summary>

**Issues:**
1. **Exports passwords** (Critical): Never export password hashes
2. **Exports SSN** (Critical): PII should not be in exports without controls
3. **No access control** (High): Anyone can call this
4. **No audit logging** (High): No record of who exported what
5. **No encryption** (High): File written in plain text
6. **Path traversal** (Medium): filepath not validated
7. **No newline parameter** (Low): May cause issues on Windows

**Improved version:**
```python
import csv
import os
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

ALLOWED_EXPORT_FIELDS = {'id', 'name', 'email', 'created_at'}
EXPORT_DIR = '/secure/exports'

def export_users_to_csv(users, requester_id, fields=None):
    """Export user data to CSV file with audit logging."""
    # Validate and filter fields
    fields = fields or ['id', 'name', 'email']
    fields = [f for f in fields if f in ALLOWED_EXPORT_FIELDS]
    
    if not fields:
        raise ValueError("No valid fields specified")
    
    # Generate safe filename
    timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    filename = f"user_export_{timestamp}.csv"
    filepath = os.path.join(EXPORT_DIR, filename)
    
    # Ensure path is within allowed directory
    if not os.path.abspath(filepath).startswith(os.path.abspath(EXPORT_DIR)):
        raise ValueError("Invalid export path")
    
    # Audit log before export
    logger.info(
        "user_export_started",
        extra={
            'requester_id': requester_id,
            'fields': fields,
            'user_count': len(users),
            'filepath': filepath
        }
    )
    
    # Export only allowed fields
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        
        for user in users:
            # Filter to only allowed fields
            safe_user = {k: user.get(k, '') for k in fields}
            writer.writerow(safe_user)
    
    # Audit log after export
    logger.info(
        "user_export_completed",
        extra={
            'requester_id': requester_id,
            'filepath': filepath,
            'rows_exported': len(users)
        }
    )
    
    return filepath
```
</details>

---

## Sample 12: API Rate Limiter Decorator

```python
from functools import wraps
import time

request_counts = {}

def rate_limit(max_requests, window_seconds):
    """Rate limit decorator."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            client_ip = kwargs.get('client_ip', 'unknown')
            
            if client_ip not in request_counts:
                request_counts[client_ip] = []
            
            # Clean old requests
            now = time.time()
            request_counts[client_ip] = [
                t for t in request_counts[client_ip]
                if now - t < window_seconds
            ]
            
            if len(request_counts[client_ip]) >= max_requests:
                raise Exception("Rate limit exceeded")
            
            request_counts[client_ip].append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

**Your Review:**
- Issues found:
- Severity:
- Confidence:

<details>
<summary>Click to reveal issues</summary>

**Issues:**
1. **Global mutable state** (High): Not thread-safe
2. **Memory leak** (High): `request_counts` grows forever
3. **IP spoofing vulnerable** (Medium): Trusts client_ip from kwargs
4. **No distributed support** (Medium): Won't work across servers
5. **Generic exception** (Low): Should use specific exception class
6. **Blocking cleanup** (Medium): Cleanup on every request is inefficient

**Improved version:**
```python
from functools import wraps
import time
import threading
from collections import defaultdict

class RateLimitExceeded(Exception):
    """Raised when rate limit is exceeded."""
    pass

class RateLimiter:
    """Thread-safe rate limiter with memory management."""
    
    def __init__(self, max_requests, window_seconds, max_clients=10000):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.max_clients = max_clients
        self._requests = defaultdict(list)
        self._lock = threading.Lock()
        self._last_cleanup = time.time()
    
    def check(self, client_id):
        """Check if request is allowed."""
        with self._lock:
            now = time.time()
            self._maybe_cleanup(now)
            
            # Clean old requests for this client
            self._requests[client_id] = [
                t for t in self._requests[client_id]
                if now - t < self.window_seconds
            ]
            
            if len(self._requests[client_id]) >= self.max_requests:
                return False
            
            self._requests[client_id].append(now)
            return True
    
    def _maybe_cleanup(self, now):
        """Periodic cleanup of old entries."""
        if now - self._last_cleanup < self.window_seconds:
            return
        
        self._last_cleanup = now
        
        # Remove old entries
        for client_id in list(self._requests.keys()):
            self._requests[client_id] = [
                t for t in self._requests[client_id]
                if now - t < self.window_seconds
            ]
            if not self._requests[client_id]:
                del self._requests[client_id]
        
        # Evict oldest clients if too many
        if len(self._requests) > self.max_clients:
            # Simple eviction: remove clients with oldest last request
            sorted_clients = sorted(
                self._requests.keys(),
                key=lambda k: max(self._requests[k]) if self._requests[k] else 0
            )
            for client_id in sorted_clients[:len(self._requests) - self.max_clients]:
                del self._requests[client_id]


def rate_limit(max_requests, window_seconds):
    """Rate limit decorator using proper limiter."""
    limiter = RateLimiter(max_requests, window_seconds)
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Get client ID from request context (implementation-specific)
            client_id = kwargs.pop('_rate_limit_key', 'default')
            
            if not limiter.check(client_id):
                raise RateLimitExceeded(
                    f"Rate limit exceeded: {max_requests} requests per {window_seconds}s"
                )
            
            return func(*args, **kwargs)
        return wrapper
    return decorator
```
</details>

---

## Scoring Your Review

After completing all samples, calculate your score:

| Metric | Count |
|:-------|:------|
| Total issues in samples | 50+ |
| Issues you found | |
| Issues you missed | |
| False positives (issues that weren't issues) | |
| **Accuracy** | Found / Total |

### Skill Levels

- **Novice** (0-30%): Keep practicing, focus on one category at a time
- **Developing** (30-50%): Good foundation, work on your blind spots
- **Competent** (50-70%): Solid reviewer, practice edge cases
- **Advanced** (70-85%): Strong skills, focus on subtle issues
- **Expert** (85%+): Consider teaching others

---

*Use these samples for practice. Real AI-generated code will have different patterns.*
