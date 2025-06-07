import json
import math
import os

def calculate_reimbursement(trip_duration_days, miles_traveled, total_receipts_amount):
    """Calculate reimbursement amount based on refined business logic.
    
    Args:
        trip_duration_days (int): Number of days for the trip.
        miles_traveled (float): Total miles traveled during the trip.
        total_receipts_amount (float): Total amount of receipts submitted.
    
    Returns:
        float: The reimbursement amount, rounded to 2 decimal places.
    """
    # Per Diem Calculation
    if trip_duration_days == 1:
        per_diem = 100.0  # Flat rate for single-day trips
    else:
        per_diem = 110.0  # Higher rate for multi-day trips
    total_per_diem = per_diem * trip_duration_days
    
    # Mileage Reimbursement Calculation
    if miles_traveled <= 100:
        mileage_reimb = 0.50 * miles_traveled  # $0.50 per mile for first 100 miles
    else:
        mileage_reimb = (0.50 * 100) + (0.40 * (miles_traveled - 100))  # $0.40 per mile beyond 100
    
    # Receipts Reimbursement Calculation
    receipts_reimb = min(0.5 * total_receipts_amount, 500.0)  # 50% of receipts, capped at $500
    
    # Efficiency Bonus
    if trip_duration_days > 0:
        miles_per_day = miles_traveled / trip_duration_days
        if 50 <= miles_per_day <= 100:
            efficiency_bonus = 20.0 * trip_duration_days  # $20 per day for efficient travel
        else:
            efficiency_bonus = 0.0
    else:
        efficiency_bonus = 0.0
    
    # Low Receipts Penalty
    if total_receipts_amount < 10:
        penalty = 5.0  # $5 penalty for receipts under $10
    else:
        penalty = 0.0
    
    # Total Reimbursement
    total_reimbursement = total_per_diem + mileage_reimb + receipts_reimb + efficiency_bonus - penalty
    return round(total_reimbursement, 2)


if __name__ == "__main__":
    import sys
    trip_duration_days      = int(sys.argv[1])
    miles_traveled          = float(sys.argv[2])
    total_receipts_amount   = float(sys.argv[3])
    result = calculate_reimbursement(trip_duration_days, miles_traveled, total_receipts_amount)
    print(result)
