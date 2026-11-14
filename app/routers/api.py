from fastapi import APIRouter
from loguru import logger

from app.database import get_all_patients

# Create a new API router to group related endpoints
router = APIRouter()


# Define a GET endpoint at api/patients
@router.get("/api/patients")
async def get_patients_json():
    """Return all patient records as JSON."""

    logger.debug("Patient records fetched.")
    # Return all patient records as JSON
    return get_all_patients()
