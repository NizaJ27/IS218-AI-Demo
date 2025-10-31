"""
User Management System for The Bread Therapist Collective

Handles user authentication, profile management, and session tracking.
"""

import json
import hashlib
import os
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, List


class UserManager:
    """Manages user profiles, authentication, and session data."""
    
    def __init__(self, data_dir: str = "user_data"):
        self.data_dir = Path(data_dir)
        self.profiles_dir = self.data_dir / "profiles"
        self.sessions_dir = self.data_dir / "sessions"
        
        # Ensure directories exist
        self.profiles_dir.mkdir(parents=True, exist_ok=True)
        self.sessions_dir.mkdir(parents=True, exist_ok=True)
    
    def _hash_password(self, password: str) -> str:
        """Hash password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def _get_profile_path(self, username: str) -> Path:
        """Get path to user profile file."""
        return self.profiles_dir / f"{username}.json"
    
    def _get_session_path(self, username: str) -> Path:
        """Get path to user session directory."""
        user_session_dir = self.sessions_dir / username
        user_session_dir.mkdir(exist_ok=True)
        return user_session_dir
    
    def create_user(self, username: str, password: str, initial_data: Dict = None) -> bool:
        """
        Create a new user profile.
        
        Args:
            username: Unique username
            password: User password (will be hashed)
            initial_data: Optional initial profile data
            
        Returns:
            True if user created successfully, False if user already exists
        """
        profile_path = self._get_profile_path(username)
        
        if profile_path.exists():
            return False
        
        profile = {
            "username": username,
            "password_hash": self._hash_password(password),
            "created_at": datetime.now().isoformat(),
            "last_login": None,
            "assigned_therapist": None,
            "recommended_therapist": None,
            "intake_completed": False,
            "intake_responses": {},
            "therapy_goals": [],
            "progress_notes": [],
            "total_sessions": 0,
            "session_history": [],
            **(initial_data or {})
        }
        
        with open(profile_path, 'w') as f:
            json.dump(profile, f, indent=2)
        
        return True
    
    def authenticate(self, username: str, password: str) -> bool:
        """
        Authenticate a user.
        
        Args:
            username: Username
            password: Password to verify
            
        Returns:
            True if authentication successful, False otherwise
        """
        profile_path = self._get_profile_path(username)
        
        if not profile_path.exists():
            return False
        
        with open(profile_path, 'r') as f:
            profile = json.load(f)
        
        password_hash = self._hash_password(password)
        
        if profile['password_hash'] == password_hash:
            # Update last login
            profile['last_login'] = datetime.now().isoformat()
            with open(profile_path, 'w') as f:
                json.dump(profile, f, indent=2)
            return True
        
        return False
    
    def get_user_profile(self, username: str) -> Optional[Dict]:
        """Get user profile data."""
        profile_path = self._get_profile_path(username)
        
        if not profile_path.exists():
            return None
        
        with open(profile_path, 'r') as f:
            return json.load(f)
    
    def update_user_profile(self, username: str, updates: Dict) -> bool:
        """
        Update user profile with new data.
        
        Args:
            username: Username
            updates: Dictionary of fields to update
            
        Returns:
            True if successful, False if user doesn't exist
        """
        profile_path = self._get_profile_path(username)
        
        if not profile_path.exists():
            return False
        
        with open(profile_path, 'r') as f:
            profile = json.load(f)
        
        profile.update(updates)
        
        with open(profile_path, 'w') as f:
            json.dump(profile, f, indent=2)
        
        return True
    
    def save_intake_assessment(self, username: str, responses: Dict, recommended_therapist: str) -> bool:
        """Save intake assessment responses and therapist recommendation."""
        return self.update_user_profile(username, {
            "intake_completed": True,
            "intake_responses": responses,
            "recommended_therapist": recommended_therapist,
            "intake_date": datetime.now().isoformat()
        })
    
    def log_session(self, username: str, therapist: str, messages: List[Dict]) -> str:
        """
        Log a therapy session.
        
        Args:
            username: Username
            therapist: Therapist name
            messages: List of message dictionaries
            
        Returns:
            Session ID (timestamp-based filename)
        """
        session_dir = self._get_session_path(username)
        session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        session_file = session_dir / f"session_{session_id}.json"
        
        session_data = {
            "session_id": session_id,
            "username": username,
            "therapist": therapist,
            "start_time": datetime.now().isoformat(),
            "messages": messages,
            "message_count": len(messages)
        }
        
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2)
        
        # Update user profile
        profile = self.get_user_profile(username)
        if profile:
            profile['total_sessions'] = profile.get('total_sessions', 0) + 1
            profile['session_history'].append({
                "session_id": session_id,
                "therapist": therapist,
                "date": datetime.now().isoformat(),
                "message_count": len(messages)
            })
            self.update_user_profile(username, profile)
        
        return session_id
    
    def get_session_history(self, username: str) -> List[Dict]:
        """Get all sessions for a user."""
        session_dir = self._get_session_path(username)
        sessions = []
        
        for session_file in sorted(session_dir.glob("session_*.json")):
            with open(session_file, 'r') as f:
                sessions.append(json.load(f))
        
        return sessions
    
    def add_progress_note(self, username: str, note: str, therapist: str = None) -> bool:
        """Add a progress note to user profile."""
        profile = self.get_user_profile(username)
        if not profile:
            return False
        
        progress_note = {
            "date": datetime.now().isoformat(),
            "note": note,
            "therapist": therapist
        }
        
        profile['progress_notes'].append(progress_note)
        return self.update_user_profile(username, {"progress_notes": profile['progress_notes']})
    
    def set_therapy_goals(self, username: str, goals: List[str]) -> bool:
        """Set therapy goals for a user."""
        return self.update_user_profile(username, {"therapy_goals": goals})
