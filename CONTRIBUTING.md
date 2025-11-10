# Contributing to ByteChan

Thank you for your interest in contributing to ByteChan! This document provides guidelines for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help create a welcoming environment for all contributors

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported
2. Create a detailed issue with:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - System information (OS, Python version, etc.)

### Suggesting Features

1. Open an issue describing the feature
2. Explain the use case and benefits
3. Discuss implementation approach

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Write/update tests
5. Ensure tests pass (`pytest tests/`)
6. Commit with clear messages
7. Push to your fork
8. Open a Pull Request

## Development Setup

\`\`\`bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/bytechan.git
cd bytechan

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/ --cov=bytechan

# Run linters
black bytechan/
flake8 bytechan/
\`\`\`

## Coding Standards

- Follow PEP 8 style guide
- Use type hints
- Write docstrings for all functions/classes
- Keep functions focused and small
- Write comprehensive tests
- Comment complex cryptographic operations

## Testing

- Write unit tests for new features
- Maintain >80% code coverage
- Test edge cases and error handling
- Include integration tests for major features

## Commit Messages

Use clear, descriptive commit messages:

\`\`\`
Add ring signature verification
Fix stealth address generation bug
Update documentation for bulletproofs
\`\`\`

## Review Process

1. Maintainers will review your PR
2. Address any feedback
3. Once approved, your PR will be merged

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
