Here is a complete package for the **Retail Billing with Multiple Discount Rules** system, including the problem statement, algorithm, Mermaid flowchart, Python source code, sample inputs, and sample outputs.

---

## 1. Problem Statement

Design an automated retail billing and invoicing system that processes a shopping cart containing multiple products with varying quantities and categories. The system must:

1. Apply **category-specific taxes** (e.g., Groceries at 0%, Apparel at 5%, Electronics at 12%).
2. Evaluate **threshold-based discounts** (e.g., 10% off if the gross purchase exceeds a certain amount).
3. Enforce **maximum concession limits** to cap discounts.
4. Generate a comprehensive itemized invoice displaying item subtotals, taxes, applied discounts, and the final payable amount.

---

## 2. Algorithm

1. **Start** and initialize the product cart with items (Name, Unit Price, Quantity, Category).
2. **Initialize** tracking variables for Subtotal, Total Tax, and Gross Amount.
3. **Iterate through each item in the cart:**
* Calculate $\text{Item Subtotal} = \text{Unit Price} \times \text{Quantity}$
* Determine **Tax Rate** based on the product category.
* Calculate $\text{Item Tax} = \text{Item Subtotal} \times \text{Tax Rate}$
* Add Item Subtotal and Item Tax to overall running totals.


4. **Calculate Gross Amount** = $\text{Overall Subtotal} + \text{Total Tax}$
5. **Evaluate Threshold Discount:**
* If Gross Amount $\ge \$150.00$, apply a 10% discount. Otherwise, 0% discount.


6. **Enforce Maximum Concession Limit:**
* If the calculated discount exceeds a maximum cap (e.g., $\$30.00$), set the discount to the maximum cap.


7. **Calculate Final Payable Amount** = $\text{Gross Amount} - \text{Applied Discount}$
8. **Display** the itemized invoice and final summary.
9. **End**

---

## 3. Flowchart (Mermaid Code)

```mermaid
graph TD
    A[Start] --> B[Initialize Cart Items & Rates]
    B --> C{Are there items left in cart?}
    C -- No --> F[Calculate Subtotal & Total Tax]
    C -- Yes --> D[Fetch Next Item: Price, Qty, Category]
    D --> E[Calculate Item Cost & Category Tax -> Add to Totals] --> C
    F --> G[Calculate Gross Amount = Subtotal + Tax]
    G --> H{Gross Amount >= $150.00?}
    H -- Yes --> I[Calculate 10% Threshold Discount] --> K
    H -- No --> J[Discount = 0.00] --> K
    K --> L{Discount > Max Concession Limit ($30.00)?}
    L -- Yes --> M[Cap Discount at $30.00] --> N
    L -- No --> N[Keep Calculated Discount] --> N
    N --> O[Calculate Final Payable = Gross Amount - Discount]
    O --> P[Display Itemized Invoice & Summary]
    P --> Z[End]

```

---

## 4. Python Source Code

```python
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

```

---

## 5. Sample Input

```python
shopping_cart = [
    {"name": "Wireless Mouse", "price": 25.00, "quantity": 2, "category": "Electronics"},
    {"name": "Organic Coffee", "price": 12.50, "quantity": 3, "category": "Grocery"},
    {"name": "Cotton T-Shirt", "price": 20.00, "quantity": 2, "category": "Apparel"},
    {"name": "Desk Lamp", "price": 45.00, "quantity": 1, "category": "General"}
]

```

---

## 6. Sample Output

```text
==================================================
               RETAIL TAX INVOICE                 
==================================================
1. Wireless Mouse (Electronics)
   2 x $25.00 = $50.00 | Tax: $6.00
2. Organic Coffee (Grocery)
   3 x $12.50 = $37.50 | Tax: $0.00
3. Cotton T-Shirt (Apparel)
   2 x $20.00 = $40.00 | Tax: $2.00
4. Desk Lamp (General)
   1 x $45.00 = $45.00 | Tax: $3.60
--------------------------------------------------
Subtotal        : $172.50
Total Tax       : $11.60
Gross Amount    : $184.10
Discount Applied: -$18.41
FINAL PAYABLE   : $165.69
==================================================

```
