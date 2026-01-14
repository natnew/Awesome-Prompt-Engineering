[← Back to Project](README.md)

# Extended Code Review Exercises

Additional code samples for practice. Each contains intentional issues.

---

## Exercise Set 2: Web Application Code

### Sample 7: File Upload Handler

```python
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file uploads from users."""
    file = request.files['file']
    filename = file.filename
    
    # Save to uploads directory
    upload_path = os.path.join('uploads', filename)
    file.save(upload_path)
    
    return f"File {filename} uploaded successfully"
```

**Your Review:**

| Issue # | Description | Severity | Line |
|:--------|:------------|:---------|:-----|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

<details>
<summary>Click to reveal issues</summary>

**Issues Found:**

1. **Path traversal vulnerability** (Critical, Line 12): `filename` is user-controlled. An attacker could use `../../../etc/passwd` to write anywhere.

2. **No file type validation** (High): Any file type can be uploaded, including executables.

3. **No file size limit** (High): Could be used for denial of service.

4. **No authentication** (High): Anyone can upload files.

5. **Filename collision** (Medium): Overwrites existing files without warning.

6. **Missing 'file' key handling** (Medium, Line 9): Will crash if 'file' not in request.

**Secure version:**
```python
import os
import uuid
from flask import Flask, request, abort
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        abort(400, 'No file provided')
    
    file = request.files['file']
    if file.filename == '':
        abort(400, 'No file selected')
    
    if not allowed_file(file.filename):
        abort(400, 'File type not allowed')
    
    # Use secure filename + UUID to prevent collisions and traversal
    safe_name = secure_filename(file.filename)
    unique_name = f"{uuid.uuid4()}_{safe_name}"
    upload_path = os.path.join('uploads', unique_name)
    
    file.save(upload_path)
    return f"File uploaded as {unique_name}"
```
</details>

---

### Sample 8: Session Management

```python
import hashlib
import time

class SessionManager:
    """Manage user sessions."""
    
    def __init__(self):
        self.sessions = {}
    
    def create_session(self, user_id):
        """Create a new session for a user."""
        session_id = hashlib.md5(str(time.time()).encode()).hexdigest()
        self.sessions[session_id] = {
            'user_id': user_id,
            'created': time.time()
        }
        return session_id
    
    def get_user(self, session_id):
        """Get user from session."""
        session = self.sessions.get(session_id)
        if session:
            return session['user_id']
        return None
    
    def logout(self, session_id):
        """End a session."""
        if session_id in self.sessions:
            del self.sessions[session_id]
```

**Your Review:**

| Issue # | Description | Severity | Line |
|:--------|:------------|:---------|:-----|
| 1 | | | |
| 2 | | | |
| 3 | | | |

<details>
<summary>Click to reveal issues</summary>

**Issues Found:**

1. **Weak session ID generation** (Critical, Line 12): MD5 of time is predictable. Attackers can guess valid session IDs.

2. **No session expiration** (High): Sessions never expire, even after long inactivity.

3. **In-memory storage only** (Medium): Sessions lost on restart, doesn't scale horizontally.

4. **No session fixation protection** (Medium): Should regenerate session ID after login.

5. **MD5 is deprecated** (Medium): Should use secrets.token_urlsafe() for session IDs.

**Secure version:**
```python
import secrets
import time

class SessionManager:
    SESSION_DURATION = 3600  # 1 hour
    
    def __init__(self):
        self.sessions = {}
    
    def create_session(self, user_id):
        session_id = secrets.token_urlsafe(32)
        self.sessions[session_id] = {
            'user_id': user_id,
            'created': time.time(),
            'last_access': time.time()
        }
        return session_id
    
    def get_user(self, session_id):
        session = self.sessions.get(session_id)
        if not session:
            return None
        
        # Check expiration
        if time.time() - session['last_access'] > self.SESSION_DURATION:
            del self.sessions[session_id]
            return None
        
        session['last_access'] = time.time()
        return session['user_id']
    
    def cleanup_expired(self):
        """Remove expired sessions."""
        now = time.time()
        expired = [
            sid for sid, s in self.sessions.items()
            if now - s['last_access'] > self.SESSION_DURATION
        ]
        for sid in expired:
            del self.sessions[sid]
```
</details>

---

### Sample 9: API Endpoint

