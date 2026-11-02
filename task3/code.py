def calculate_hospital_bill(name, age, income, has_insurance, consultation, diagnostics, treatment):
    # 1. Validate billing constraints
    if consultation < 0 or diagnostics < 0 or treatment < 0 or age < 0 or income < 0:
        return {"Error": "Invalid input: Charges, age, and income cannot be negative."}
    
    # 2. Calculate Subtotal
    subtotal = consultation + diagnostics + treatment
    concession_amount = 0.0
    classification = "General Private"

    # 3. Apply Policy & Classification Rules
    if has_insurance:
        classification = "Insured"
        concession_amount = subtotal * 0.80  # Insurance covers 80%
    elif age >= 60:
        classification = "Senior Citizen Subsidized"
        concession_amount = subtotal * 0.15  # 15% senior concession
    elif income < 250000:
        classification = "Low-Income Subsidized"
        concession_amount = subtotal * 0.25  # 25% low-income concession
    else:
        classification = "General Private"
        concession_amount = 0.0

    # 4. Final Amount Calculation
    final_amount = subtotal - concession_amount

    # 5. Return Itemized Result
    return {
        "Patient Name": name,
        "Age": age,
        "Annual Income": income,
        "Patient Classification": classification,
        "Consultation Fee": consultation,
        "Diagnostic Charges": diagnostics,
        "Treatment Charges": treatment,
        "Subtotal": subtotal,
        "Concession / Insurance Coverage": concession_amount,
        "Final Payable Amount": final_amount
    }

# --- Execution Example ---
if __name__ == "__main__":
    # Test case: Senior Citizen without insurance
    bill_result = calculate_hospital_bill(
        name="Martha Wayne",
        age=65,
        income=450000,
        has_insurance=False,
        consultation=600.0,
        diagnostics=1400.0,
        treatment=5000.0
    )

    print("--- HOSPITAL BILLING SUMMARY ---")
    for key, value in bill_result.items():
        if isinstance(value, float):
            print(f"{key}: ${value:.2f}")
        else:
            print(f"{key}: {value}")
