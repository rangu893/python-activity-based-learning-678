class ElectricityBillingSystem:
    def __init__(self):
        # Progressive slabs: (upper_limit, rate_per_unit)
        self.slabs = [
            (100, 1.50),
            (300, 3.00),
            (float('inf'), 5.00)
        ]
        self.fixed_charge = 20.00

    def calculate_bill(self, units):
        energy_charge = 0.0
        remaining_units = units
        previous_limit = 0

        # Calculate progressive slab charges
        for limit, rate in self.slabs:
            slab_range = limit - previous_limit
            if remaining_units > slab_range:
                energy_charge += slab_range * rate
                remaining_units -= slab_range
                previous_limit = limit
            else:
                energy_charge += remaining_units * rate
                break

        total_bill = energy_charge + self.fixed_charge

        # Apply rebate or surcharge
        if units < 100:
            total_bill -= energy_charge * 0.10  # 10% rebate on energy charge
        elif units > 400:
            total_bill += total_bill * 0.05    # 5% surcharge on total bill

        return round(total_bill, 2)

    def analyze_household_bills(self, monthly_data):
        results = []
        prev_units = None

        print("=== PROGRESSIVE ELECTRICITY BILLING & ANOMALY REPORT ===")
        print(f"{'Month':<10}{'Units (kWh)':<15}{'Bill ($)':<12}{'Status / Alert'}")
        print("-" * 55)

        for month, units in monthly_data.items():
            bill = self.calculate_bill(units)
            alert_status = "Normal"

            if prev_units is not None and prev_units > 0:
                increase_pct = ((units - prev_units) / prev_units) * 100
                if increase_pct > 50:
                    alert_status = f"⚠️ Unusual Spike (+{increase_pct:.1f}%)"

            print(f"{month:<10}{units:<15}{'$' + str(bill):<12}{alert_status}")
            
            prev_units = units
            results.append({"month": month, "units": units, "bill": bill, "status": alert_status})

        return results

# --- Sample Execution ---
if __name__ == "__main__":
    # Sample multi-month consumption data
    household_consumption = {
        "January": 85,    # Under 100 units -> Rebate applied
        "February": 115,  # Normal usage in slab 2
        "March": 130,     # Normal usage
        "April": 340,     # Higher usage in slab 3
        "May": 510        # Heavy AC usage -> Surcharge applied + Unusual spike compared to April
    }

    system = ElectricityBillingSystem()
    system.analyze_household_bills(household_consumption)
