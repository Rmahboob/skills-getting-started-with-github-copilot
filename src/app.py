"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.

Extended with GenAI System Engineering capabilities.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import Optional, Dict, Any
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import GenAI module (gracefully handle if dependencies are missing)
try:
    from src.genai_system_engineering import create_genai_engineer
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False

app = FastAPI(
    title="Mergington High School API",
    description="API for viewing and signing up for extracurricular activities. "
                "Extended with GenAI System Engineering capabilities.",
    version="1.0.0"
)

# Initialize GenAI engineer if available
if GENAI_AVAILABLE:
    genai_engineer = create_genai_engineer()
else:
    genai_engineer = None

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}


# ============================================================================
# GenAI System Engineering Endpoints
# ============================================================================

class RequirementsAnalysisRequest(BaseModel):
    """Request model for requirements analysis"""
    requirements_text: str


class DesignGenerationRequest(BaseModel):
    """Request model for design generation"""
    specifications: str
    design_type: Optional[str] = "architecture"


class RiskAssessmentRequest(BaseModel):
    """Request model for risk assessment"""
    system_description: str


class TestCaseGenerationRequest(BaseModel):
    """Request model for test case generation"""
    requirements: str
    test_type: Optional[str] = "functional"


class OptimizationRequest(BaseModel):
    """Request model for system optimization"""
    system_config: Dict[str, Any]
    optimization_goal: Optional[str] = "performance"


@app.get("/genai/status")
def genai_status():
    """Check if GenAI capabilities are enabled"""
    if not GENAI_AVAILABLE:
        return {
            "enabled": False,
            "message": "GenAI module is not available. Install required dependencies."
        }
    
    if genai_engineer and genai_engineer.is_enabled():
        return {
            "enabled": True,
            "message": "GenAI System Engineering is ready",
            "model": genai_engineer.model
        }
    else:
        return {
            "enabled": False,
            "message": "GenAI is not configured. Please set OPENAI_API_KEY environment variable."
        }


@app.post("/genai/analyze-requirements")
def analyze_requirements(request: RequirementsAnalysisRequest):
    """
    Analyze system requirements using GenAI
    
    Example request:
    ```json
    {
        "requirements_text": "The system shall process user requests within 2 seconds..."
    }
    ```
    """
    if not GENAI_AVAILABLE or not genai_engineer:
        raise HTTPException(
            status_code=503,
            detail="GenAI functionality is not available"
        )
    
    result = genai_engineer.analyze_requirements(request.requirements_text)
    return result


@app.post("/genai/generate-design")
def generate_design(request: DesignGenerationRequest):
    """
    Generate system design based on specifications
    
    Example request:
    ```json
    {
        "specifications": "A web-based student management system...",
        "design_type": "architecture"
    }
    ```
    """
    if not GENAI_AVAILABLE or not genai_engineer:
        raise HTTPException(
            status_code=503,
            detail="GenAI functionality is not available"
        )
    
    result = genai_engineer.generate_design(
        request.specifications,
        request.design_type
    )
    return result


@app.post("/genai/assess-risks")
def assess_risks(request: RiskAssessmentRequest):
    """
    Assess potential risks in a system design
    
    Example request:
    ```json
    {
        "system_description": "A cloud-based microservices architecture..."
    }
    ```
    """
    if not GENAI_AVAILABLE or not genai_engineer:
        raise HTTPException(
            status_code=503,
            detail="GenAI functionality is not available"
        )
    
    result = genai_engineer.assess_risks(request.system_description)
    return result


@app.post("/genai/generate-test-cases")
def generate_test_cases(request: TestCaseGenerationRequest):
    """
    Generate test cases based on requirements
    
    Example request:
    ```json
    {
        "requirements": "User login functionality with email and password...",
        "test_type": "functional"
    }
    ```
    """
    if not GENAI_AVAILABLE or not genai_engineer:
        raise HTTPException(
            status_code=503,
            detail="GenAI functionality is not available"
        )
    
    result = genai_engineer.generate_test_cases(
        request.requirements,
        request.test_type
    )
    return result


@app.post("/genai/optimize-system")
def optimize_system(request: OptimizationRequest):
    """
    Suggest optimizations for a system configuration
    
    Example request:
    ```json
    {
        "system_config": {
            "database": "MySQL",
            "cache": "None",
            "workers": 4
        },
        "optimization_goal": "performance"
    }
    ```
    """
    if not GENAI_AVAILABLE or not genai_engineer:
        raise HTTPException(
            status_code=503,
            detail="GenAI functionality is not available"
        )
    
    result = genai_engineer.optimize_system(
        request.system_config,
        request.optimization_goal
    )
    return result
