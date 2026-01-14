"""
AI Code Review - Solutions

SPOILER ALERT: Only read this after completing your review of code_samples.py

Each sample includes:
- List of issues
- Severity ratings
- Corrected implementation
"""


# =============================================================================
# SAMPLE 1: Calculate Average - SOLUTIONS
# =============================================================================
"""
ISSUES FOUND:

1. Division by zero (High)
   - Empty list causes ZeroDivisionError
   - No check for len(numbers) == 0

2. No type checking (Medium)
   - Non-numeric items will cause TypeError
   - No validation that input is a list

3. No None check (Medium)
   - None input causes TypeError on sum()

Total issues: 3
"""

def calculate_average_fixed(numbers):
    """Calculate the average of a list of numbers."""
    if numbers is None:
        raise ValueError("Input cannot be None")
    
    if not isinstance(numbers, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    
    if len(numbers) == 0:
        raise ValueError("Cannot calculate average of empty list")
    
    # Validate all items are numeric
    for i, num in enumerate(numbers):
        if not isinstance(num, (int, float)):
            raise TypeError(f"Item at index {i} is not numeric: {num}")
    
    return sum(numbers) / len(numbers)


# =============================================================================
# SAMPLE 2: User Authentication - SOLUTIONS
# =============================================================================
"""
ISSUES FOUND:

1. SQL Injection (Critical)
   - String interpolation allows injection
   - username = "admin'--" bypasses password check

2. Plain text passwords (Critical)
   - Passwords should be hashed (bcrypt, argon2)
   - Comparison should use constant-time comparison

3. Timing attack vulnerability (High)
   - Early return on no user leaks information
   - Should use constant-time comparison

4. No connection error handling (Medium)
   - Database errors not caught
   - Connection not properly managed

5. No input validation (Medium)
   - No length limits on inputs
   - No character validation

Total issues: 5
"""

import sqlite3
import hashlib
import hmac
import secrets

def authenticate_user_fixed(username, password):
    """Check if username and password are valid - SECURE VERSION."""
    # Input validation
    if not username or not password:
        return False
    
    if len(username) > 100 or len(password) > 100:
        return False
    
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        # Parameterized query prevents SQL injection
        query = "SELECT password_hash, salt FROM users WHERE username = ?"
        cursor.execute(query, (username,))
        
        result = cursor.fetchone()
        conn.close()
        
        if result is None:
            # Constant-time fake check to prevent timing attacks
            fake_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), b'fake_salt', 100000)
            return False
        
        stored_hash, salt = result
        
        # Hash the provided password
        computed_hash = hashlib.pbkdf2_hmac(
            'sha256', 
            password.encode(), 
            salt.encode(), 
            100000
        ).hex()
        
        # Constant-time comparison
        return hmac.compare_digest(computed_hash, stored_hash)
        
    except sqlite3.Error:
        return False


# =============================================================================
# SAMPLE 3: Find Duplicates - SOLUTIONS
# =============================================================================
"""
ISSUES FOUND:

1. O(n²) complexity (High)
   - Nested loops make this very slow
   - O(n) solution exists using sets/dicts

2. O(n) lookup in duplicates list (Medium)
   - 'if items[i] not in duplicates' is O(n)
   - Should use a set for O(1) lookup

3. Redundant comparisons (Low)
   - Compares same pairs multiple times indirectly
   - Could be optimized

Total issues: 3
"""

def find_duplicates_fixed(items):
    """Find all duplicate items in a list - O(n) version."""
    seen = set()
    duplicates = set()
    
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)


# Alternative using Counter
from collections import Counter

def find_duplicates_counter(items):
    """Find all duplicate items using Counter."""
    counts = Counter(items)
    return [item for item, count in counts.items() if count > 1]


# =============================================================================
# SAMPLE 4: Parse Date - SOLUTIONS
# =============================================================================
"""
ISSUES FOUND:

1. No input validation (High)
   - None input causes AttributeError
   - Wrong format causes IndexError or ValueError

2. No format validation (High)
   - "not-a-date" doesn't raise clear error
   - Invalid dates like "2024-13-45" accepted

3. No error handling (Medium)
   - Should catch and re-raise with helpful message

4. No type checking (Low)
   - Non-string input not handled

Total issues: 4
"""

from datetime import datetime

def parse_date_fixed(date_string):
    """Parse a date string in format YYYY-MM-DD."""
    if date_string is None:
        raise ValueError("Date string cannot be None")
    
    if not isinstance(date_string, str):
        raise TypeError(f"Expected string, got {type(date_string).__name__}")
    
    # Use datetime for validation
    try:
        parsed = datetime.strptime(date_string, '%Y-%m-%d')
        return {
            'year': parsed.year,
            'month': parsed.month,
            'day': parsed.day
        }
    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected YYYY-MM-DD, got: {date_string}") from e


