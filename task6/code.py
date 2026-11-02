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
