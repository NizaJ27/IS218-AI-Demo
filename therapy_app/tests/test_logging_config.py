"""
Unit tests for logging configuration.

Tests logging setup, formatters, handlers, decorators, and context managers.
"""

import pytest
import logging
import json
import tempfile
import shutil
from pathlib import Path
from datetime import datetime

from src.logging_config import (
    JSONFormatter,
    setup_logging,
    get_logger,
    log_performance,
    LogContext
)


class TestJSONFormatter:
    """Tests for JSONFormatter."""

    def test_json_formatter_basic_log(self):
        """Test that JSONFormatter produces valid JSON."""
        formatter = JSONFormatter()
        
        # Create a log record
        record = logging.LogRecord(
            name="test_logger",
            level=logging.INFO,
            pathname="test.py",
            lineno=10,
            msg="Test message",
            args=(),
            exc_info=None
        )
        record.funcName = "test_func"
        record.module = "test_module"
        
        result = formatter.format(record)
        
        # Should be valid JSON
        log_data = json.loads(result)
        
        assert "timestamp" in log_data
        assert log_data["level"] == "INFO"
        assert log_data["message"] == "Test message"
        assert log_data["logger"] == "test_logger"
        assert log_data["module"] == "test_module"
        assert log_data["function"] == "test_func"
        assert log_data["line"] == 10

    def test_json_formatter_with_exception(self):
        """Test JSONFormatter includes exception info."""
        formatter = JSONFormatter()
        
        try:
            raise ValueError("Test error")
        except ValueError:
            import sys
            exc_info = sys.exc_info()
            
            record = logging.LogRecord(
                name="test",
                level=logging.ERROR,
                pathname="test.py",
                lineno=20,
                msg="Error occurred",
                args=(),
                exc_info=exc_info
            )
            record.funcName = "test"
            record.module = "test"
            
            result = formatter.format(record)
            log_data = json.loads(result)
            
            assert "exception" in log_data
            assert "ValueError" in log_data["exception"]
            assert "Test error" in log_data["exception"]

    def test_json_formatter_with_extra_fields(self):
        """Test JSONFormatter includes custom fields."""
        formatter = JSONFormatter()
        
        record = logging.LogRecord(
            name="test",
            level=logging.INFO,
            pathname="test.py",
            lineno=30,
            msg="User action",
            args=(),
            exc_info=None
        )
        record.funcName = "test"
        record.module = "test"
        
        # Add custom fields
        record.user_id = "user123"
        record.request_id = "req456"
        record.duration_ms = 250.5
        
        result = formatter.format(record)
        log_data = json.loads(result)
        
        assert log_data["user_id"] == "user123"
        assert log_data["request_id"] == "req456"
        assert log_data["duration_ms"] == 250.5


