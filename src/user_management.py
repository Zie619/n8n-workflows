#!/usr/bin/env python3
"""
N8N 工作流用户管理系统
多用户访问控制和身份验证。
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, EmailStr
from typing import List, Dict, Any, Optional
import sqlite3
import hashlib
import secrets
import jwt
from datetime import datetime, timedelta
import json
import os

# Configuration - Use environment variables for security
SECRET_KEY = os.environ.get("JWT_SECRET_KEY", secrets.token_urlsafe(32))
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Security
security = HTTPBearer()

class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: EmailStr
    full_name: str
    role: str = "user"
    active: bool = True
    created_at: Optional[str] = None

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    password: str
    role: str = "user"

class UserLogin(BaseModel):
    username: str
    password: str

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None
    active: Optional[bool] = None

class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: int

class UserManager:
    def __init__(self, db_path: str = "users.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """初始化用户数据库。"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                full_name TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT DEFAULT 'user',
                active BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_login TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                token_hash TEXT UNIQUE NOT NULL,
                expires_at TIMESTAMP NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_permissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                resource TEXT NOT NULL,
                action TEXT NOT NULL,
                granted BOOLEAN DEFAULT 1,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
        
        conn.commit()
        conn.close()
        
        # Create default admin user if none exists
        self.create_default_admin()
    
    def create_default_admin(self):
        """如果不存在则创建默认管理员用户。"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM users WHERE role = 'admin'")
        admin_count = cursor.fetchone()[0]
        
        if admin_count == 0:
            # Use environment variable or generate secure random password
            admin_password = os.environ.get("ADMIN_PASSWORD", secrets.token_urlsafe(16))
            password_hash = self.hash_password(admin_password)

            cursor.execute("""
                INSERT INTO users (username, email, full_name, password_hash, role)
                VALUES (?, ?, ?, ?, ?)
            """, ("admin", "admin@n8n-workflows.com", "System Administrator", password_hash, "admin"))

            conn.commit()
            # Only print password if it was auto-generated (not from env)
            if "ADMIN_PASSWORD" not in os.environ:
                print(f"Default admin user created: admin/{admin_password}")
                print("WARNING: Please change this password immediately after first login!")
            else:
                print("Default admin user created with environment-configured password")
        
        conn.close()
    
    def hash_password(self, password: str) -> str:
        """使用 SHA-256 对密码进行哈希处理。"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def verify_password(self, password: str, hashed: str) -> bool:
        """验证密码是否与哈希值匹配。"""
        return self.hash_password(password) == hashed
    
    def create_user(self, user_data: UserCreate) -> User:
        """Create a new user."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            # Check if username or email already exists
            cursor.execute("SELECT COUNT(*) FROM users WHERE username = ? OR email = ?", 
                         (user_data.username, user_data.email))
            if cursor.fetchone()[0] > 0:
                raise ValueError("Username or email already exists")
            
            password_hash = self.hash_password(user_data.password)
            
            cursor.execute("""
                INSERT INTO users (username, email, full_name, password_hash, role)
                VALUES (?, ?, ?, ?, ?)
            """, (user_data.username, user_data.email, user_data.full_name, 
                  password_hash, user_data.role))
            
            user_id = cursor.lastrowid
            conn.commit()
            
            return User(
                id=user_id,
                username=user_data.username,
                email=user_data.email,
                full_name=user_data.full_name,
                role=user_data.role,
                active=True,
                created_at=datetime.now().isoformat()
            )
            
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()
    
    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        """Authenticate user and return user data."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, username, email, full_name, password_hash, role, active
            FROM users WHERE username = ? AND active = 1
        """, (username,))
        
        row = cursor.fetchone()
        conn.close()
        
        if row and self.verify_password(password, row[4]):
            return User(
                id=row[0],
                username=row[1],
                email=row[2],
                full_name=row[3],
                role=row[5],
                active=bool(row[6])
            )
        
        return None
    
    def create_access_token(self, user: User) -> str:
        """Create JWT access token."""
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode = {
            "sub": str(user.id),
            "username": user.username,
            "role": user.role,
            "exp": expire
        }
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    def verify_token(self, token: str) -> Optional[User]:
        """Verify JWT token and return user data."""
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id = payload.get("sub")
            username = payload.get("username")
            role = payload.get("role")
            
            if user_id is None or username is None:
                return None
            
            return User(
                id=int(user_id),
                username=username,
                role=role
            )
        except jwt.PyJWTError:
            return None
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Get user by ID."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, username, email, full_name, role, active, created_at
            FROM users WHERE id = ?
        """, (user_id,))
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return User(
                id=row[0],
                username=row[1],
                email=row[2],
                full_name=row[3],
                role=row[4],
                active=bool(row[5]),
                created_at=row[6]
            )
        
        return None
    
    def get_all_users(self) -> List[User]:
        """Get all users."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, username, email, full_name, role, active, created_at
            FROM users ORDER BY created_at DESC
        """)
        
        users = []
        for row in cursor.fetchall():
            users.append(User(
                id=row[0],
                username=row[1],
                email=row[2],
                full_name=row[3],
                role=row[4],
                active=bool(row[5]),
                created_at=row[6]
            ))
        
        conn.close()
        return users
    
    def update_user(self, user_id: int, update_data: UserUpdate) -> Optional[User]:
        """Update user data."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            # Build update query dynamically
            updates = []
            params = []
            
            if update_data.full_name is not None:
                updates.append("full_name = ?")
                params.append(update_data.full_name)
            
            if update_data.email is not None:
                updates.append("email = ?")
                params.append(update_data.email)
            
            if update_data.role is not None:
                updates.append("role = ?")
                params.append(update_data.role)
            
            if update_data.active is not None:
                updates.append("active = ?")
                params.append(update_data.active)
            
            if not updates:
                return self.get_user_by_id(user_id)
            
            params.append(user_id)
            query = f"UPDATE users SET {', '.join(updates)} WHERE id = ?"
            
            cursor.execute(query, params)
            conn.commit()
            
            return self.get_user_by_id(user_id)
            
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()
    
    def delete_user(self, user_id: int) -> bool:
        """Delete user (soft delete by setting active=False)."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute("UPDATE users SET active = 0 WHERE id = ?", (user_id,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

