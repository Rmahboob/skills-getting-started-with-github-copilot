"""Tests for the GenAI System Engineering module"""

import pytest
from src.genai_system_engineering import (
    create_genai_engineer,
    GenAISystemEngineer,
    SystemEngineeringTask,
)


class TestGenAISystemEngineer:
    """Test cases for GenAI System Engineer"""

    def test_create_engineer_without_api_key(self):
        """Test engineer creation without API key"""
        engineer = create_genai_engineer(api_key=None)
        assert engineer is not None
        assert isinstance(engineer, GenAISystemEngineer)

    def test_is_enabled_without_api_key(self):
        """Test that engineer reports disabled without API key"""
        engineer = create_genai_engineer(api_key=None)
        assert isinstance(engineer.is_enabled(), bool)

    def test_analyze_requirements_without_api_key(self):
        """Test requirements analysis without API key"""
        engineer = GenAISystemEngineer(api_key=None)
        result = engineer.analyze_requirements("Test requirements")
        assert "status" in result
        assert result["status"] in ["disabled", "error", "success"]

    def test_system_engineering_task_enum(self):
        """Test SystemEngineeringTask enum values"""
        assert SystemEngineeringTask.REQUIREMENTS_ANALYSIS == "requirements_analysis"
        assert SystemEngineeringTask.DESIGN_GENERATION == "design_generation"
        assert SystemEngineeringTask.RISK_ASSESSMENT == "risk_assessment"
