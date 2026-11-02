def generate_retail_invoice(cart):
    category_tax_rates = {
        "Grocery": 0.00,
        "Apparel": 0.05,
        "Electronics": 0.12,
        "General": 0.08
    }
    
    max_concession_limit = 30.00
    threshold_limit = 150.00
    threshold_discount_rate = 0.10
    
    itemized_list = []
    subtotal = 0.0
    total_tax = 0.0
    
    # 1. Process each item in the cart
    for item in cart:
        name = item["name"]
        price = item["price"]
        qty = item["quantity"]
        category = item["category"]
        
        item_subtotal = price * qty
        tax_rate = category_tax_rates.get(category, 0.05)
        item_tax = item_subtotal * tax_rate
        item_total = item_subtotal + item_tax
        
        subtotal += item_subtotal
        total_tax += item_tax
        
        itemized_list.append({
            "Name": name,
            "Category": category,
            "Price": price,
            "Qty": qty,
            "Subtotal": item_subtotal,
            "Tax": item_tax,
            "Total": item_total
        })
        
    # 2. Calculate Gross Amount
    gross_amount = subtotal + total_tax
    
    # 3. Evaluate Threshold Discount
    if gross_amount >= threshold_limit:
        raw_discount = gross_amount * threshold_discount_rate
    else:
        raw_discount = 0.0
        
    # 4. Enforce Maximum Concession Limit
    applied_discount = min(raw_discount, max_concession_limit)
    
    # 5. Final Payable Amount
    final_payable = gross_amount - applied_discount
    
    return {
        "Items": itemized_list,
        "Subtotal": subtotal,
        "Total Tax": total_tax,
        "Gross Amount": gross_amount,
        "Applied Discount": applied_discount,
        "Final Payable": final_payable
    }

# --- Execution Example ---
if __name__ == "__main__":
    shopping_cart = [
        {"name": "Wireless Mouse", "price": 25.00, "quantity": 2, "category": "Electronics"},
        {"name": "Organic Coffee", "price": 12.50, "quantity": 3, "category": "Grocery"},
        {"name": "Cotton T-Shirt", "price": 20.00, "quantity": 2, "category": "Apparel"},
        {"name": "Desk Lamp", "price": 45.00, "quantity": 1, "category": "General"}
    ]
    
    invoice = generate_retail_invoice(shopping_cart)
    
    print("==================================================")
    print("               RETAIL TAX INVOICE                 ")
    print("==================================================")
    for idx, item in enumerate(invoice["Items"], 1):
        print(f"{idx}. {item['Name']} ({item['Category']})")
        print(f"   {item['Qty']} x ${item['Price']:.2f} = ${item['Subtotal']:.2f} | Tax: ${item['Tax']:.2f}")
    print("--------------------------------------------------")
    print(f"Subtotal        : ${invoice['Subtotal']:.2f}")
    print(f"Total Tax       : ${invoice['Total Tax']:.2f}")
    print(f"Gross Amount    : ${invoice['Gross Amount']:.2f}")
    print(f"Discount Applied: -${invoice['Applied Discount']:.2f}")
    print(f"FINAL PAYABLE   : ${invoice['Final Payable']:.2f}")
    print("==================================================")
