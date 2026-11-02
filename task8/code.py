def analyze_manufacturing_profitability(
    units, material_cost, labor_hours, labor_rate, 
    machine_hours, machine_rate, wastage_pct, 
    selling_price, target_margin_pct
):
    # 1. Validate Inputs
    if units <= 0 or material_cost < 0 or labor_hours < 0 or labor_rate < 0 or \
       machine_hours < 0 or machine_rate < 0 or wastage_pct < 0 or selling_price < 0:
        return {"Error": "Invalid inputs: Costs, hours, and quantities cannot be negative."}

    # 2. Compute Costs per unit
    adjusted_material_cost = material_cost * (1 + (wastage_pct / 100.0))
    labor_cost = labor_hours * labor_rate
    machine_cost = machine_hours * machine_rate
    
    total_cost_per_unit = adjusted_material_cost + labor_cost + machine_cost
    total_batch_cost = total_cost_per_unit * units
    
    # 3. Compute Revenue & Profit
    total_revenue = selling_price * units
    actual_profit = total_revenue - total_batch_cost
    actual_margin_pct = (actual_profit / total_revenue * 100) if total_revenue > 0 else 0.0
    
    # 4. Target Evaluation
    target_met = actual_margin_pct >= target_margin_pct
    status = "Target Met Successfully" if target_met else "Target Not Met"

    # 5. Return Statement
    return {
        "Units Produced": units,
        "Adjusted Material Cost/Unit": adjusted_material_cost,
        "Labor Cost/Unit": labor_cost,
        "Machine Cost/Unit": machine_cost,
        "Total Cost per Unit": total_cost_per_unit,
        "Total Batch Cost": total_batch_cost,
        "Total Revenue": total_revenue,
        "Actual Profit": actual_profit,
        "Actual Margin (%)": actual_margin_pct,
        "Target Margin (%)": target_margin_pct,
        "Production Status": status
    }

# --- Execution Example ---
if __name__ == "__main__":
    result = analyze_manufacturing_profitability(
        units=1000,
        material_cost=25.00,
        labor_hours=2.0,
        labor_rate=15.00,
        machine_hours=1.5,
        machine_rate=40.00,
        wastage_pct=5.0,        # 5% material wastage
        selling_price=120.00,
        target_margin_pct=25.0  # 25% target profit margin
    )
    
    print("========================================")
    print("  MANUFACTURING PROFITABILITY ANALYSIS  ")
    print("========================================")
    for key, value in result.items():
        if isinstance(value, float):
            if "Margin" in key:
                print(f"{key:30}: {value:.2f}%")
            else:
                print(f"{key:30}: ${value:,.2f}")
        else:
            print(f"{key:30}: {value}")
    print("========================================")