class TestSetupLogging:
    """Tests for setup_logging function."""

    def test_setup_logging_basic(self):
        """Test basic logging setup."""
        with tempfile.TemporaryDirectory() as tmpdir:
            logger = setup_logging(
                log_level="INFO",
                log_dir=tmpdir,
                enable_console=True,
                enable_file=True
            )
            
            assert logger is not None
            assert logger.name == "websearch"
            assert logger.level == logging.INFO

    def test_setup_logging_creates_log_directory(self):
        """Test that setup_logging creates log directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_dir = Path(tmpdir) / "logs"
            
            setup_logging(
                log_dir=str(log_dir),
                enable_file=True
            )
            
            assert log_dir.exists()

    def test_setup_logging_with_json_format(self):
        """Test logging setup with JSON formatting."""
        with tempfile.TemporaryDirectory() as tmpdir:
            logger = setup_logging(
                log_level="DEBUG",
                log_dir=tmpdir,
                json_format=True
            )
            
            # Log a message
            logger.info("Test message")
            
            # Check log file
            log_file = Path(tmpdir) / "app.log"
            assert log_file.exists()
            
            # Read and verify JSON format
            with open(log_file) as f:
                content = f.read()
                # Should contain JSON with message
                assert "Test message" in content

    def test_setup_logging_different_levels(self):
        """Test setup with different log levels."""
        with tempfile.TemporaryDirectory() as tmpdir:
            logger_debug = setup_logging(
                log_level="DEBUG",
                log_dir=tmpdir
            )
            assert logger_debug.level == logging.DEBUG
            
            logger_info = setup_logging(
                log_level="INFO",
                log_dir=tmpdir
            )
            assert logger_info.level == logging.INFO
            
            logger_warning = setup_logging(
                log_level="WARNING",
                log_dir=tmpdir
            )
            assert logger_warning.level == logging.WARNING

    def test_setup_logging_console_only(self):
        """Test logging with console handler only."""
        logger = setup_logging(
            log_level="INFO",
            enable_console=True,
            enable_file=False
        )
        
        assert logger is not None
        # Should have console handler
        assert len(logger.handlers) > 0

    def test_setup_logging_file_only(self):
        """Test logging with file handler only."""
        with tempfile.TemporaryDirectory() as tmpdir:
            logger = setup_logging(
                log_level="INFO",
                log_dir=tmpdir,
                enable_console=False,
                enable_file=True
            )
            
            assert logger is not None
            # Should have file handlers
            assert len(logger.handlers) > 0

    def test_setup_logging_creates_error_log(self):
        """Test that error.log file is created."""
        with tempfile.TemporaryDirectory() as tmpdir:
            logger = setup_logging(
                log_level="DEBUG",
                log_dir=tmpdir,
                enable_file=True
            )
            
            # Log an error
            logger.error("Test error")
            
            # Check both log files exist
            app_log = Path(tmpdir) / "app.log"
            error_log = Path(tmpdir) / "error.log"
            
            assert app_log.exists()
            assert error_log.exists()
            
            # Error should be in error.log
            with open(error_log) as f:
                content = f.read()
                assert "Test error" in content


class TestGetLogger:
    """Tests for get_logger function."""

    def test_get_logger_returns_logger(self):
        """Test that get_logger returns a logger instance."""
        logger = get_logger("test_module")
        
        assert logger is not None
        assert isinstance(logger, logging.Logger)
        assert "websearch.test_module" in logger.name

    def test_get_logger_different_names(self):
        """Test getting loggers with different names."""
        logger1 = get_logger("module1")
        logger2 = get_logger("module2")
        
        assert logger1.name != logger2.name
        assert "module1" in logger1.name
        assert "module2" in logger2.name


class TestLogPerformance:
    """Tests for log_performance decorator."""

    def test_log_performance_decorator_success(self):
        """Test performance logging decorator on successful function."""
        with tempfile.TemporaryDirectory() as tmpdir:
            logger = setup_logging(log_dir=tmpdir, enable_console=False)
            
            @log_performance(logger)
            def test_function():
                return "success"
            
            result = test_function()
            
            assert result == "success"
            
            # Check log file contains performance info
            log_file = Path(tmpdir) / "app.log"
            with open(log_file) as f:
                content = f.read()
                assert "test_function completed successfully" in content

    def test_log_performance_decorator_with_exception(self):
        """Test performance logging decorator when function raises exception."""
        with tempfile.TemporaryDirectory() as tmpdir:
            logger = setup_logging(log_dir=tmpdir, enable_console=False)
            
            @log_performance(logger)
            def failing_function():
                raise ValueError("Test error")
            
            with pytest.raises(ValueError):
                failing_function()
            
            # Check error log contains failure info
            error_log = Path(tmpdir) / "error.log"
            with open(error_log) as f:
                content = f.read()
                assert "failing_function failed" in content
                assert "Test error" in content

    def test_log_performance_measures_time(self):
        """Test that decorator measures execution time."""
        with tempfile.TemporaryDirectory() as tmpdir:
            logger = setup_logging(log_dir=tmpdir, enable_console=False, json_format=True)
            
            @log_performance(logger)
            def slow_function():
                import time
                time.sleep(0.01)  # 10ms
                return "done"
            
            result = slow_function()
            
            assert result == "done"
            
            # Check log contains duration
            log_file = Path(tmpdir) / "app.log"
            with open(log_file) as f:
                content = f.read()
                assert "duration_ms" in content


class TestLogContext:
    """Tests for LogContext context manager."""

    def test_log_context_success(self):
        """Test LogContext with successful operation."""
        with tempfile.TemporaryDirectory() as tmpdir:
            logger = setup_logging(log_dir=tmpdir, enable_console=False)
            
            with LogContext(logger, "Test operation"):
                pass
            
            # Check log file
            log_file = Path(tmpdir) / "app.log"
            with open(log_file) as f:
                content = f.read()
                assert "Starting: Test operation" in content
                assert "Completed: Test operation" in content

    def test_log_context_with_exception(self):
        """Test LogContext when exception occurs."""
        with tempfile.TemporaryDirectory() as tmpdir:
            logger = setup_logging(log_dir=tmpdir, enable_console=False)
            
            try:
                with LogContext(logger, "Failing operation"):
                    raise RuntimeError("Test error")
            except RuntimeError:
                pass
            
            # Check error log
            error_log = Path(tmpdir) / "error.log"
            with open(error_log) as f:
                content = f.read()
                assert "Failed: Failing operation" in content
                assert "Test error" in content

    def test_log_context_with_extra_context(self):
        """Test LogContext with additional context fields."""
        with tempfile.TemporaryDirectory() as tmpdir:
            logger = setup_logging(log_dir=tmpdir, enable_console=False, json_format=True)
            
            with LogContext(logger, "User request", user_id="user123", request_id="req456"):
                pass
            
            # Check log contains extra context
            log_file = Path(tmpdir) / "app.log"
            with open(log_file) as f:
                content = f.read()
                # In JSON format, should see the context fields
                assert "User request" in content

    def test_log_context_measures_duration(self):
        """Test that LogContext measures operation duration."""
        with tempfile.TemporaryDirectory() as tmpdir:
            logger = setup_logging(log_dir=tmpdir, enable_console=False, json_format=True)
            
            with LogContext(logger, "Timed operation"):
                import time
                time.sleep(0.01)
            
            # Check log contains duration
            log_file = Path(tmpdir) / "app.log"
            with open(log_file) as f:
                content = f.read()
                assert "duration_ms" in content

    def test_log_context_does_not_suppress_exceptions(self):
        """Test that LogContext doesn't suppress exceptions."""
        with tempfile.TemporaryDirectory() as tmpdir:
            logger = setup_logging(log_dir=tmpdir, enable_console=False)
            
            with pytest.raises(ValueError):
                with LogContext(logger, "Test"):
                    raise ValueError("Should propagate")


class TestLoggingIntegration:
    """Integration tests for logging functionality."""

    def test_complete_logging_workflow(self):
        """Test complete logging workflow with all components."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Setup logging
            main_logger = setup_logging(
                log_level="DEBUG",
                log_dir=tmpdir,
                enable_console=False,
                enable_file=True,
                json_format=True
            )
            
            # Get module logger
            module_logger = get_logger("my_module")
            
            # Use context manager
            with LogContext(module_logger, "Processing request", request_id="123"):
                module_logger.info("Step 1 complete")
                
                # Use decorator
                @log_performance(module_logger)
                def process_data():
                    return "result"
                
                result = process_data()
            
            # Verify log files exist
            app_log = Path(tmpdir) / "app.log"
            assert app_log.exists()
            
            # Verify content
            with open(app_log) as f:
                content = f.read()
                assert "Processing request" in content
                assert "Step 1 complete" in content
                assert "process_data completed successfully" in content
