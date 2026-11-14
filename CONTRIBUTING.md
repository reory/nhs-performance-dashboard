# 🏥 Contributing to NHS Performance Dashboard

Thank you for your interest in contributing to the NHS Performance Dashboard.

This project demonstrates modern Python development practices using FastAPI, DuckDB, Pydantic, Jinja2, and Pytest. Whether you are fixing a bug, improving documentation, enhancing the dashboard, or adding new features, all contributions are welcome.

---

## 📋 Contents

- Development Setup
- Running the Application
- Running Tests
- Creating a Branch
- Pull Request Guidelines
- Clinical Logic
- Reporting Issues
- Feature Requests

---

## 🌿 Development Setup

Clone the repository:

```bash
git clone https://github.com/reory/nhs-performance-dashboard.git
cd nhs-performance-dashboard
```

Create a virtual environment:

```bash
uv venv
```

Activate the environment.

### Windows

```powershell
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install all dependencies:

```bash
uv sync --all-groups
```

---

## 🚀 Running the Application

Generate sample patient data:

```bash
uv run python scripts/generate_faker_data.py
```

Start the FastAPI application:

```bash
uv run uvicorn app.main:app --reload
```

Open your browser and navigate to:

```text
http://127.0.0.1:8000
```

---

## 🧪 Running Tests

Run the full test suite before committing changes:

```bash
uv run pytest
```

The test suite covers:

- NHS number validation
- RTT breach calculations
- Data generation
- FastAPI endpoints
- Export functionality

All tests should pass before submitting a Pull Request.

---

## 🌱 Creating a Branch

Use descriptive branch names that clearly explain the change:

```text
fix/dashboard-metric-bug
fix/nhs-validation
feature/search-enhancements
feature/new-dashboard-chart
docs/readme-improvements
```

Avoid working directly on the main branch.

---

## ✅ Pull Request Guidelines

Before opening a Pull Request:

- Ensure all tests pass.
- Keep changes focused on a single issue or feature.
- Update documentation where appropriate.
- Add or update tests for new functionality.
- Keep code, comments, and docstrings concise and readable.
- Remove unused imports, dead code, and debugging statements.

A good Pull Request should clearly explain:

- What changed
- Why it changed
- How it was tested

---

## 🏥 Clinical Logic

Please take extra care when modifying:

- RTT (Referral to Treatment) calculations
- Waiting-time metrics
- NHS number validation
- Patient data generation
- Dashboard KPI calculations

Changes affecting clinical logic should include corresponding tests to ensure behaviour remains predictable and reliable.

---

## 🐛 Reporting Issues

If you discover a bug, please include:

- A clear description of the issue
- Steps to reproduce the problem
- Expected behaviour
- Actual behaviour
- Error messages or screenshots where relevant
- Python version and operating system details

Providing as much information as possible helps reproduce and resolve issues more quickly.

## 💡 Feature Requests

Suggestions for improvements are always welcome.

When submitting a feature request, please include:

- The problem the feature solves
- Why the feature would be useful
- A brief description of the proposed solution
- Any alternative approaches that were considered

Please try to keep suggestions aligned with the project's goal of demonstrating healthcare analytics, FastAPI development, data engineering practices, and dashboard visualisation.

## 🧹 Code Style

This project aims to keep the codebase clean, readable, and beginner friendly.

General guidelines:

- Write clear and concise code
- Prefer descriptive variable and function names
- Keep functions focused on a single responsibility
- Include tests where appropriate
- Use type hints where helpful
- Keep comments and docstrings concise

## 🙏 Thank You

Thank you for taking the time to contribute.

Whether you improve documentation, fix a bug, add tests, or suggest a new feature, every contribution helps make the project better and provides valuable learning opportunities for the broader Python community.
