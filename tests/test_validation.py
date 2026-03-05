import pytest
from pydantic import ValidationError
from app.models import Patient
from datetime import date
import nhs_number

def test_valid_nhs_number():
    """Test that a mathematically valid nhs number is accepted."""
    
    # Generate a valid NHS number using the library itself.
    # This is better than making up a number.
    valid_num = nhs_number.generate(quantity=1)[0]
    
    # Check the library first
    assert nhs_number.is_valid(valid_num) is True

    # Ensure the pydantic model accepts it.

    patient = Patient(
        nhs_id=valid_num,
        name="John Doe",
        gp_practice="The Valley Site",
        dob=date(1975, 4, 11),
        specialty="Cardiology",
        priority="Routine",
        referral_date=date(2024, 1, 1),
        wait_weeks=10
    )

    assert patient.nhs_id == valid_num

def test_valid_nhs_number_fails():
    """Test that a keyboard number 1234567890 triggers a pydantic error."""

    invalid_num = "1234567890"
    assert nhs_number.is_valid(invalid_num) is False

    with pytest.raises(ValidationError):
        Patient(
            nhs_id=invalid_num,
            name="Bad Data",
            gp_practice="Fragile Entity",
            dob=date(1990, 9, 9),
            specialty="GP",
            priority="Urgent",
            referral_date=date(2025, 1, 11),
            wait_weeks=1
        )