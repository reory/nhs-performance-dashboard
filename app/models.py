from datetime import date

import nhs_number
from loguru import logger
from pydantic import BaseModel, validator


class Patient(BaseModel):
    """Represents a patient on a referral waiting list."""

    gp_practice: str
    nhs_id: str
    name: str
    dob: date
    specialty: str
    priority: str
    referral_date: date
    wait_weeks: int

    # This tells Pydantic how to use the NHS library.
    @validator("nhs_id")
    @classmethod
    def validate_nhs_id(cls, v):
        """
        Normalise the NHS number by stripping spaces and punctuation,
        ensuring it contains exactly 10 digits.
        """

        logger.debug(f"Validating nhs ID: {v}")

        # Normalise and remove spaces/hyphens
        clean_v = v.replace(" ", "").replace("-", "")

        if not nhs_number.is_valid(clean_v):
            raise ValueError(f"Invalid NHS Number: {v}")
        return clean_v
