import tkinter as tk
from tkinter import messagebox
from db_config import get_connection
from billing_logic import generate_bill

class BillingApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Billing Application")

        # Customer Name
        tk.Label(root, text="Customer Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        # Item Entry
        self.items = []
        tk.Label(root, text="Item").grid(row=1, column=0)
        self.item_entry = tk.Entry(root)
        self.item_entry.grid(row=1, column=1)

        tk.Label(root, text="Price").grid(row=2, column=0)
        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=2, column=1)

        tk.Button(root, text="Add Item", command=self.add_item).grid(row=3, column=0, columnspan=2)

        # Listbox to show items
        self.listbox = tk.Listbox(root, width=40)
        self.listbox.grid(row=4, column=0, columnspan=2)

        # Generate Bill
        tk.Button(root, text="Generate Bill", command=self.save_bill).grid(row=5, column=0, columnspan=2)

    def add_item(self):
        item = self.item_entry.get().strip()
        try:
            price = float(self.price_entry.get())
            if not item:
                raise ValueError("Item cannot be empty")
            self.items.append((item, price))
            self.listbox.insert(tk.END, f"{item} - ₹{price}")
            self.item_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter valid item and price.")

    def save_bill(self):
        customer = self.name_entry.get().strip()
        if not customer or not self.items:
            messagebox.showerror("Error", "Customer name and items are required.")
            return
        total = sum(price for _, price in self.items)
        path = generate_bill(customer, self.items, total)
        self.save_to_db(customer, total)
        messagebox.showinfo("Bill Generated", f"Bill saved to {path}")
        self.listbox.delete(0, tk.END)
        self.items.clear()

    def save_to_db(self, customer_name, total_amount):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO bills (customer_name, total_amount) VALUES (%s, %s)", 
                           (customer_name, total_amount))
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

if _name_ == "_main_":
    root = tk.Tk()
    app = BillingApp(root)
    root.mainloop()


