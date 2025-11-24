#!/usr/bin/env python3
"""
Example script demonstrating GenAI System Engineering capabilities
"""

import os
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.genai_system_engineering import create_genai_engineer


def main():
    """Main demo function"""
    print("\nGenAI System Engineering Demo")
    print("=" * 80)
    
    # Initialize the engineer
    engineer = create_genai_engineer()
    
    # Check if enabled
    if not engineer.is_enabled():
        print("\n⚠ WARNING: GenAI is not enabled!")
        print("\nTo use GenAI features:")
        print("1. Get an OpenAI API key from https://platform.openai.com/")
        print("2. Create a .env file with: OPENAI_API_KEY=your-key-here")
        print("3. Install dependencies: pip install -r requirements.txt")
        return
    
    print("\n✓ GenAI is enabled and ready!")
    print(f"Using model: {engineer.model}")
    
    # Demo requirements analysis
    print("\n--- Requirements Analysis Demo ---")
    result = engineer.analyze_requirements("""
    System Requirements:
    1. The system shall support 10,000 concurrent users
    2. Page load time should be fast
    3. Data must be backed up
    """)
    print(f"Status: {result['status']}")


if __name__ == "__main__":
    main()
