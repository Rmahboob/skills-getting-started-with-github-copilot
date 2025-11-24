# Getting Started with GitHub Copilot

_Get started using GitHub Copilot in less than an hour._

## Welcome

- **Who is this for**: Developers at any experience level looking to accelerate their code workflow.
- **What you'll learn**: The different ways to interact with Copilot to explain, write, debug, and develop code.
- **What you'll build**: You will guide Copilot to update Mergington High School's extracurricular activities website.
- **Prerequisites**:
  - Skills exercise: [Introduction to GitHub](https://github.com/skills/introduction-to-github)
  - Familiarity with [VS Code](https://code.visualstudio.com/)
  - Basic coding principles
- **How long**: This exercise takes less than one hour to complete.

In this exercise, you will:

1. Use a preconfigured Codespace to run VS Code in your browser.
1. Learn different interaction options to develop with GitHub Copilot.
1. Use Copilot to summarize and review your pull request.

## 🚀 New: GenAI System Engineering Support

This repository now includes comprehensive Python configuration and GenAI capabilities for System Engineering use cases:

### Features

- **Requirements Analysis**: AI-powered analysis of system requirements for clarity, completeness, and testability
- **Design Generation**: Generate system architectures and designs from specifications
- **Risk Assessment**: Identify and evaluate potential system risks
- **Test Case Generation**: Automatically generate comprehensive test cases
- **System Optimization**: Get AI-powered suggestions for system performance improvements

### Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure GenAI** (Optional - for AI features):
   ```bash
   cp .env.example .env
   # Edit .env and add your OPENAI_API_KEY
   ```

3. **Run the Application**:
   ```bash
   uvicorn src.app:app --reload --port 8000
   ```

4. **Access the API**:
   - Main API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs
   - GenAI Status: http://localhost:8000/genai/status

### Documentation

- **[GENAI_SETUP.md](GENAI_SETUP.md)**: Comprehensive setup and usage guide
- **[examples/](examples/)**: Example scripts and demos
- **[src/genai_system_engineering.py](src/genai_system_engineering.py)**: GenAI module source

### Python Configuration

The project includes modern Python development setup:

- **pyproject.toml**: Modern Python project configuration
- **Code formatting**: Black (configured for 100 char line length)
- **Linting**: Ruff with comprehensive rules
- **Type checking**: MyPy support
- **Testing**: Pytest with coverage
- **VS Code**: Pre-configured settings for optimal Python development

### Example Usage

```python
from src.genai_system_engineering import create_genai_engineer

# Initialize the GenAI engineer
engineer = create_genai_engineer()

# Analyze requirements
result = engineer.analyze_requirements("""
    System Requirements:
    1. The system shall support 10,000 concurrent users
    2. Response time shall be under 2 seconds
""")
print(result)
```

See [GENAI_SETUP.md](GENAI_SETUP.md) for complete documentation and examples.

### How to start this exercise

Simply copy the exercise to your account, then give your favorite Octocat (Mona) **about 20 seconds** to prepare the first lesson, then **refresh the page**.

[![](https://img.shields.io/badge/Copy%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/new?template_owner=skills&template_name=getting-started-with-github-copilot&owner=%40me&name=skills-getting-started-with-github-copilot&description=Exercise:+Get+started+using+GitHub+Copilot&visibility=public)

<details>
<summary>Having trouble? 🤷</summary><br/>

When copying the exercise, we recommend the following settings:

- For owner, choose your personal account or an organization to host the repository.

- We recommend creating a public repository, since private repositories will use Actions minutes.
   
If the exercise isn't ready in 20 seconds, please check the [Actions](../../actions) tab.

- Check to see if a job is running. Sometimes it simply takes a bit longer.

- If the page shows a failed job, please submit an issue. Nice, you found a bug! 🐛

</details>

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)