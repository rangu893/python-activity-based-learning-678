def calculate_payroll(emp_id, name, basic, allowances, ot_hours, ot_rate, incentives):
    # 1. Validate inputs
    if basic < 0 or allowances < 0 or ot_hours < 0 or ot_rate < 0 or incentives < 0:
        return {"Error": "Inputs cannot be negative."}
    
    # 2. Calculate Earnings
    ot_pay = ot_hours * ot_rate
    gross_salary = basic + allowances + ot_pay + incentives
    
    # 3. Progressive Tax Bracket Evaluation
    if gross_salary <= 30000:
        tax_rate = 0.05
    elif gross_salary <= 70000:
        tax_rate = 0.10
    else:
        tax_rate = 0.20
        
    income_tax = gross_salary * tax_rate
    provident_fund = basic * 0.12  # Standard 12% PF on basic pay
    total_deductions = income_tax + provident_fund
    
    # 4. Calculate Net Salary
    net_salary = gross_salary - total_deductions
    
    # 5. Return structured statement
    return {
        "Employee ID": emp_id,
        "Employee Name": name,
        "Basic Pay": basic,
        "Allowances": allowances,
        "Overtime Pay": ot_pay,
        "Incentives": incentives,
        "Gross Salary": gross_salary,
        "Income Tax": income_tax,
        "Provident Fund (PF)": provident_fund,
        "Total Deductions": total_deductions,
        "Net Salary": net_salary
    }

# --- Execution Example ---
if __name__ == "__main__":
    statement = calculate_payroll(
        emp_id="EMP1024",
        name="Alex Smith",
        basic=45000.0,
        allowances=8000.0,
        ot_hours=10,
        ot_rate=250.0,
        incentives=5000.0
    )
    
    print("========================================")
    print("        EMPLOYEE SALARY STATEMENT       ")
    print("========================================")
    for key, value in statement.items():
        if isinstance(value, float):
            print(f"{key:25}: ${value:,.2f}")
        else:
            print(f"{key:25}: {value}")
    print("========================================")
