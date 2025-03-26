# Python Project Template

A Python project template with a complete development environment setup including type checking, testing, and code quality tools.

## Features

- **Type Checking**: Full mypy integration with strict type checking
- **Testing**: Pytest with coverage reporting
- **Code Quality**: Black formatting and Flake8 linting
- **Git Hooks**: Pre-commit hooks for consistent code quality
- **Docker Support**: Ready for containerization

## Getting Started

### Prerequisites

- Python 3.12 or higher
- [UV](https://github.com/astral-sh/uv) package manager

### Installation

1. Clone the repository:

```bash
git@github.com:rahulgurujala/python-template.git
cd python-template
```

2. Install dependencies:

```bash
uv pip install -e ".[dev]"
```

3. Install pre-commit hooks:

```bash
pre-commit install
```

## Development

### Project Structure

```
python-template/
├── src/                # Source code
│   ├── __init__.py
│   └── core.py         # Core functionality
├── tests/              # Test suite
│   ├── conftest.py     # Shared pytest fixtures
│   └── test_sample.py  # Sample tests
├── .flake8             # Flake8 configuration
├── .pre-commit-config.yaml  # Pre-commit hooks configuration
├── .vscode/            # VS Code settings
├── pyproject.toml      # Project configuration
└── Dockerfile          # Docker configuration
```

### Running Tests

Run the test suite with:

```bash
python -m pytest
```

For test coverage:

```bash
python -m pytest --cov=src
```

### Type Checking

Run mypy to check types:

```bash
mypy src tests
```

### Code Formatting and Linting

Format code with Black:

```bash
black src tests
```

Lint code with Flake8:

```bash
flake8 src tests
```

## Docker

### Building and running your application

When you're ready, start your application by running:

```bash
docker compose up --build
```

Your application will be available at http://localhost:8000.

### Deploying your application to the cloud

First, build your image:

```bash
docker build -t myapp .
```

If your cloud uses a different CPU architecture than your development machine (e.g., you are on a Mac M1 and your cloud provider is amd64), build the image for that platform:

```bash
docker build --platform=linux/amd64 -t myapp .
```

Then, push it to your registry:

```bash
docker push myregistry.com/myapp
```

## Project Configuration

### pyproject.toml

The project uses `pyproject.toml` for configuration with the following tools:

- **Black**: Code formatting with 88 character line length
- **Pytest**: Test configuration with coverage reporting
- **Mypy**: Strict type checking

### Pre-commit Hooks

The following pre-commit hooks are configured:

- Basic file checks (trailing whitespace, file endings)
- Black formatting
- Flake8 linting with docstring checking
- Mypy type checking

## License

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## References

- [Docker's Python guide](https://docs.docker.com/language/python/)
- [Mypy documentation](https://mypy.readthedocs.io/)
- [Pytest documentation](https://docs.pytest.org/)
- [Black documentation](https://black.readthedocs.io/)
- [Flake8 documentation](https://flake8.pycqa.org/)
