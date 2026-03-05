from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.database import get_all_patients


router = APIRouter()

# Configure Jinja2 to load HTML templates from the app/templates folder
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    
    # Fetch the data from DuckDB
    patients = get_all_patients()

    # Calculate the breaches (Patients that have been waiting more than 18 weeks)
    breaches = [p for p in patients if p['wait_weeks'] > 18]
    breach_count = len(breaches)

    # Calculate the cancer logic
    cancer_patients = [p for p in patients if p['priority'] == 'Two Week Wait (Cancer)']
    cancer_count = len(cancer_patients)

    # Calculate the percentage
    total_count = len(patients)
    breach_percent = (breach_count / total_count * 100) if total_count > 0 else 0

    # Average wait time calculations
    if patients:
        avg_wait = sum(p['wait_weeks'] for p in patients) / len(patients)
    else:
        avg_wait = 0
    
    # Convert dates to strings for charts.js/ JSON compatability
    json_compatible_patients = jsonable_encoder(patients)
    
    # Pass the encoded list to the templates
    return templates.TemplateResponse(
        request,
        "index.html",                              
        {
            "patients": json_compatible_patients,
            "breach_count": breach_count,
            "breach_percent": breach_percent,
            "cancer_count": cancer_count,
            "avg_wait": round(avg_wait, 1) # Round waiting times to make it clear.
        }
    )
