# Mergington High School Activities API

A super simple FastAPI application that allows students to view and sign up for extracurricular activities.

## Features

- View all available extracurricular activities
- Sign up for activities

## Getting Started

### Setting Up a Virtual Environment (Recommended)

It's recommended to use a Python virtual environment to manage dependencies and avoid conflicts with system packages.

#### On Windows:

```bash
# Navigate to the project directory
cd /path/to/skills-getting-started-with-github-copilot

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate
```

#### On macOS/Linux:

```bash
# Navigate to the project directory
cd /path/to/skills-getting-started-with-github-copilot

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

#### Deactivating the Virtual Environment

When you're done working, you can deactivate the virtual environment:

```bash
deactivate
```

### Installing Dependencies

Once the virtual environment is activated, install the required dependencies:

```bash
# Install from requirements.txt
pip install -r requirements.txt

# Or install manually
pip install fastapi uvicorn
```

### Running the Application

1. Make sure your virtual environment is activated (you should see `(venv)` in your terminal prompt)

2. Run the application using uvicorn:

   ```bash
   uvicorn src.app:app --reload
   ```

   The `--reload` flag enables auto-reloading when you make code changes.

3. Open your browser and go to:
   - API documentation: http://localhost:8000/docs
   - Alternative documentation: http://localhost:8000/redoc

## API Endpoints

| Method | Endpoint                                                          | Description                                                         |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Get all activities with their details and current participant count |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Sign up for an activity                                             |

## Data Model

The application uses a simple data model with meaningful identifiers:

1. **Activities** - Uses activity name as identifier:

   - Description
   - Schedule
   - Maximum number of participants allowed
   - List of student emails who are signed up

2. **Students** - Uses email as identifier:
   - Name
   - Grade level

All data is stored in memory, which means data will be reset when the server restarts.