# Initialize user manager
user_manager = UserManager()

# FastAPI app for User Management
user_app = FastAPI(title="N8N User Management", version="1.0.0")

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    """Get current authenticated user."""
    token = credentials.credentials
    user = user_manager.verify_token(token)
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user

def require_admin(current_user: User = Depends(get_current_user)) -> User:
    """Require admin role."""
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return current_user

@user_app.post("/auth/register", response_model=User)
async def register_user(user_data: UserCreate):
    """Register a new user."""
    try:
        user = user_manager.create_user(user_data)
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@user_app.post("/auth/login", response_model=Token)
async def login_user(login_data: UserLogin):
    """Login user and return access token."""
    user = user_manager.authenticate_user(login_data.username, login_data.password)
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = user_manager.create_access_token(user)
    
    return Token(
        access_token=access_token,
        token_type="bearer",
        expires_in=ACCESS_TOKEN_EXPIRE_MINUTES * 60
    )

@user_app.get("/auth/me", response_model=User)
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    """Get current user information."""
    return current_user

@user_app.get("/users", response_model=List[User])
async def get_all_users(admin: User = Depends(require_admin)):
    """Get all users (admin only)."""
    return user_manager.get_all_users()

@user_app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int, current_user: User = Depends(get_current_user)):
    """Get user by ID."""
    # Users can only view their own profile unless they're admin
    if current_user.id != user_id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Access denied")
    
    user = user_manager.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

@user_app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, update_data: UserUpdate, 
                     current_user: User = Depends(get_current_user)):
    """Update user data."""
    # Users can only update their own profile unless they're admin
    if current_user.id != user_id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Access denied")
    
    # Non-admin users cannot change roles
    if current_user.role != "admin" and update_data.role is not None:
        raise HTTPException(status_code=403, detail="Cannot change role")
    
    user = user_manager.update_user(user_id, update_data)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

@user_app.delete("/users/{user_id}")
async def delete_user(user_id: int, admin: User = Depends(require_admin)):
    """Delete user (admin only)."""
    success = user_manager.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"message": "User deleted successfully"}