# =============================================================================
# SAMPLE 5: Rate Limiter - SOLUTIONS
# =============================================================================
"""
ISSUES FOUND:

1. Not thread-safe (Critical)
   - Race condition on self.requests access
   - Multiple threads can exceed limit

2. Unbounded memory growth (High)
   - Old client IDs never removed
   - Memory leak over time

3. Inefficient cleanup (Medium)
   - Rebuilds list on every call
   - Could use more efficient data structure

Total issues: 3
"""

import time
import threading
from collections import defaultdict

class RateLimiterFixed:
    """Thread-safe rate limiter with memory management."""
    
    def __init__(self, max_requests, window_seconds, max_clients=10000):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.max_clients = max_clients
        self.requests = defaultdict(list)
        self.lock = threading.Lock()
        self.last_cleanup = time.time()
    
    def is_allowed(self, client_id):
        """Check if a request from client_id is allowed."""
        now = time.time()
        
        with self.lock:
            self._maybe_cleanup(now)
            
            # Remove old requests for this client
            self.requests[client_id] = [
                t for t in self.requests[client_id]
                if now - t < self.window_seconds
            ]
            
            if len(self.requests[client_id]) < self.max_requests:
                self.requests[client_id].append(now)
                return True
            
            return False
    
    def _maybe_cleanup(self, now):
        """Periodic cleanup of stale entries."""
        if now - self.last_cleanup < self.window_seconds:
            return
        
        self.last_cleanup = now
        
        # Remove empty entries
        empty_clients = [
            cid for cid, times in self.requests.items()
            if not times or now - max(times) > self.window_seconds
        ]
        for cid in empty_clients:
            del self.requests[cid]
        
        # Evict oldest if over limit
        if len(self.requests) > self.max_clients:
            sorted_clients = sorted(
                self.requests.keys(),
                key=lambda k: max(self.requests[k]) if self.requests[k] else 0
            )
            for cid in sorted_clients[:len(self.requests) - self.max_clients]:
                del self.requests[cid]


# =============================================================================
# SAMPLE 6: Config Manager - SOLUTIONS
# =============================================================================
"""
ISSUES FOUND:

1. No file existence check (High)
   - FileNotFoundError if file doesn't exist
   - Should handle gracefully or create default

2. Path traversal vulnerability (High)
   - config_path not validated
   - Could read/write arbitrary files

3. Race condition on save (High)
   - Concurrent writes can corrupt file
   - No file locking

4. Non-atomic writes (Medium)
   - Partial write on crash corrupts config
   - Should write to temp then rename

5. No JSON validation (Medium)
   - Malformed JSON crashes silently
   - Should validate structure

6. Type assumptions (Medium)
   - Assumes config is always a dict
   - Could be list or other JSON type

7. No encoding specified (Low)
   - Could fail on non-ASCII content

8. Silent failures (Medium)
   - Errors not logged or reported

9. No schema validation (Low)
   - Any value can be set for any key

10. Permissions not checked (Medium)
    - Could expose sensitive data

Total issues: 10
"""

import json
import os
import tempfile
import threading

class ConfigManagerFixed:
    """Secure configuration manager."""
    
    ALLOWED_DIR = '/app/config'
    
    def __init__(self, config_path, default_config=None):
        self.config_path = self._validate_path(config_path)
        self.default_config = default_config or {}
        self.lock = threading.Lock()
        self.config = self._load_config()
    
    def _validate_path(self, path):
        """Ensure path is within allowed directory."""
        abs_path = os.path.abspath(path)
        if not abs_path.startswith(os.path.abspath(self.ALLOWED_DIR)):
            raise ValueError(f"Config path must be within {self.ALLOWED_DIR}")
        return abs_path
    
    def _load_config(self):
        """Load config with error handling."""
        if not os.path.exists(self.config_path):
            return self.default_config.copy()
        
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                if not isinstance(config, dict):
                    raise ValueError("Config must be a JSON object")
                return config
        except (json.JSONDecodeError, ValueError) as e:
            # Log error and return default
            print(f"Error loading config: {e}")
            return self.default_config.copy()
    
    def get(self, key, default=None):
        """Get a config value (thread-safe)."""
        with self.lock:
            return self.config.get(key, default)
    
    def set(self, key, value):
        """Set a config value and save atomically."""
        with self.lock:
            self.config[key] = value
            self._save_config()
    
    def _save_config(self):
        """Save config atomically."""
        # Write to temp file
        dir_name = os.path.dirname(self.config_path)
        fd, temp_path = tempfile.mkstemp(dir=dir_name, suffix='.tmp')
        
        try:
            with os.fdopen(fd, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2)
            
            # Atomic rename
            os.replace(temp_path, self.config_path)
        except Exception:
            # Clean up temp file on error
            if os.path.exists(temp_path):
                os.remove(temp_path)
            raise


