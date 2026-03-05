# This test simulates a patient who has been for one day over the 18 weeks mark!
# This is the Referral to treatment logic. (RTT)

from datetime import datetime, timedelta

def test_rtt_breach_calculation():
    """A patient waiting > 126 days must be flagged as a BREACH!"""

    today = datetime.now().date()

    # Create a referral date from 127 days ago (18 wks) A breach
    referral_date = today - timedelta(days=127)

    # Calculate the weeks waiting
    days_waiting = (today - referral_date).days
    is_breach = days_waiting > 126

    # Asssertions
    assert is_breach is True
    assert (days_waiting / 7) > 18