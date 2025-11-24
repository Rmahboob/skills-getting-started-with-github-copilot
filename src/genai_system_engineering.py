"""
System Engineering GenAI Module

This module provides AI-powered capabilities for system engineering tasks,
including requirements analysis, design generation, and system optimization.
"""

import os
from typing import Dict, List, Optional, Any
from enum import Enum
import json

# Optional imports - gracefully handle if not installed
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False


class SystemEngineeringTask(str, Enum):
    """Types of system engineering tasks"""
    REQUIREMENTS_ANALYSIS = "requirements_analysis"
    DESIGN_GENERATION = "design_generation"
    RISK_ASSESSMENT = "risk_assessment"
    OPTIMIZATION = "optimization"
    DOCUMENTATION = "documentation"
    TEST_CASE_GENERATION = "test_case_generation"


class GenAISystemEngineer:
    """
    AI-powered System Engineering Assistant
    
    This class provides methods to assist with various system engineering tasks
    using GenAI capabilities.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the GenAI System Engineer
        
        Args:
            api_key: OpenAI API key. If not provided, will try to read from env
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("OPENAI_MODEL", "gpt-4")
        self.temperature = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))
        
        if OPENAI_AVAILABLE and self.api_key:
            self.client = OpenAI(api_key=self.api_key)
            self.enabled = True
        else:
            self.client = None
            self.enabled = False
    
    def is_enabled(self) -> bool:
        """Check if GenAI is properly configured and enabled"""
        return self.enabled
    
    def analyze_requirements(self, requirements_text: str) -> Dict[str, Any]:
        """
        Analyze system requirements and provide insights
        
        Args:
            requirements_text: Text containing system requirements
            
        Returns:
            Dictionary containing analysis results
        """
        if not self.is_enabled():
            return {
                "status": "disabled",
                "message": "GenAI is not configured. Please set OPENAI_API_KEY."
            }
        
        prompt = f"""
        As a system engineering expert, analyze the following requirements:
        
        {requirements_text}
        
        Provide:
        1. Clarity assessment (are requirements clear and unambiguous?)
        2. Completeness check (are there any gaps?)
        3. Testability evaluation (can these be tested?)
        4. Potential conflicts or contradictions
        5. Suggestions for improvement
        
        Format your response as JSON with keys: clarity, completeness, testability, conflicts, suggestions
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a system engineering expert."},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature,
                max_tokens=int(os.getenv("GENAI_MAX_TOKENS", "2000"))
            )
            
            result = response.choices[0].message.content
            
            # Try to parse as JSON, fallback to text if not valid JSON
            try:
                parsed_result = json.loads(result)
                return {
                    "status": "success",
                    "analysis": parsed_result,
                    "raw_response": result
                }
            except json.JSONDecodeError:
                return {
                    "status": "success",
                    "analysis": result,
                    "raw_response": result
                }
                
        except Exception as e:
            return {
                "status": "error",
                "message": f"Error during analysis: {str(e)}"
            }
    
    def generate_design(self, specifications: str, design_type: str = "architecture") -> Dict[str, Any]:
        """
        Generate system design based on specifications
        
        Args:
            specifications: System specifications
            design_type: Type of design (architecture, database, api, etc.)
            
        Returns:
            Dictionary containing generated design
        """
        if not self.is_enabled():
            return {
                "status": "disabled",
                "message": "GenAI is not configured. Please set OPENAI_API_KEY."
            }
        
        prompt = f"""
        Based on the following specifications, generate a {design_type} design:
        
        {specifications}
        
        Provide:
        1. Overall design approach
        2. Key components and their responsibilities
        3. Interface definitions
        4. Data flow
        5. Technology recommendations
        
        Format as a detailed design document.
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert system designer."},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature,
                max_tokens=int(os.getenv("GENAI_MAX_TOKENS", "2000"))
            )
            
            return {
                "status": "success",
                "design": response.choices[0].message.content,
                "design_type": design_type
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": f"Error during design generation: {str(e)}"
            }
    
    def assess_risks(self, system_description: str) -> Dict[str, Any]:
        """
        Assess potential risks in a system design
        
        Args:
            system_description: Description of the system
            
        Returns:
            Dictionary containing risk assessment
        """
        if not self.is_enabled():
            return {
                "status": "disabled",
                "message": "GenAI is not configured. Please set OPENAI_API_KEY."
            }
        
        prompt = f"""
        Perform a risk assessment for the following system:
        
        {system_description}
        
        Identify:
        1. Technical risks
        2. Security risks
        3. Performance risks
        4. Operational risks
        5. Mitigation strategies for each risk
        
        Rate each risk as: Critical, High, Medium, or Low
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a risk assessment expert."},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature,
                max_tokens=int(os.getenv("GENAI_MAX_TOKENS", "2000"))
            )
            
            return {
                "status": "success",
                "assessment": response.choices[0].message.content
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": f"Error during risk assessment: {str(e)}"
            }
    
    def generate_test_cases(self, requirements: str, test_type: str = "functional") -> Dict[str, Any]:
        """
        Generate test cases based on requirements
        
        Args:
            requirements: System requirements
            test_type: Type of tests (functional, integration, performance, etc.)
            
        Returns:
            Dictionary containing generated test cases
        """
        if not self.is_enabled():
            return {
                "status": "disabled",
                "message": "GenAI is not configured. Please set OPENAI_API_KEY."
            }
        
        prompt = f"""
        Generate {test_type} test cases for the following requirements:
        
        {requirements}
        
        For each test case provide:
        1. Test ID
        2. Test description
        3. Preconditions
        4. Test steps
        5. Expected results
        6. Priority (High/Medium/Low)
        
        Format as a structured list.
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a test engineering expert."},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature,
                max_tokens=int(os.getenv("GENAI_MAX_TOKENS", "2000"))
            )
            
            return {
                "status": "success",
                "test_cases": response.choices[0].message.content,
                "test_type": test_type
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": f"Error during test case generation: {str(e)}"
            }
    
    def optimize_system(self, system_config: Dict[str, Any], 
                       optimization_goal: str = "performance") -> Dict[str, Any]:
        """
        Suggest optimizations for a system configuration
        
        Args:
            system_config: Current system configuration
            optimization_goal: Goal (performance, cost, reliability, etc.)
            
        Returns:
            Dictionary containing optimization suggestions
        """
        if not self.is_enabled():
            return {
                "status": "disabled",
                "message": "GenAI is not configured. Please set OPENAI_API_KEY."
            }
        
        config_str = json.dumps(system_config, indent=2)
        
        prompt = f"""
        Analyze this system configuration and suggest optimizations for {optimization_goal}:
        
        {config_str}
        
        Provide:
        1. Current bottlenecks or inefficiencies
        2. Specific optimization recommendations
        3. Expected impact of each recommendation
        4. Implementation complexity (Easy/Medium/Hard)
        5. Potential trade-offs
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a system optimization expert."},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature,
                max_tokens=int(os.getenv("GENAI_MAX_TOKENS", "2000"))
            )
            
            return {
                "status": "success",
                "optimizations": response.choices[0].message.content,
                "optimization_goal": optimization_goal
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": f"Error during optimization: {str(e)}"
            }


# Convenience function for quick access
def create_genai_engineer(api_key: Optional[str] = None) -> GenAISystemEngineer:
    """
    Factory function to create a GenAI System Engineer instance
    
    Args:
        api_key: Optional OpenAI API key
        
    Returns:
        GenAISystemEngineer instance
    """
    return GenAISystemEngineer(api_key=api_key)
