Here is a complete system design, algorithm, Mermaid flowchart, and Python implementation for the **Progressive Electricity Billing & Anomaly Detection System**.

---

## 1. Problem Statement

Design an automated electricity billing system that calculates monthly utility bills using progressive consumption slabs, fixed service charges, and conditional rebates or surcharges. Additionally, the system compares consumption trends across multiple months and flags unusual usage spikes (e.g., an increase greater than 50% compared to the previous month).

**Pricing Rules:**

* **Slab 1 (0 – 100 units):** $\$1.50$ per unit
* **Slab 2 (101 – 300 units):** $\$3.00$ per unit
* **Slab 3 (301+ units):** $\$5.00$ per unit
* **Fixed Charge:** $\$20.00$ per month
* **Rebate:** $10\%$ discount on energy charges if consumption is under $100$ units.
* **Surcharge:** $5\%$ surcharge on the total bill if consumption exceeds $400$ units.
* **Anomaly Threshold:** Any month-over-month consumption increase exceeding $50\%$ triggers an unusual increase alert.

---

## 2. Algorithm

1. **Initialize Parameters:** Define consumption slabs with respective rates, fixed monthly charges, rebate rules, surcharge rules, and anomaly thresholds.
2. **Input Data:** Collect monthly electricity consumption records (in kilowatt-hours / units) for a household over a sequence of months.
3. **Calculate Monthly Bills:**
* For each month, iterate through the progressive consumption slabs.
* Compute energy charges based on units consumed within each tier.
* Add the fixed service charge.
* Apply rebates (if units $< 100$) or surcharges (if units $> 400$).


4. **Compare Across Months:**
* Track consumption relative to the previous month.
* Calculate percentage growth: $\text{Percentage Increase} = \frac{\text{Current} - \text{Previous}}{\text{Previous}} \times 100$.
* If growth exceeds $50\%$, flag the month with an **Unusual Increase Alert**.


5. **Output Results:** Display an itemized summary table showing monthly consumption, calculated bills, and any anomaly warnings.

---

## 3. Flowchart

```mermaid
graph TD
    A[Start] --> B[Define Slabs, Rates, Fixed Fees & Rules]
    B --> C[Input Multi-Month Consumption Data]
    C --> D[Initialize Previous Units = None]
    D --> E{For each Month Record}
    E --> F[Calculate Progressive Slab Energy Charges]
    F --> G[Add Fixed Service Charge]
    G --> H{Units < 100?}
    H -- Yes --> I[Apply 10% Energy Rebate]
    H -- No --> J{Units > 400?}
    I --> K[Finalize Bill Amount]
    J -- Yes --> L[Apply 5% Total Surcharge]
    J -- No --> K
    L --> K
    K --> M{Previous Units Exists and Increase > 50%?}
    M -- Yes --> N[Flag Unusual Increase Alert]
    M -- No --> O[Normal Status]
    N --> P[Store Month Result]
    O --> P
    P --> Q[Update Previous Units = Current Units]
    Q --> R{More Months?}
    R -- Yes --> E
    R -- No --> S[Output Billing History & Anomaly Report]
    S --> T[End]

```

---


## 5. Sample Input

A dictionary containing monthly electricity consumption values (in kilowatt-hours / units):

```python
{
    "January": 85,
    "February": 115,
    "March": 130,
    "April": 340,
    "May": 510
}

```

---

## 6. Sample Output

```text
=== PROGRESSIVE ELECTRICITY BILLING & ANOMALY REPORT ===
Month     Units (kWh)    Bill ($)    Status / Alert
-------------------------------------------------------
January   85             $147.25     Normal
February  115            $169.5      Normal
March     130            $214.5      Normal
April     340            $995.0      Normal
May       510            $1827.0     ⚠️ Unusual Spike (+50.0%)

```