```python
from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/api/ping', methods=['POST'])
def ping_host():
    """Ping a host to check if it's reachable."""
    data = request.get_json()
    host = data['host']
    
    # Run ping command
    result = subprocess.run(
        f"ping -c 3 {host}",
        shell=True,
        capture_output=True,
        text=True
    )
    
    return jsonify({
        'host': host,
        'reachable': result.returncode == 0,
        'output': result.stdout
    })
```

**Your Review:**

| Issue # | Description | Severity |
|:--------|:------------|:---------|
| 1 | | |
| 2 | | |

<details>
<summary>Click to reveal issues</summary>

**Issues Found:**

1. **Command injection** (Critical, Line 13-17): User input directly in shell command. Attacker can run: `{"host": "google.com; cat /etc/passwd"}`.

2. **No input validation** (High): No validation of host format.

3. **Information disclosure** (Medium, Line 21): Full command output exposed to user.

4. **Missing 'host' key handling** (Medium): Will crash if key missing.

5. **No rate limiting** (Medium): Could be used for DDoS via ping.

**Secure version:**
```python
import re
import subprocess
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

HOST_PATTERN = re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9\-\.]{0,253}[a-zA-Z0-9]$')

@app.route('/api/ping', methods=['POST'])
def ping_host():
    data = request.get_json()
    if not data or 'host' not in data:
        abort(400, 'Missing host parameter')
    
    host = data['host']
    
    # Validate hostname format
    if not HOST_PATTERN.match(host):
        abort(400, 'Invalid hostname format')
    
    # Use list form to avoid shell injection
    result = subprocess.run(
        ['ping', '-c', '3', host],
        capture_output=True,
        text=True,
        timeout=10
    )
    
    return jsonify({
        'host': host,
        'reachable': result.returncode == 0
        # Don't expose full output
    })
```
</details>

---

## Exercise Set 3: Data Processing

### Sample 10: CSV Parser

```python
def parse_csv(csv_string):
    """Parse a CSV string into a list of dictionaries."""
    lines = csv_string.strip().split('\n')
    headers = lines[0].split(',')
    
    results = []
    for line in lines[1:]:
        values = line.split(',')
        row = {}
        for i, header in enumerate(headers):
            row[header] = values[i]
        results.append(row)
    
    return results
```

**Your Review:**

| Issue # | Description | Severity |
|:--------|:------------|:---------|
| 1 | | |
| 2 | | |
| 3 | | |

<details>
<summary>Click to reveal issues</summary>

**Issues Found:**

1. **Doesn't handle quoted fields** (High): `"Hello, World"` would be split incorrectly.

2. **Index out of bounds** (High, Line 11): If a row has fewer values than headers, raises IndexError.

3. **No empty input handling** (Medium): Empty string causes index error at Line 3.

4. **Doesn't handle escaped quotes** (Medium): Can't parse `"He said ""Hello"""`.

5. **No newlines in values** (Medium): Multi-line values not supported.

6. **Whitespace handling** (Low): Doesn't strip whitespace from values.

**Better approach:**
```python
import csv
from io import StringIO

def parse_csv(csv_string):
    """Parse a CSV string into a list of dictionaries."""
    if not csv_string or not csv_string.strip():
        return []
    
    reader = csv.DictReader(StringIO(csv_string))
    return list(reader)
```

Or if you must implement manually:
```python
def parse_csv(csv_string):
    if not csv_string or not csv_string.strip():
        return []
    
    lines = csv_string.strip().split('\n')
    if len(lines) < 2:
        return []
    
    headers = [h.strip() for h in lines[0].split(',')]
    
    results = []
    for line in lines[1:]:
        values = [v.strip() for v in line.split(',')]
        row = {}
        for i, header in enumerate(headers):
            row[header] = values[i] if i < len(values) else ''
        results.append(row)
    
    return results
```
</details>

---

### Sample 11: Data Aggregation

```python
def aggregate_sales(transactions):
    """Aggregate sales by product category."""
    totals = {}
    
    for t in transactions:
        category = t['category']
        amount = t['amount']
        
        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount
    
    return totals
```

**Your Review:**

| Issue # | Description | Severity |
|:--------|:------------|:---------|
| 1 | | |
| 2 | | |

<details>
<summary>Click to reveal issues</summary>

**Issues Found:**

