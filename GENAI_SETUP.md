# GenAI System Engineering Setup Guide

This document provides a comprehensive guide to setting up and using the GenAI System Engineering capabilities in the Mergington High School project.

## Overview

The GenAI System Engineering module provides AI-powered assistance for various system engineering tasks:

- **Requirements Analysis**: Analyze system requirements for clarity, completeness, and testability
- **Design Generation**: Generate system designs based on specifications
- **Risk Assessment**: Identify and assess potential risks in system designs
- **Test Case Generation**: Generate comprehensive test cases from requirements
- **System Optimization**: Get AI-powered optimization suggestions

## Prerequisites

### 1. Python Environment

Ensure you have Python 3.8 or higher installed:

```bash
python --version
# Should output: Python 3.8.x or higher
```

### 2. Install Dependencies

#### Basic Installation (Core features only)

```bash
pip install -r requirements.txt
```

#### Development Installation (with testing and code quality tools)

```bash
pip install -r requirements-dev.txt
```

#### Minimal Installation (without heavy ML libraries)

If you want to use GenAI features without installing large ML libraries like transformers and torch, the basic installation already includes OpenAI and LangChain.

### 3. API Key Configuration

To use GenAI features, you need an OpenAI API key:

1. Sign up at [OpenAI Platform](https://platform.openai.com/)
2. Generate an API key from your account settings
3. Create a `.env` file in the project root:

```bash
cp .env.example .env
```

4. Edit `.env` and add your API key:

```env
OPENAI_API_KEY=sk-your-actual-api-key-here
OPENAI_MODEL=gpt-4  # or gpt-3.5-turbo for lower costs
OPENAI_TEMPERATURE=0.7
```

## Configuration Options

### Environment Variables

Configure the following in your `.env` file:

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Required |
| `OPENAI_MODEL` | Model to use (gpt-4, gpt-3.5-turbo) | gpt-4 |
| `OPENAI_TEMPERATURE` | Response creativity (0.0-1.0) | 0.7 |
| `GENAI_MAX_TOKENS` | Maximum tokens per response | 2000 |
| `GENAI_TIMEOUT` | Request timeout in seconds | 30 |

### Python Project Configuration

The project uses `pyproject.toml` for modern Python configuration:

```toml
[project]
name = "mergington-high-school-genai"
requires-python = ">=3.8"
```

## Running the Application

### Start the API Server

```bash
# From the project root
uvicorn src.app:app --reload --port 8000
```

The API will be available at:
- Main API: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Alternative Docs: http://localhost:8000/redoc

### Verify GenAI Status

Check if GenAI is properly configured:

```bash
curl http://localhost:8000/genai/status
```

Expected response if configured correctly:
```json
{
  "enabled": true,
  "message": "GenAI System Engineering is ready",
  "model": "gpt-4"
}
```

## Using GenAI Features

### 1. Requirements Analysis

Analyze system requirements for quality and completeness:

```bash
curl -X POST http://localhost:8000/genai/analyze-requirements \
  -H "Content-Type: application/json" \
  -d '{
    "requirements_text": "The system shall respond to user queries within 2 seconds and support up to 1000 concurrent users."
  }'
```

**Python Example:**

```python
import requests

response = requests.post(
    "http://localhost:8000/genai/analyze-requirements",
    json={
        "requirements_text": """
        The system shall:
        1. Process user authentication within 1 second
        2. Support 10,000 concurrent users
        3. Maintain 99.9% uptime
        4. Store data securely with encryption
        """
    }
)

result = response.json()
print(result['analysis'])
```

### 2. Design Generation

Generate system designs from specifications:

```bash
curl -X POST http://localhost:8000/genai/generate-design \
  -H "Content-Type: application/json" \
  -d '{
    "specifications": "A web-based student management system with course enrollment, grade tracking, and parent communication features.",
    "design_type": "architecture"
  }'
```

**Python Example:**

```python
import requests

response = requests.post(
    "http://localhost:8000/genai/generate-design",
    json={
        "specifications": "A microservices-based e-commerce platform",
        "design_type": "architecture"
    }
)

design = response.json()
print(design['design'])
```

### 3. Risk Assessment

Assess potential risks in your system:

```bash
curl -X POST http://localhost:8000/genai/assess-risks \
  -H "Content-Type: application/json" \
  -d '{
    "system_description": "A cloud-based microservices architecture using AWS, with multiple services communicating via REST APIs."
  }'
```

### 4. Test Case Generation

Generate test cases from requirements:

```bash
curl -X POST http://localhost:8000/genai/generate-test-cases \
  -H "Content-Type: application/json" \
  -d '{
    "requirements": "User login with email and password, including password reset functionality.",
    "test_type": "functional"
  }'
```

### 5. System Optimization

Get optimization suggestions:

```bash
curl -X POST http://localhost:8000/genai/optimize-system \
  -H "Content-Type: application/json" \
  -d '{
    "system_config": {
      "database": "PostgreSQL",
      "cache": "None",
      "workers": 4,
      "load_balancer": "nginx"
    },
    "optimization_goal": "performance"
  }'
```

## Direct Python Usage

You can also use the GenAI module directly in Python:

```python
from src.genai_system_engineering import create_genai_engineer

# Initialize the engineer
engineer = create_genai_engineer()

# Check if it's enabled
if engineer.is_enabled():
    # Analyze requirements
    result = engineer.analyze_requirements("""
        The system must support 1000 concurrent users
        and respond within 2 seconds.
    """)
    print(result)
    
    # Generate design
    design = engineer.generate_design(
        "A real-time chat application",
        design_type="architecture"
    )
    print(design)
    
    # Assess risks
    risks = engineer.assess_risks(
        "A public-facing web application with user data"
    )
    print(risks)
```

## Development Workflow

### Code Quality Tools

The project is configured with modern Python development tools:

#### Black (Code Formatting)

```bash
# Format all Python files
black src/

# Check formatting without changes
black --check src/
```

#### Ruff (Linting)

```bash
# Lint the codebase
ruff check src/

# Auto-fix issues
ruff check --fix src/
```

#### MyPy (Type Checking)

```bash
# Type check the code
mypy src/
```

#### Pytest (Testing)

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html
```

### Pre-commit Hooks

Install pre-commit hooks to automatically check code before committing:

```bash
pip install pre-commit
pre-commit install
```

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black
  
  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.1.13
    hooks:
      - id: ruff
        args: [--fix]
```

## Troubleshooting

### Issue: "GenAI is not configured"

**Solution**: Ensure you have set the `OPENAI_API_KEY` in your `.env` file:

```bash
# Check if .env exists
ls -la .env

# Verify the key is set
grep OPENAI_API_KEY .env
```

### Issue: "Module 'openai' not found"

**Solution**: Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Issue: API calls are slow

**Solutions**:
1. Use `gpt-3.5-turbo` instead of `gpt-4` for faster responses
2. Reduce `GENAI_MAX_TOKENS` in `.env`
3. Increase `OPENAI_TEMPERATURE` for less careful (but faster) responses

### Issue: Rate limit errors

**Solution**: OpenAI has rate limits. Consider:
1. Adding retry logic with exponential backoff
2. Caching responses for common queries
3. Upgrading your OpenAI plan

## Best Practices

### 1. Security

- **Never commit `.env` file** - It's in `.gitignore` by default
- **Use environment variables** for all sensitive data
- **Rotate API keys regularly**
- **Set spending limits** in your OpenAI account

### 2. Cost Management

- Use `gpt-3.5-turbo` for development and testing
- Set appropriate `max_tokens` limits
- Cache responses when possible
- Monitor usage in OpenAI dashboard

### 3. Performance

- Use async operations for multiple AI calls
- Implement request timeouts
- Add proper error handling
- Consider response streaming for long outputs

### 4. Code Quality

- Follow the configured Black formatting style
- Fix all Ruff linting warnings
- Add type hints for better code clarity
- Write tests for custom functionality

## VS Code Integration

### Recommended Extensions

The project is configured for optimal VS Code experience:

- **GitHub Copilot**: AI-powered code completion
- **Python**: Python language support
- **Pylance**: Fast Python language server
- **Black Formatter**: Auto-formatting on save
- **Ruff**: Real-time linting

### Settings

Add to `.vscode/settings.json`:

```json
{
  "python.linting.enabled": true,
  "python.linting.ruffEnabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "python.testing.pytestEnabled": true
}
```

## Example Use Cases

### System Engineering Workflow

1. **Requirements Phase**:
   - Use `analyze_requirements()` to validate requirements
   - Iterate based on feedback

2. **Design Phase**:
   - Use `generate_design()` for architecture proposals
   - Use `assess_risks()` to identify design issues

3. **Implementation Phase**:
   - Use `optimize_system()` for performance tuning
   - Generate configuration recommendations

4. **Testing Phase**:
   - Use `generate_test_cases()` for comprehensive test coverage
   - Generate both positive and negative test scenarios

### Educational Projects

Perfect for learning:
- System design principles
- Requirements engineering
- Risk management
- Test-driven development

## Additional Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Black Code Style](https://black.readthedocs.io/)
- [Ruff Linter](https://beta.ruff.rs/docs/)

## Support

For issues or questions:
1. Check the API documentation at `/docs`
2. Review error messages in the API responses
3. Check OpenAI service status
4. Review the example code in this guide

## License

MIT License - See LICENSE file for details
