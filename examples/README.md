# GenAI Examples

This directory contains example scripts demonstrating the GenAI System Engineering capabilities.

## Available Examples

### genai_demo.py

A comprehensive demo script showing all GenAI features:

```bash
# Run the demo
python examples/genai_demo.py
```

**Prerequisites:**
- Set up your `.env` file with `OPENAI_API_KEY`
- Install dependencies: `pip install -r requirements.txt`

## Creating Your Own Examples

You can create custom examples by importing the GenAI module:

```python
from src.genai_system_engineering import create_genai_engineer

# Initialize
engineer = create_genai_engineer()

# Use the features
if engineer.is_enabled():
    result = engineer.analyze_requirements("Your requirements here")
    print(result)
```

See `GENAI_SETUP.md` in the root directory for detailed documentation.