1. **Floating point accumulation error** (Medium): Summing floats can accumulate errors. For financial data, use Decimal.

2. **Missing key handling** (Medium): Assumes all transactions have 'category' and 'amount'.

3. **No type validation** (Low): Doesn't verify amount is numeric.

4. **Could use defaultdict** (Style): More Pythonic with collections.defaultdict.

**Improved version:**
```python
from collections import defaultdict
from decimal import Decimal

def aggregate_sales(transactions):
    """Aggregate sales by product category."""
    if not transactions:
        return {}
    
    totals = defaultdict(Decimal)
    
    for t in transactions:
        category = t.get('category', 'Unknown')
        amount = t.get('amount', 0)
        
        # Convert to Decimal for precision
        if isinstance(amount, (int, float)):
            amount = Decimal(str(amount))
        
        totals[category] += amount
    
    return dict(totals)
```
</details>

---

### Sample 12: Caching Decorator

```python
def cache(func):
    """Cache function results."""
    cached = {}
    
    def wrapper(*args):
        if args in cached:
            return cached[args]
        result = func(*args)
        cached[args] = result
        return result
    
    return wrapper

@cache
def expensive_computation(n):
    """Some expensive computation."""
    return sum(range(n))
```

**Your Review:**

| Issue # | Description | Severity |
|:--------|:------------|:---------|
| 1 | | |
| 2 | | |
| 3 | | |

<details>
<summary>Click to reveal issues</summary>

**Issues Found:**

1. **Memory leak** (High): Cache grows unbounded, never evicted.

2. **Unhashable arguments** (Medium): Fails if args contain lists or dicts.

3. **No kwargs support** (Medium, Line 6): Ignores keyword arguments entirely.

4. **Not thread-safe** (Medium): Race condition on cache access.

5. **Loses function metadata** (Low): Should use @functools.wraps.

**Improved version:**
```python
from functools import wraps, lru_cache
import threading

def cache(maxsize=128):
    """Thread-safe LRU cache decorator."""
    def decorator(func):
        # Use built-in lru_cache
        cached_func = lru_cache(maxsize=maxsize)(func)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Convert kwargs to hashable form
            key = (args, tuple(sorted(kwargs.items())))
            return cached_func(*args, **kwargs)
        
        wrapper.cache_clear = cached_func.cache_clear
        wrapper.cache_info = cached_func.cache_info
        return wrapper
    return decorator

# Or simply use:
@lru_cache(maxsize=128)
def expensive_computation(n):
    return sum(range(n))
```
</details>

---

## Exercise Set 4: Async & Concurrent Code

### Sample 13: Async HTTP Client

```python
import asyncio
import aiohttp

async def fetch_all(urls):
    """Fetch multiple URLs concurrently."""
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = session.get(url)
            tasks.append(task)
        
        responses = await asyncio.gather(*tasks)
        
        results = []
        for response in responses:
            data = await response.json()
            results.append(data)
        
        return results
```

**Your Review:**

| Issue # | Description | Severity |
|:--------|:------------|:---------|
| 1 | | |
| 2 | | |
| 3 | | |

<details>
<summary>Click to reveal issues</summary>

**Issues Found:**

1. **Resource leak** (High, Line 8): `session.get()` returns response that needs context manager or explicit close.

2. **No error handling** (High): One failed request fails everything.

3. **No timeout** (Medium): Requests could hang forever.

4. **No rate limiting** (Medium): Could overwhelm target servers.

5. **JSON parse errors not handled** (Medium, Line 14): Not all responses are JSON.

**Improved version:**
```python
import asyncio
import aiohttp
from aiohttp import ClientTimeout

async def fetch_url(session, url, timeout=30):
    """Fetch a single URL with error handling."""
    try:
        async with session.get(url, timeout=ClientTimeout(total=timeout)) as response:
            if response.status == 200:
                return await response.json()
            else:
                return {'error': f'HTTP {response.status}', 'url': url}
    except asyncio.TimeoutError:
        return {'error': 'timeout', 'url': url}
    except aiohttp.ClientError as e:
        return {'error': str(e), 'url': url}
    except Exception as e:
        return {'error': str(e), 'url': url}

async def fetch_all(urls, max_concurrent=10):
    """Fetch multiple URLs with concurrency limit."""
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def bounded_fetch(session, url):
        async with semaphore:
            return await fetch_url(session, url)
    
    async with aiohttp.ClientSession() as session:
        tasks = [bounded_fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)
```
</details>

