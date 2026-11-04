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
