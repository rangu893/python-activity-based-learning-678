import math

def campus_event_financial_planning(venue, equipment, catering_pp, transport_pp, certificate_pp, sponsorships, registration_fee):
    # 1. Input Validation
    if venue < 0 or equipment < 0 or catering_pp < 0 or transport_pp < 0 or certificate_pp < 0 or sponsorships < 0 or registration_fee < 0:
        return {"Error": "Costs, sponsorships, and registration fees cannot be negative."}
    
    variable_cost_pp = catering_pp + transport_pp + certificate_pp
    
    if registration_fee <= variable_cost_pp:
        return {"Error": "Registration fee must exceed the variable cost per person to achieve break-even."}

    # 2. Cost Aggregations
    total_fixed_costs = venue + equipment
    net_fixed_costs = total_fixed_costs - sponsorships
    
    # 3. Break-Even Calculations
    if net_fixed_costs <= 0:
        break_even_count = 0
        status = "Sponsorships fully cover fixed expenses!"
    else:
        contribution_margin = registration_fee - variable_cost_pp
        break_even_count = math.ceil(net_fixed_costs / contribution_margin)
        status = "Break-even target established."

    return {
        "Total Fixed Costs": total_fixed_costs,
        "Total Sponsorships": sponsorships,
        "Net Fixed Costs": max(0.0, net_fixed_costs),
        "Variable Cost Per Person": variable_cost_pp,
        "Registration Fee Per Person": registration_fee,
        "Contribution Margin Per Person": registration_fee - variable_cost_pp,
        "Minimum Break-Even Count": break_even_count,
        "Planning Status": status
    }

# --- Execution Example ---
if __name__ == "__main__":
    result = campus_event_financial_planning(
        venue=1200.00,
        equipment=450.00,
        catering_pp=12.50,
        transport_pp=5.00,
        certificate_pp=2.50,
        sponsorships=500.00,
        registration_fee=35.00
    )
    
    print("========================================")
    print("    CAMPUS EVENT FINANCIAL PLANNING     ")
    print("========================================")
    for key, value in result.items():
        if isinstance(value, float):
            print(f"{key:32}: ${value:,.2f}")
        else:
            print(f"{key:32}: {value}")
    print("========================================")