---

### Sample 14: Thread Pool

```python
import threading

class ThreadPool:
    """Simple thread pool for parallel execution."""
    
    def __init__(self, num_workers):
        self.tasks = []
        self.results = []
        self.workers = []
        
        for _ in range(num_workers):
            worker = threading.Thread(target=self._worker)
            worker.start()
            self.workers.append(worker)
    
    def _worker(self):
        while self.tasks:
            task = self.tasks.pop(0)
            result = task()
            self.results.append(result)
    
    def submit(self, task):
        self.tasks.append(task)
    
    def get_results(self):
        for worker in self.workers:
            worker.join()
        return self.results
```

**Your Review:**

| Issue # | Description | Severity |
|:--------|:------------|:---------|
| 1 | | |
| 2 | | |
| 3 | | |

<details>
<summary>Click to reveal issues</summary>

**Issues Found:**

1. **Race condition on tasks list** (Critical, Line 16-17): Multiple threads pop from same list without locking.

2. **Race condition on results** (Critical, Line 18): Multiple threads append to results without locking.

3. **Workers exit immediately** (High, Line 15): Workers check `while self.tasks` and exit when empty, even if more tasks coming.

4. **No task ordering** (Medium): Results don't correspond to task submission order.

5. **No exception handling** (Medium): One task failure affects worker.

6. **No shutdown mechanism** (Medium): Workers need clean shutdown.

**Improved version:**
```python
import threading
from queue import Queue
from concurrent.futures import ThreadPoolExecutor

# Best: Just use the standard library
def parallel_execute(tasks, num_workers=4):
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        return list(executor.map(lambda t: t(), tasks))

# Or if implementing manually:
class ThreadPool:
    def __init__(self, num_workers):
        self.task_queue = Queue()
        self.results = []
        self.results_lock = threading.Lock()
        self.shutdown_flag = threading.Event()
        
        self.workers = []
        for _ in range(num_workers):
            worker = threading.Thread(target=self._worker)
            worker.daemon = True
            worker.start()
            self.workers.append(worker)
    
    def _worker(self):
        while not self.shutdown_flag.is_set():
            try:
                task = self.task_queue.get(timeout=0.1)
                try:
                    result = task()
                    with self.results_lock:
                        self.results.append(result)
                except Exception as e:
                    with self.results_lock:
                        self.results.append(e)
                finally:
                    self.task_queue.task_done()
            except:
                continue
    
    def submit(self, task):
        self.task_queue.put(task)
    
    def get_results(self):
        self.task_queue.join()
        self.shutdown_flag.set()
        return self.results.copy()
```
</details>

---

## Scoring Your Reviews

After completing all exercises, calculate your score:

| Category | Samples | Critical Found | High Found | Medium Found | Total Issues |
|:---------|:--------|:---------------|:-----------|:-------------|:-------------|
| Basic Functions | 1-6 | /6 | /8 | /10 | |
| Web Application | 7-9 | /4 | /6 | /6 | |
| Data Processing | 10-12 | /1 | /4 | /6 | |
| Concurrent | 13-14 | /3 | /4 | /4 | |
| **Total** | | | | | |

### Interpreting Your Score

**Critical issues caught:**
- 100%: Excellent security awareness
- 75-99%: Good, but review security fundamentals
- <75%: Security training recommended

**High issues caught:**
- 80%+: Strong code review skills
- 60-79%: Solid foundation, practice edge cases
- <60%: Focus on error handling and validation

**Medium issues caught:**
- 70%+: Thorough reviewer
- 50-69%: Average, catches main issues
- <50%: May miss maintainability issues

---

## Building Your Final Checklist

Based on what you missed, customize your checklist:

```markdown
# My AI Code Review Checklist

## My Blind Spots (Issues I Missed)
- [ ] ____
- [ ] ____
- [ ] ____

## Security (I should always check)
- [ ] ____
- [ ] ____

## Error Handling (I often miss)
- [ ] ____
- [ ] ____

## Performance (I should consider)
- [ ] ____
- [ ] ____

## Concurrency (If applicable)
- [ ] ____
- [ ] ____
```

---

[← Back to Project](README.md)
