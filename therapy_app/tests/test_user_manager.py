"""
Unit tests for UserManager class.

Tests user authentication, profile management, session logging, and progress tracking.
"""

import json
import os
import tempfile
import shutil
from pathlib import Path
from datetime import datetime
from unittest.mock import patch, Mock

import pytest

from src.user_manager import UserManager


@pytest.fixture
def temp_user_data_dir():
    """Create a temporary directory for user data during tests."""
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)


@pytest.fixture
def user_manager(temp_user_data_dir):
    """Create a UserManager instance with temporary data directory."""
    return UserManager(data_dir=temp_user_data_dir)


class TestUserManagerInitialization:
    """Tests for UserManager initialization."""

    def test_initialization_creates_directories(self, temp_user_data_dir):
        """Test that initialization creates required directories."""
        manager = UserManager(data_dir=temp_user_data_dir)
        
        assert Path(temp_user_data_dir, "profiles").exists()
        assert Path(temp_user_data_dir, "sessions").exists()

    def test_initialization_with_existing_directories(self, temp_user_data_dir):
        """Test initialization when directories already exist."""
        # Create directories first
        Path(temp_user_data_dir, "profiles").mkdir(parents=True)
        Path(temp_user_data_dir, "sessions").mkdir(parents=True)
        
        # Should not raise an error
        manager = UserManager(data_dir=temp_user_data_dir)
        assert manager is not None


class TestUserCreation:
    """Tests for user creation and registration."""

    def test_create_user_success(self, user_manager):
        """Test successful user creation."""
        result = user_manager.create_user("testuser", "password123", {"email": "test@example.com"})
        
        assert result is True
        assert user_manager.get_user_profile("testuser") is not None

    def test_create_user_with_initial_data(self, user_manager):
        """Test user creation with initial profile data."""
        initial_data = {
            "email": "test@example.com",
            "age": 25,
            "preferred_name": "Test"
        }
        
        user_manager.create_user("testuser", "password123", initial_data)
        profile = user_manager.get_user_profile("testuser")
        
        assert profile["email"] == "test@example.com"
        assert profile["age"] == 25
        assert profile["preferred_name"] == "Test"

    def test_create_user_hashes_password(self, user_manager):
        """Test that passwords are hashed, not stored as plain text."""
        user_manager.create_user("testuser", "password123")
        profile = user_manager.get_user_profile("testuser")
        
        assert profile["password_hash"] != "password123"
        assert len(profile["password_hash"]) == 64  # SHA-256 produces 64-char hex string

    def test_create_duplicate_user_fails(self, user_manager):
        """Test that creating a duplicate username fails."""
        user_manager.create_user("testuser", "password123")
        result = user_manager.create_user("testuser", "newpassword")
        
        assert result is False

    def test_create_user_sets_timestamps(self, user_manager):
        """Test that user creation sets created_at and last_login timestamps."""
        user_manager.create_user("testuser", "password123")
        profile = user_manager.get_user_profile("testuser")
        
        assert "created_at" in profile
        assert "last_login" in profile
        # Verify created_at is valid ISO format, last_login is None initially
        datetime.fromisoformat(profile["created_at"])
        assert profile["last_login"] is None


class TestUserAuthentication:
    """Tests for user authentication."""

    def test_authenticate_success(self, user_manager):
        """Test successful user authentication."""
        user_manager.create_user("testuser", "password123")
        result = user_manager.authenticate("testuser", "password123")
        
        assert result is True

    def test_authenticate_wrong_password(self, user_manager):
        """Test authentication fails with wrong password."""
        user_manager.create_user("testuser", "password123")
        result = user_manager.authenticate("testuser", "wrongpassword")
        
        assert result is False

    def test_authenticate_nonexistent_user(self, user_manager):
        """Test authentication fails for non-existent user."""
        result = user_manager.authenticate("nonexistent", "password123")
        
        assert result is False

    def test_authenticate_updates_last_login(self, user_manager):
        """Test that successful authentication updates last_login timestamp."""
        user_manager.create_user("testuser", "password123")
        profile_before = user_manager.get_user_profile("testuser")
        
        # Wait a moment to ensure timestamp difference
        import time
        time.sleep(0.1)
        
        user_manager.authenticate("testuser", "password123")
        profile_after = user_manager.get_user_profile("testuser")
        
        assert profile_after["last_login"] != profile_before["last_login"]