@user_app.get("/auth/dashboard")
async def get_auth_dashboard():
    """Get authentication dashboard HTML."""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>N8N User Management</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                color: #333;
            }
            .dashboard {
                max-width: 1000px;
                margin: 0 auto;
                padding: 20px;
            }
            .header {
                background: white;
                padding: 30px;
                border-radius: 15px;
                margin-bottom: 30px;
                text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            }
            .header h1 {
                font-size: 32px;
                margin-bottom: 10px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .auth-section {
                background: white;
                padding: 30px;
                border-radius: 15px;
                margin-bottom: 30px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }
            .auth-tabs {
                display: flex;
                margin-bottom: 20px;
                border-bottom: 2px solid #e9ecef;
            }
            .tab {
                padding: 15px 30px;
                cursor: pointer;
                border-bottom: 3px solid transparent;
                transition: all 0.3s ease;
            }
            .tab.active {
                border-bottom-color: #667eea;
                color: #667eea;
                font-weight: bold;
            }
            .tab-content {
                display: none;
            }
            .tab-content.active {
                display: block;
            }
            .form-group {
                margin-bottom: 20px;
            }
            .form-group label {
                display: block;
                margin-bottom: 8px;
                font-weight: bold;
                color: #333;
            }
            .form-group input {
                width: 100%;
                padding: 12px;
                border: 2px solid #e9ecef;
                border-radius: 8px;
                font-size: 16px;
                transition: border-color 0.3s ease;
            }
            .form-group input:focus {
                outline: none;
                border-color: #667eea;
            }
            .btn {
                padding: 12px 24px;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                cursor: pointer;
                transition: all 0.3s ease;
                text-decoration: none;
                display: inline-block;
                text-align: center;
            }
            .btn-primary {
                background: #667eea;
                color: white;
            }
            .btn-primary:hover {
                background: #5a6fd8;
            }
            .btn-secondary {
                background: #f8f9fa;
                color: #666;
                border: 1px solid #e9ecef;
            }
            .btn-secondary:hover {
                background: #e9ecef;
            }
            .user-list {
                background: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }
            .user-card {
                background: #f8f9fa;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 15px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .user-info h3 {
                margin-bottom: 5px;
                color: #333;
            }
            .user-info p {
                color: #666;
                font-size: 14px;
            }
            .user-role {
                background: #667eea;
                color: white;
                padding: 4px 12px;
                border-radius: 15px;
                font-size: 12px;
                font-weight: bold;
            }
            .user-role.admin {
                background: #dc3545;
            }
            .status-indicator {
                display: inline-block;
                width: 10px;
                height: 10px;
                border-radius: 50%;
                margin-right: 8px;
            }
            .status-online {
                background: #28a745;
            }
            .status-offline {
                background: #dc3545;
            }
            .message {
                padding: 15px;
                border-radius: 8px;
                margin-bottom: 20px;
                display: none;
            }
            .message.success {
                background: #d4edda;
                color: #155724;
                border: 1px solid #c3e6cb;
            }
            .message.error {
                background: #f8d7da;
                color: #721c24;
                border: 1px solid #f5c6cb;
            }
        </style>
    </head>
    <body>
        <div class="dashboard">
            <div class="header">
                <h1>👥 N8N User Management</h1>
                <p>Manage users, roles, and access control for your workflow platform</p>
            </div>
            
            <div class="auth-section">
                <div class="auth-tabs">
                    <div class="tab active" onclick="showTab('login')">Login</div>
                    <div class="tab" onclick="showTab('register')">Register</div>
                </div>
                
                <div id="message" class="message"></div>
                
                <div id="login" class="tab-content active">
                    <h2>Login to Your Account</h2>
                    <form id="loginForm">
                        <div class="form-group">
                            <label for="loginUsername">Username</label>
                            <input type="text" id="loginUsername" required>
                        </div>
                        <div class="form-group">
                            <label for="loginPassword">Password</label>
                            <input type="password" id="loginPassword" required>
                        </div>
                        <button type="submit" class="btn btn-primary">Login</button>
                    </form>
                </div>
                
                <div id="register" class="tab-content">
                    <h2>Create New Account</h2>
                    <form id="registerForm">
                        <div class="form-group">
                            <label for="regUsername">Username</label>
                            <input type="text" id="regUsername" required>
                        </div>
                        <div class="form-group">
                            <label for="regEmail">Email</label>
                            <input type="email" id="regEmail" required>
                        </div>
                        <div class="form-group">
                            <label for="regFullName">Full Name</label>
                            <input type="text" id="regFullName" required>
                        </div>
                        <div class="form-group">
                            <label for="regPassword">Password</label>
                            <input type="password" id="regPassword" required>
                        </div>
                        <button type="submit" class="btn btn-primary">Register</button>
                    </form>
                </div>
            </div>
            
            <div class="user-list" id="userList" style="display: none;">
                <h2>User Management</h2>
                <div id="usersContainer">
                    <div class="loading">Loading users...</div>
                </div>
            </div>
        </div>
        
        <script>
            let currentUser = null;
            let authToken = null;
            
            function showTab(tabName) {
                // Hide all tabs
                document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
                document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
                
                // Show selected tab
                event.target.classList.add('active');
                document.getElementById(tabName).classList.add('active');
            }
            
            function showMessage(message, type) {
                const messageDiv = document.getElementById('message');
                messageDiv.textContent = message;
                messageDiv.className = `message ${type}`;
                messageDiv.style.display = 'block';
                
                setTimeout(() => {
                    messageDiv.style.display = 'none';
                }, 5000);
            }
            
            async function login(username, password) {
                try {
                    const response = await fetch('/auth/login', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({username, password})
                    });
                    
                    if (response.ok) {
                        const data = await response.json();
                        authToken = data.access_token;
                        currentUser = await getCurrentUser();
                        showMessage('Login successful!', 'success');
                        loadUsers();
                    } else {
                        const error = await response.json();
                        showMessage(error.detail || 'Login failed', 'error');
                    }
                } catch (error) {
                    showMessage('Login error: ' + error.message, 'error');
                }
            }
            
            async function register(username, email, fullName, password) {
                try {
                    const response = await fetch('/auth/register', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({username, email, full_name: fullName, password, role: 'user'})
                    });
                    
                    if (response.ok) {
                        showMessage('Registration successful! Please login.', 'success');
                        showTab('login');
                    } else {
                        const error = await response.json();
                        showMessage(error.detail || 'Registration failed', 'error');
                    }
                } catch (error) {
                    showMessage('Registration error: ' + error.message, 'error');
                }
            }
            
            async function getCurrentUser() {
                if (!authToken) return null;
                
                try {
                    const response = await fetch('/auth/me', {
                        headers: {'Authorization': `Bearer ${authToken}`}
                    });
                    
                    if (response.ok) {
                        return await response.json();
                    }
                } catch (error) {
                    console.error('Error getting current user:', error);
                }
                return null;
            }
            
            async function loadUsers() {
                if (!authToken) return;
                
                try {
                    const response = await fetch('/users', {
                        headers: {'Authorization': `Bearer ${authToken}`}
                    });
                    
                    if (response.ok) {
                        const users = await response.json();
                        displayUsers(users);
                        document.getElementById('userList').style.display = 'block';
                    } else {
                        showMessage('Failed to load users', 'error');
                    }
                } catch (error) {
                    showMessage('Error loading users: ' + error.message, 'error');
                }
            }
            
            function displayUsers(users) {
                const container = document.getElementById('usersContainer');
                container.innerHTML = users.map(user => `
                    <div class="user-card">
                        <div class="user-info">
                            <h3>${user.full_name}</h3>
                            <p>@${user.username} • ${user.email}</p>
                        </div>
                        <div>
                            <span class="user-role ${user.role}">${user.role.toUpperCase()}</span>
                            <span class="status-indicator ${user.active ? 'status-online' : 'status-offline'}"></span>
                        </div>
                    </div>
                `).join('');
            }
            
            // Event listeners
            document.getElementById('loginForm').addEventListener('submit', (e) => {
                e.preventDefault();
                const username = document.getElementById('loginUsername').value;
                const password = document.getElementById('loginPassword').value;
                login(username, password);
            });
            
            document.getElementById('registerForm').addEventListener('submit', (e) => {
                e.preventDefault();
                const username = document.getElementById('regUsername').value;
                const email = document.getElementById('regEmail').value;
                const fullName = document.getElementById('regFullName').value;
                const password = document.getElementById('regPassword').value;
                register(username, email, fullName, password);
            });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(user_app, host="127.0.0.1", port=8004)