# =============================================================================
# SAMPLE 7: File Download Handler - SOLUTIONS
# =============================================================================
"""
ISSUES FOUND:

1. No URL validation (Critical)
   - SSRF vulnerability
   - Can fetch internal URLs

2. Path traversal (Critical)
   - save_path not validated
   - Can write to arbitrary locations

3. No error handling (High)
   - Network errors crash
   - File errors not caught

4. No timeout (High)
   - Can hang indefinitely

5. Loads entire file in memory (High)
   - Large files cause OOM
   - Should stream

6. No status code check (High)
   - 404/500 still "succeeds"

7. No content-type validation (Medium)
   - Could download malicious files

Total issues: 7
"""

import os
import requests
from urllib.parse import urlparse

ALLOWED_DOMAINS = {'trusted-cdn.example.com', 'assets.example.com'}
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB
ALLOWED_EXTENSIONS = {'.pdf', '.png', '.jpg', '.jpeg', '.csv'}

def download_file_fixed(url, save_dir):
    """Download a file securely."""
    # Validate URL
    parsed = urlparse(url)
    
    if parsed.scheme not in ('http', 'https'):
        raise ValueError(f"Invalid URL scheme: {parsed.scheme}")
    
    if parsed.netloc not in ALLOWED_DOMAINS:
        raise ValueError(f"Domain not allowed: {parsed.netloc}")
    
    # Get and validate filename
    filename = os.path.basename(parsed.path)
    if not filename or '..' in filename:
        raise ValueError("Invalid filename")
    
    ext = os.path.splitext(filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Extension not allowed: {ext}")
    
    # Validate save path
    save_path = os.path.join(save_dir, filename)
    if not os.path.abspath(save_path).startswith(os.path.abspath(save_dir)):
        raise ValueError("Path traversal detected")
    
    # Download with timeout and streaming
    response = requests.get(url, stream=True, timeout=30)
    response.raise_for_status()
    
    # Check content length
    content_length = int(response.headers.get('content-length', 0))
    if content_length > MAX_FILE_SIZE:
        raise ValueError(f"File too large: {content_length} bytes")
    
    # Stream to file with size check
    downloaded = 0
    with open(save_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            downloaded += len(chunk)
            if downloaded > MAX_FILE_SIZE:
                os.remove(save_path)
                raise ValueError("File exceeded size limit")
            f.write(chunk)
    
    return save_path


# =============================================================================
# SAMPLE 8: Password Reset Token - SOLUTIONS
# =============================================================================
"""
ISSUES FOUND:

1. Insecure random (Critical)
   - random module is not cryptographically secure
   - Should use secrets module

2. Timing attack (High)
   - String comparison leaks timing info
   - Should use constant-time comparison

3. Token stored in plain text (High)
   - Tokens should be hashed
   - Stolen DB exposes all tokens

4. No single-use enforcement (Medium)
   - Token can be reused
   - Should mark as used after verification

5. No rate limiting (Medium)
   - Brute force possible

Total issues: 5
"""

import secrets
import hashlib
import hmac
from datetime import datetime, timedelta

def generate_reset_token_fixed(user_id):
    """Generate a secure password reset token."""
    # Cryptographically secure token
    token = secrets.token_urlsafe(32)
    
    # Hash for storage
    token_hash = hashlib.sha256(token.encode()).hexdigest()
    
    expiry = datetime.utcnow() + timedelta(hours=1)
    
    return {
        'token_for_user': token,  # Send this to user
        'stored_data': {
            'user_id': user_id,
            'token_hash': token_hash,
            'expiry': expiry.isoformat(),
            'used': False
        }
    }

def verify_reset_token_fixed(stored_data, provided_token):
    """Verify a password reset token securely."""
    # Check expiry first
    expiry = datetime.fromisoformat(stored_data['expiry'])
    if datetime.utcnow() > expiry:
        return False
    
    # Check if already used
    if stored_data.get('used', False):
        return False
    
    # Hash provided token
    provided_hash = hashlib.sha256(provided_token.encode()).hexdigest()
    
    # Constant-time comparison
    return hmac.compare_digest(stored_data['token_hash'], provided_hash)


# =============================================================================
# SAMPLE 9: Cache - SOLUTIONS
# =============================================================================
"""
ISSUES FOUND:

1. Not thread-safe (High)
   - Race conditions on concurrent access

2. Memory leak (High)
   - Expired entries only removed on access
   - Inactive keys accumulate

3. delete() raises KeyError (Medium)
   - Should handle missing keys gracefully

4. No size limit (Medium)
   - Cache can grow unbounded

5. Missing time import (Low)
   - Code won't run as-is

Total issues: 5
"""

import time
import threading
from collections import OrderedDict

class CacheFixed:
    """Thread-safe cache with size limit and cleanup."""
    
    def __init__(self, max_size=1000, cleanup_interval=60):
        self.max_size = max_size
        self.cleanup_interval = cleanup_interval
        self.data = OrderedDict()
        self.lock = threading.RLock()
        self.last_cleanup = time.time()
    
    def get(self, key, default=None):
        """Get a value from cache."""
        with self.lock:
            if key in self.data:
                value, expiry = self.data[key]
                if time.time() < expiry:
                    # Move to end (LRU)
                    self.data.move_to_end(key)
                    return value
                else:
                    del self.data[key]
            return default
    
    def set(self, key, value, ttl=300):
        """Set a value in cache."""
        with self.lock:
            self._maybe_cleanup()
            
            # Evict oldest if at capacity
            while len(self.data) >= self.max_size:
                self.data.popitem(last=False)
            
            expiry = time.time() + ttl
            self.data[key] = (value, expiry)
            self.data.move_to_end(key)
    
    def delete(self, key):
        """Delete a key from cache."""
        with self.lock:
            self.data.pop(key, None)  # Safe delete
    
    def _maybe_cleanup(self):
        """Periodic cleanup of expired entries."""
        now = time.time()
        if now - self.last_cleanup < self.cleanup_interval:
            return
        
        self.last_cleanup = now
        expired = [k for k, (v, exp) in self.data.items() if now >= exp]
        for key in expired:
            del self.data[key]


# =============================================================================
# SAMPLE 10: Data Export - SOLUTIONS
# =============================================================================
"""
ISSUES FOUND:

1. Exports passwords (Critical)
   - Password hashes should NEVER be exported

2. Exports SSN (Critical)
   - PII requires special handling
   - Should be masked or excluded

3. No access control (High)
   - Any code can call this
   - Should check permissions

4. No audit logging (High)
   - No record of who exported what

5. Path traversal (Medium)
   - filepath not validated

6. No encryption (High)
   - Sensitive data written in plain text

7. No newline parameter (Low)
   - May cause issues on Windows

Total issues: 7
"""

import csv
import os
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

ALLOWED_FIELDS = {'id', 'name', 'email', 'created_at'}
EXPORT_DIR = '/secure/exports'

def export_users_to_csv_fixed(users, requester_id, fields=None):
    """Export user data with security controls."""
    # Filter to allowed fields only
    fields = fields or ['id', 'name', 'email']
    fields = [f for f in fields if f in ALLOWED_FIELDS]
    
    if not fields:
        raise ValueError("No valid fields specified")
    
    # Generate safe filename
    timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    filename = f"user_export_{timestamp}.csv"
    filepath = os.path.join(EXPORT_DIR, filename)
    
    # Validate path
    if not os.path.abspath(filepath).startswith(os.path.abspath(EXPORT_DIR)):
        raise ValueError("Invalid export path")
    
    # Audit log
    logger.info(
        "user_export",
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
            safe_user = {k: user.get(k, '') for k in fields}
            writer.writerow(safe_user)
    
    return filepath


# =============================================================================
# SCORING GUIDE
# =============================================================================

TOTAL_ISSUES = {
    'sample_1': 3,
    'sample_2': 5,
    'sample_3': 3,
    'sample_4': 4,
    'sample_5': 3,
    'sample_6': 10,
    'sample_7': 7,
    'sample_8': 5,
    'sample_9': 5,
    'sample_10': 7,
}

print(f"""
AI Code Review - Scoring Guide
{'=' * 50}

Total issues across all samples: {sum(TOTAL_ISSUES.values())}

Skill levels:
- Novice (0-30%):     0-{int(sum(TOTAL_ISSUES.values()) * 0.3)} issues found
- Developing (30-50%): {int(sum(TOTAL_ISSUES.values()) * 0.3)}-{int(sum(TOTAL_ISSUES.values()) * 0.5)} issues found
- Competent (50-70%): {int(sum(TOTAL_ISSUES.values()) * 0.5)}-{int(sum(TOTAL_ISSUES.values()) * 0.7)} issues found  
- Advanced (70-85%):  {int(sum(TOTAL_ISSUES.values()) * 0.7)}-{int(sum(TOTAL_ISSUES.values()) * 0.85)} issues found
- Expert (85%+):      {int(sum(TOTAL_ISSUES.values()) * 0.85)}+ issues found
""")