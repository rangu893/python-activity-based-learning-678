Here is a complete package for the **Railway Fare and Reservation Calculator** system, including the problem statement, algorithm, Mermaid flowchart, Python source code, sample inputs, and sample outputs.

---

## 1. Problem Statement

Design an automated railway ticketing and fare calculation system. The system must process journey details including **distance**, **travel class** (e.g., Sleeper, AC 3-Tier, AC 2-Tier), and a list of **passengers** with their ages. It must compute base fares according to distance slabs and class rates, apply **age-based concessions** (child and senior citizen discounts), add fixed **reservation fees**, and handle **cancellation penalties** if applicable, generating a detailed fare statement.

---

## 2. Algorithm

1. **Start** and input journey distance, travel class, and passenger list (Name, Age).
2. **Validate Inputs:** Check if distance is greater than 0 and if the selected class is valid.
3. **Determine Base Rate per KM** based on the travel class:
* Sleeper: $0.50 / km
* AC 3-Tier: $1.20 / km
* AC 2-Tier: $1.80 / km


4. **Iterate through each passenger:**
* Calculate $\text{Base Fare} = \text{Distance} \times \text{Class Rate}$
* Apply Concession:
* If Age $\le 5$: Free / 100% concession
* If Age between 6 and 12: 50% concession
* If Age $\ge 60$: 40% concession
* Otherwise: No concession (0%)


* Add fixed **Reservation Fee** (e.g., $15.00 per ticket).
* Accumulate individual fares into the **Total Group Fare**.


5. **Display** the itemized passenger ticket statement and total payable amount.
6. **End**

---

## 3. Flowchart (Mermaid Code)

```mermaid
graph TD
    A[Start] --> B[Input Distance, Class, & Passenger List]
    B --> C{Is Distance > 0 & Class Valid?}
    C -- No --> D[Error: Invalid Inputs] --> Z[End]
    C -- Yes --> E[Determine Rate per KM based on Class]
    E --> F{Are there passengers left?}
    F -- No --> K[Calculate Total Group Fare]
    F -- Yes --> G[Get Next Passenger Age]
    G --> H{Check Age Concession Bracket}
    H -- Age <= 5 --> I[100% Off + Reservation Fee] --> J[Add to Total] --> F
    H -- Age 6 to 12 --> I2[50% Concession + Reservation Fee] --> J --> F
    H -- Age >= 60 --> I3[40% Concession + Reservation Fee] --> J --> F
    H -- Regular Adult --> I4[0% Concession + Reservation Fee] --> J --> F
    K --> L[Display Itemized Fare Summary]
    L --> Z[End]

```

---

## 4. Python Source Code

```python
def calculate_railway_fare(distance, travel_class, passengers):
    # Class rates per kilometer
    class_rates = {
        "Sleeper": 0.50,
        "AC 3-Tier": 1.20,
        "AC 2-Tier": 1.80
    }
    
    if distance <= 0 or travel_class not in class_rates:
        return {"Error": "Invalid distance or travel class."}
    
    rate_per_km = class_rates[travel_class]
    reservation_fee = 15.00
    
    itemized_passengers = []
    total_group_fare = 0.0
    
    for name, age in passengers:
        base_fare = distance * rate_per_km
        concession_rate = 0.0
        concession_type = "Regular Adult"
        
        # Age-based concessions
        if age <= 5:
            concession_rate = 1.00  # Free ticket
            concession_type = "Infant (Free)"
        elif 6 <= age <= 12:
            concession_rate = 0.50  # 50% discount
            concession_type = "Child (50% Off)"
        elif age >= 60:
            concession_rate = 0.40  # 40% discount
            concession_type = "Senior Citizen (40% Off)"
            
        discount_amount = base_fare * concession_rate
        fare_after_concession = base_fare - discount_amount
        final_ticket_price = fare_after_concession + reservation_fee
        
        total_group_fare += final_ticket_price
        
        itemized_passengers.append({
            "Name": name,
            "Age": age,
            "Category": concession_type,
            "Base Fare": base_fare,
            "Discount": discount_amount,
            "Reservation Fee": reservation_fee,
            "Total Ticket Price": final_ticket_price
        })
        
    return {
        "Distance (km)": distance,
        "Travel Class": travel_class,
        "Passenger Breakdown": itemized_passengers,
        "Total Group Fare": total_group_fare
    }

# --- Execution Example ---
if __name__ == "__main__":
    journey_distance = 650.0  # in km
    selected_class = "AC 3-Tier"
    passenger_list = [
        ("David Miller", 35),
        ("Sarah Miller", 32),
        ("Leo Miller", 9),
        ("Arthur Miller", 68)
    ]
    
    result = calculate_railway_fare(journey_distance, selected_class, passenger_list)
    
    print("==================================================")
    print("          RAILWAY FARE STATEMENT SUMMARY          ")
    print("==================================================")
    print(f"Journey Distance : {result['Distance (km썬']} km" if 'Distance (km썬' in result else f"Journey Distance : {result['Distance (km)']} km")
    print(f"Travel Class     : {result['Travel Class']}")
    print("--------------------------------------------------")
    
    for p in result["Passenger Breakdown"]:
        print(f"Passenger : {p['Name']} (Age: {p['Age']} - {p['Category']})")
        print(f"  Base Fare       : ${p['Base Fare']:.2f}")
        print(f"  Discount        : -${p['Discount']:.2f}")
        print(f"  Reservation Fee : ${p['Reservation Fee']:.2f}")
        print(f"  Ticket Total    : ${p['Total Ticket Price']:.2f}")
        print("--------------------------------------------------")
        
    print(f"TOTAL GROUP FARE  : ${result['Total Group Fare']:.2f}")
    print("==================================================")

```

---

## 5. Sample Input

```python
journey_distance = 650.0
selected_class = "AC 3-Tier"
passenger_list = [
    ("David Miller", 35),
    ("Sarah Miller", 32),
    ("Leo Miller", 9),
    ("Arthur Miller", 68)
]

```

---

## 6. Sample Output

```text
==================================================
          RAILWAY FARE STATEMENT SUMMARY          
==================================================
Journey Distance : 650.0 km
Travel Class     : AC 3-Tier
--------------------------------------------------
Passenger : David Miller (Age: 35 - Regular Adult)
  Base Fare       : $780.00
  Discount        : -$0.00
  Reservation Fee : $15.00
  Ticket Total    : $795.00
--------------------------------------------------
Passenger : Sarah Miller (Age: 32 - Regular Adult)
  Base Fare       : $780.00
  Discount        : -$0.00
  Reservation Fee : $15.00
  Ticket Total    : $795.00
--------------------------------------------------
Passenger : Leo Miller (Age: 9 - Child (50% Off))
  Base Fare       : $780.00
  Discount        : -$390.00
  Reservation Fee : $15.00
  Ticket Total    : $405.00
--------------------------------------------------
Passenger : Arthur Miller (Age: 68 - Senior Citizen (40% Off))
  Base Fare       : $780.00
  Discount        : -$312.00
  Reservation Fee : $15.00
  Ticket Total    : $483.00
--------------------------------------------------
TOTAL GROUP FARE  : $2478.00
==================================================

```