class TestProfileManagement:
    """Tests for user profile management."""

    def test_get_user_profile_success(self, user_manager):
        """Test retrieving an existing user profile."""
        user_manager.create_user("testuser", "password123", {"email": "test@example.com"})
        profile = user_manager.get_user_profile("testuser")
        
        assert profile is not None
        assert profile["username"] == "testuser"
        assert profile["email"] == "test@example.com"

    def test_get_nonexistent_profile(self, user_manager):
        """Test retrieving a non-existent profile returns None."""
        profile = user_manager.get_user_profile("nonexistent")
        
        assert profile is None

    def test_update_user_profile(self, user_manager):
        """Test updating user profile data."""
        user_manager.create_user("testuser", "password123")
        
        updates = {
            "email": "newemail@example.com",
            "preferred_name": "Tester"
        }
        result = user_manager.update_user_profile("testuser", updates)
        
        assert result is True
        profile = user_manager.get_user_profile("testuser")
        assert profile["email"] == "newemail@example.com"
        assert profile["preferred_name"] == "Tester"

    def test_update_nonexistent_profile(self, user_manager):
        """Test updating non-existent profile returns False."""
        result = user_manager.update_user_profile("nonexistent", {"email": "test@example.com"})
        
        assert result is False


class TestIntakeAssessment:
    """Tests for intake assessment storage."""

    def test_save_intake_assessment(self, user_manager):
        """Test saving intake assessment responses."""
        user_manager.create_user("testuser", "password123")
        
        responses = {
            "primary_concern": 0,
            "therapy_preference": 0,
            "goals": "Reduce stress"
        }
        
        result = user_manager.save_intake_assessment("testuser", responses, "sourdough")
        
        assert result is True
        profile = user_manager.get_user_profile("testuser")
        assert profile["intake_responses"] == responses
        assert profile["recommended_therapist"] == "sourdough"

    def test_save_intake_for_nonexistent_user(self, user_manager):
        """Test saving intake for non-existent user returns False."""
        result = user_manager.save_intake_assessment("nonexistent", {}, "sourdough")
        
        assert result is False


class TestSessionLogging:
    """Tests for session logging functionality."""

    def test_log_session_success(self, user_manager):
        """Test logging a therapy session."""
        user_manager.create_user("testuser", "password123")
        
        messages = [
            {"role": "user", "content": "I'm feeling anxious"},
            {"role": "assistant", "content": "I hear you. Let's explore that."}
        ]
        
        session_id = user_manager.log_session("testuser", "sourdough", messages)
        
        assert session_id is not None
        # Session ID is timestamp format YYYYMMDD_HHMMSS
        assert len(session_id) == 15  # 8 digits + underscore + 6 digits

    def test_log_session_creates_user_directory(self, user_manager, temp_user_data_dir):
        """Test that logging a session creates user-specific session directory."""
        user_manager.create_user("testuser", "password123")
        user_manager.log_session("testuser", "sourdough", [])
        
        user_session_dir = Path(temp_user_data_dir, "sessions", "testuser")
        assert user_session_dir.exists()

    def test_log_session_for_nonexistent_user(self, user_manager):
        """Test logging session for non-existent user still creates session file."""
        session_id = user_manager.log_session("nonexistent", "sourdough", [])
        
        # Session file is created even if profile update fails
        assert session_id is not None

    def test_log_session_increments_count(self, user_manager):
        """Test that logging sessions increments total_sessions count."""
        user_manager.create_user("testuser", "password123")
        
        user_manager.log_session("testuser", "sourdough", [{"role": "user", "content": "Test"}])
        user_manager.log_session("testuser", "sourdough", [{"role": "user", "content": "Test 2"}])
        
        profile = user_manager.get_user_profile("testuser")
        assert profile["total_sessions"] == 2


