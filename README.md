# Markov Chain Text Generator

A Python project for generating text using Markov chains. This project uses text files as input to build a statistical model for generating new text.

## Development Setup with DevContainer

This project is configured to use VS Code DevContainers for a consistent development environment.

### Prerequisites

- **VS Code** with the Remote - Containers extension installed
- **Docker Desktop** or Docker Engine

### Quick Start

1. **Open the project in VS Code**:
   ```bash
   code /path/to/markovsan
   ```

2. **Reopen in Container**:
   - VS Code will detect the `.devcontainer` folder
   - Click "Reopen in Container" when prompted
   - Wait for the container to build and start

3. **Verify the setup**:
   ```bash
   python --version
   uv --version
   ruff --version
   black --version
   flake8 --version
   ```

### Project Structure

```
markovsan/
├── .devcontainer/          # DevContainer configuration
│   ├── Dockerfile         # Container image definition
│   └── devcontainer.json  # VS Code settings
├── src/                    # Source code
│   └── markovsan/
│       └── __init__.py
├── tests/                  # Test files
├── pyproject.toml         # Project configuration
├── .gitignore            # Git ignore patterns
└── README.md            # This file
```

## Usage

### Installing Dependencies

```bash
uv sync
```

### Running Code

```bash
python -m markovsan
```

### Code Quality

The project uses three tools for code quality:

**Ruff** (linting):
```bash
ruff check src/
ruff check src/ --fix  # Auto-fix issues
```

**Black** (formatting):
```bash
black src/
```

**Flake8** (additional linting):
```bash
flake8 src/
```

All three tools are configured to run on save in VS Code.

### Running Tests

```bash
pytest
pytest --cov=src  # With coverage report
```

## Development without DevContainer

If you prefer to work without the container:

1. Create a virtual environment:
   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install UV:
   ```bash
   pip install uv
   ```

3. Sync dependencies:
   ```bash
   uv sync
   ```

4. Install dev tools:
   ```bash
   pip install ruff black flake8 pytest
   ```

## Notes

- Python 3.12+ is required
- All dependencies are managed by UV
- The DevContainer includes all necessary tools and extensions
- SSH keys are mounted for Git operations (optional)

## License

Add your license information here.
