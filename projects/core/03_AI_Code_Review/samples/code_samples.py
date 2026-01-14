"""
AI Code Review - Practice Samples

These are AI-generated code samples with intentional issues.
Your task: Review each function and identify all problems.

DO NOT look at the solutions file until you've completed your review.
"""


# =============================================================================
# SAMPLE 1: Calculate Average
# Difficulty: Easy
# =============================================================================

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    total = sum(numbers)
    return total / len(numbers)


# =============================================================================
# SAMPLE 2: User Authentication
# Difficulty: Medium
# =============================================================================

import sqlite3

def authenticate_user(username, password):
    """Check if username and password are valid."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    
    user = cursor.fetchone()
    conn.close()
    
    return user is not None


# =============================================================================
# SAMPLE 3: Find Duplicates
# Difficulty: Medium
# =============================================================================

def find_duplicates(items):
    """Find all duplicate items in a list."""
    duplicates = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                if items[i] not in duplicates:
                    duplicates.append(items[i])
    return duplicates


# =============================================================================
# SAMPLE 4: Parse Date
# Difficulty: Easy
# =============================================================================

def parse_date(date_string):
    """Parse a date string in format YYYY-MM-DD."""
    parts = date_string.split('-')
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    return {'year': year, 'month': month, 'day': day}


# =============================================================================
# SAMPLE 5: Rate Limiter
# Difficulty: Hard
# =============================================================================

import time

class RateLimiter:
    """Limit requests to max_requests per window_seconds."""
    
    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = {}
    
    def is_allowed(self, client_id):
        """Check if a request from client_id is allowed."""
        now = time.time()
        
        if client_id not in self.requests:
            self.requests[client_id] = []
        
        # Remove old requests
        self.requests[client_id] = [
            t for t in self.requests[client_id] 
            if now - t < self.window_seconds
        ]
        
        if len(self.requests[client_id]) < self.max_requests:
            self.requests[client_id].append(now)
            return True
        
        return False


# =============================================================================
# SAMPLE 6: Config Manager (Complex)
# Difficulty: Hard
# =============================================================================

import json

class ConfigManager:
    """Manage application configuration from JSON file."""
    
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self._load_config()
    
    def _load_config(self):
        with open(self.config_path, 'r') as f:
            return json.load(f)
    
    def get(self, key, default=None):
        """Get a config value."""
        return self.config.get(key, default)
    
    def set(self, key, value):
        """Set a config value and save."""
        self.config[key] = value
        self._save_config()
    
    def _save_config(self):
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f)


# =============================================================================
# SAMPLE 7: File Download Handler
# Difficulty: Hard
# =============================================================================

import os
import requests

def download_file(url, save_path):
    """Download a file from URL and save to disk."""
    response = requests.get(url)
    
    with open(save_path, 'wb') as f:
        f.write(response.content)
    
    return save_path


# =============================================================================
# SAMPLE 8: Password Reset Token
# Difficulty: Hard
# =============================================================================

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


# =============================================================================
# SAMPLE 9: Cache Implementation
# Difficulty: Medium
# =============================================================================

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


# =============================================================================
# SAMPLE 10: Data Export
# Difficulty: Medium
# =============================================================================

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


# =============================================================================
# SAMPLE 11: Webhook Handler (Flask)
# Difficulty: Hard
# =============================================================================

# Note: This would require Flask to run
# from flask import Flask, request
# import subprocess
# 
# app = Flask(__name__)
# 
# @app.route('/webhook', methods=['POST'])
# def handle_webhook():
#     """Handle incoming webhook."""
#     data = request.json
#     
#     # Run deployment script
#     branch = data['ref'].split('/')[-1]
#     result = subprocess.run(
#         f'./deploy.sh {branch}',
#         shell=True,
#         capture_output=True
#     )
#     
#     return {'status': 'ok', 'output': result.stdout.decode()}


# =============================================================================
# SAMPLE 12: Rate Limiter Decorator
# Difficulty: Medium
# =============================================================================

from functools import wraps

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


# =============================================================================
# YOUR REVIEW TRACKING
# =============================================================================

"""
Track your findings here:

Sample 1 - Calculate Average:
- Issues found:
- Severity:
- Missed issues (after checking solutions):

Sample 2 - User Authentication:
- Issues found:
- Severity:
- Missed issues:

Sample 3 - Find Duplicates:
- Issues found:
- Severity:
- Missed issues:

... continue for all samples
"""


if __name__ == "__main__":
    print("AI Code Review - Practice Samples")
    print("=" * 50)
    print()
    print("Instructions:")
    print("1. Review each function above")
    print("2. Document all issues you find")
    print("3. Classify severity (Critical/High/Medium/Low)")
    print("4. Check against solutions.py when done")
    print()
    print("Tip: Run this file to test the code behavior")
    print()
    
    # Quick tests to demonstrate issues
    print("Quick demonstrations:")
    print("-" * 30)
    
    # Sample 1: Empty list
    try:
        result = calculate_average([])
        print(f"calculate_average([]) = {result}")
    except Exception as e:
        print(f"calculate_average([]) raised: {type(e).__name__}")
    
    # Sample 3: Performance
    import time
    large_list = list(range(1000)) + list(range(500))  # Has duplicates
    start = time.time()
    find_duplicates(large_list)
    elapsed = time.time() - start
    print(f"find_duplicates(1500 items) took {elapsed:.3f}s")
    
    # Sample 4: Invalid input
    try:
        result = parse_date("not-a-date")
        print(f"parse_date('not-a-date') = {result}")
    except Exception as e:
        print(f"parse_date('not-a-date') raised: {type(e).__name__}")