class TestSessionHistory:
    """Tests for retrieving session history."""

    def test_get_session_history_empty(self, user_manager):
        """Test getting session history for user with no sessions."""
        user_manager.create_user("testuser", "password123")
        history = user_manager.get_session_history("testuser")
        
        assert history == []

    def test_get_session_history_with_sessions(self, user_manager):
        """Test getting session history returns saved sessions."""
        user_manager.create_user("testuser", "password123")
        
        messages1 = [{"role": "user", "content": "Session 1"}]
        messages2 = [{"role": "user", "content": "Session 2"}]
        
        import time
        user_manager.log_session("testuser", "sourdough", messages1)
        time.sleep(1)  # Ensure different timestamp
        user_manager.log_session("testuser", "brioche", messages2)
        
        history = user_manager.get_session_history("testuser")
        
        assert len(history) == 2
        assert history[0]["therapist"] == "sourdough"
        assert history[1]["therapist"] == "brioche"

    def test_get_session_history_limit(self, user_manager):
        """Test that get_session_history returns all sessions (no limit parameter)."""
        user_manager.create_user("testuser", "password123")
        
        import time
        for i in range(3):
            user_manager.log_session("testuser", "sourdough", [{"role": "user", "content": f"Test {i}"}])
            if i < 2:
                time.sleep(1)  # Ensure different timestamps
        
        history = user_manager.get_session_history("testuser")
        
        assert len(history) == 3

    def test_get_session_history_nonexistent_user(self, user_manager):
        """Test getting history for non-existent user returns empty list."""
        history = user_manager.get_session_history("nonexistent")
        
        assert history == []


class TestProgressNotes:
    """Tests for progress notes functionality."""

    def test_add_progress_note(self, user_manager):
        """Test adding a progress note."""
        user_manager.create_user("testuser", "password123")
        
        result = user_manager.add_progress_note("testuser", "Client shows improvement", "sourdough")
        
        assert result is True
        profile = user_manager.get_user_profile("testuser")
        assert len(profile["progress_notes"]) == 1
        assert profile["progress_notes"][0]["note"] == "Client shows improvement"
        assert profile["progress_notes"][0]["therapist"] == "sourdough"

    def test_add_multiple_progress_notes(self, user_manager):
        """Test adding multiple progress notes."""
        user_manager.create_user("testuser", "password123")
        
        user_manager.add_progress_note("testuser", "First note", "sourdough")
        user_manager.add_progress_note("testuser", "Second note", "sourdough")
        
        profile = user_manager.get_user_profile("testuser")
        assert len(profile["progress_notes"]) == 2

    def test_add_progress_note_has_timestamp(self, user_manager):
        """Test that progress notes include timestamp."""
        user_manager.create_user("testuser", "password123")
        user_manager.add_progress_note("testuser", "Test note", "sourdough")
        
        profile = user_manager.get_user_profile("testuser")
        note = profile["progress_notes"][0]
        
        assert "date" in note
        datetime.fromisoformat(note["date"])  # Verify valid timestamp

    def test_add_progress_note_nonexistent_user(self, user_manager):
        """Test adding note for non-existent user returns False."""
        result = user_manager.add_progress_note("nonexistent", "Test", "sourdough")
        
        assert result is False


class TestTherapyGoals:
    """Tests for therapy goals management."""

    def test_set_therapy_goals(self, user_manager):
        """Test setting therapy goals."""
        user_manager.create_user("testuser", "password123")
        
        goals = ["Reduce anxiety", "Improve sleep", "Build confidence"]
        result = user_manager.set_therapy_goals("testuser", goals)
        
        assert result is True
        profile = user_manager.get_user_profile("testuser")
        assert profile["therapy_goals"] == goals

    def test_set_therapy_goals_replaces_existing(self, user_manager):
        """Test that setting goals replaces existing goals."""
        user_manager.create_user("testuser", "password123")
        
        user_manager.set_therapy_goals("testuser", ["Goal 1"])
        user_manager.set_therapy_goals("testuser", ["Goal 2", "Goal 3"])
        
        profile = user_manager.get_user_profile("testuser")
        assert profile["therapy_goals"] == ["Goal 2", "Goal 3"]

    def test_set_therapy_goals_nonexistent_user(self, user_manager):
        """Test setting goals for non-existent user returns False."""
        result = user_manager.set_therapy_goals("nonexistent", ["Goal"])
        
        assert result is False
