.PHONY: run test coverage clean install help

# Default target
.DEFAULT_GOAL := help

help: ## Show this help message
	@echo "Discord Ops Copilot - Available Commands"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

run: ## Run the Discord Ops Copilot Streamlit application
	@./run.sh

install: ## Install all required dependencies
	@echo "📦 Installing dependencies..."
	@pip install -r requirements.txt
	@echo "✅ Dependencies installed successfully!"

test: ## Run all tests
	@echo "🧪 Running tests..."
	@pytest

coverage: ## Run tests with coverage report
	@echo "📊 Running tests with coverage..."
	@pytest --cov=src --cov-report=term-missing --cov-report=html
	@echo "✅ Coverage report generated in htmlcov/"

clean: ## Clean up generated files and caches
	@echo "🧹 Cleaning up..."
	@rm -rf __pycache__ .pytest_cache htmlcov .coverage
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete
	@echo "✅ Cleanup complete!"

lint: ## Run linting checks
	@echo "🔍 Running linter..."
	@pytest --pylint

format: ## Format code (if you have a formatter installed)
	@echo "✨ Formatting code..."
	@black . 2>/dev/null || echo "Install black for code formatting: pip install black"

dev: ## Run in development mode with auto-reload
	@echo "🔧 Starting in development mode..."
	@streamlit run streamlit_app.py --server.runOnSave=true
