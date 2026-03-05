from pydantic import BaseModel, validator
from datetime import date
import nhs_number

class Patient(BaseModel):
    # Patients GP practice
    gp_practice: str
    # Unique NHS identifier
    nhs_id: str
    # Full patient name
    name: str
    # Date of birth
    dob: date
    # Clinical specialty the patient is referred to
    specialty: str
    # Priority category (eg, urgent)
    priority: str
    # Date the referral was made
    referral_date: date
    # Calculated number of weeks the patient has been waiting
    wait_weeks: int

    # This tells Pydantic how to use the NHS library.
    @validator('nhs_id')
    @classmethod
    def validate_nhs_id(cls, v):
        # Normalise and remove spaces/hyphens
        clean_v = v.replace(" ", "").replace("-", "")

        if not nhs_number.is_valid(clean_v):
            raise ValueError(f"Invalid NHS Number: {v}")
        return clean_v