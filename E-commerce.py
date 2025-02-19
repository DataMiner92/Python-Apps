import tkinter as tk
from tkinter import ttk, messagebox
import datetime


class ECommerceGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("E-Commerce System")
        self.master.configure(bg="#f0f0f0")
        self.master.geometry("700x600")  # Set initial window size
        self.master.resizable(True, True)  # Allow resizing

        # Set a consistent font
        self.font = ("Helvetica", 10)

        # Main Label
        self.label = tk.Label(
            master,
            text="Service Pro© E-Com System",
            font=("Helvetica", 18, "bold", "underline"),
            bg="lightgray",
        )
        self.label.pack(pady=10)

        # Dashboard Frame
        self.dashboard_frame = tk.Frame(master, bg="gray", bd=2, relief=tk.RIDGE)
        self.dashboard_frame.pack(pady=10, padx=10, fill=tk.X)

        # Buttons in Dashboard Frame
        self.products_button = ttk.Button(
            self.dashboard_frame, text="Show Products", command=self.show_products
        )
        self.products_button.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = ttk.Button(
            self.dashboard_frame, text="Add Product to Cart", command=self.show_add_dialog
        )
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.remove_button = ttk.Button(
            self.dashboard_frame,
            text="Remove Product from Cart",
            command=self.show_remove_dialog,
        )
        self.remove_button.grid(row=0, column=2, padx=5, pady=5)

        self.cart_button = ttk.Button(
            self.dashboard_frame, text="Show Cart", command=self.show_cart
        )
        self.cart_button.grid(row=0, column=3, padx=5, pady=5)

        self.order_button = ttk.Button(
            self.dashboard_frame, text="Place Order", command=self.place_order
        )
        self.order_button.grid(row=0, column=4, padx=5, pady=5)

        self.print_button = ttk.Button(
            self.dashboard_frame, text="Print Items", command=self.print_items
        )
        self.print_button.grid(row=0, column=5, padx=5, pady=5)

        self.clear_button = ttk.Button(
            self.dashboard_frame, text="Clear Area", command=self.clear_output
        )
        self.clear_button.grid(row=0, column=6, padx=5, pady=5)

        self.add_product_button = ttk.Button(
            self.dashboard_frame, text="Add New Product", command=self.show_add_product_dialog
        )
        self.add_product_button.grid(row=0, column=7, padx=5, pady=5)

        self.exit_button = ttk.Button(
            self.dashboard_frame, text="Exit", command=self.master.quit
        )
        self.exit_button.grid(row=0, column=8, padx=5, pady=5)

        # Output Text Area
        self.output_text = tk.Text(
            master, height=15, width=80, font=self.font, wrap=tk.WORD
        )
        self.output_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Initialize E-Commerce System
        self.ecommerce_system = ECommerceSystem()

    def show_products(self):
        self.update_output(self.ecommerce_system.show_products())

    def show_cart(self):
        self.update_output(self.ecommerce_system.show_cart())

    def place_order(self):
        self.update_output(self.ecommerce_system.place_order())

    def show_add_dialog(self):
        AddProductDialog(self.master, self.ecommerce_system, self.update_output)

    def show_remove_dialog(self):
        RemoveProductDialog(self.master, self.ecommerce_system, self.update_output)

    def show_add_product_dialog(self):
        AddNewProductDialog(self.master, self.ecommerce_system, self.update_output)

    def update_output(self, message):
        self.output_text.insert(tk.END, message + "\n")
        self.output_text.see(tk.END)  # Scroll to the end

    def clear_output(self):
        self.output_text.delete(1.0, tk.END)

    def print_items(self):
        # Print items (products or cart) to the output text area
        items = self.ecommerce_system.show_cart()
        self.update_output("=== Printed Items ===\n" + items)
        self.update_output("=== End transaction ===\n")


class AddProductDialog:
    def __init__(self, master, ecommerce_system, update_output):
        self.master = master
        self.ecommerce_system = ecommerce_system
        self.update_output = update_output

        self.dialog = tk.Toplevel(master)
        self.dialog.title("Add Product to Cart")
        self.dialog.configure(bg="#f0f0f0")

        self.label = tk.Label(
            self.dialog,
            text="Enter Product ID and Quantity:",
            font=("Arial", 12),
            bg="powderblue",
        )
        self.label.pack(pady=10)

        self.product_id_entry = ttk.Entry(self.dialog, font=("Arial", 12))
        self.product_id_entry.pack(pady=5)

        self.quantity_entry = ttk.Entry(self.dialog, font=("Arial", 12))
        self.quantity_entry.pack(pady=5)

        self.add_button = ttk.Button(self.dialog, text="Add", command=self.add_product)
        self.add_button.pack(pady=10)

    def add_product(self):
        product_id = self.product_id_entry.get()
        quantity = self.quantity_entry.get()
        if product_id.isdigit() and quantity.isdigit():
            result = self.ecommerce_system.add_product_to_cart(int(product_id), int(quantity))
            self.update_output(result)
            self.dialog.destroy()
        else:
            messagebox.showerror("Error", "Invalid input. Please enter valid product ID and quantity.")


class RemoveProductDialog:
    def __init__(self, master, ecommerce_system, update_output):
        self.master = master
        self.ecommerce_system = ecommerce_system
        self.update_output = update_output

        self.dialog = tk.Toplevel(master)
        self.dialog.title("Remove Product from Cart")
        self.dialog.configure(bg="powderblue")

        self.label = tk.Label(
            self.dialog,
            text="Enter Product ID:",
            font=("Arial", 12),
            bg="powderblue",
        )
        self.label.pack(pady=10)

        self.product_id_entry = ttk.Entry(self.dialog, font=("Arial", 12))
        self.product_id_entry.pack(pady=5)

        self.remove_button = ttk.Button(
            self.dialog, text="Remove", command=self.remove_product
        )
        self.remove_button.pack(pady=10)

    def remove_product(self):
        product_id = self.product_id_entry.get()
        if product_id.isdigit():
            result = self.ecommerce_system.remove_product_from_cart(int(product_id))
            self.update_output(result)
            self.dialog.destroy()
        else:
            messagebox.showerror("Error", "Invalid input. Please enter valid product ID.")


class AddNewProductDialog:
    def __init__(self, master, ecommerce_system, update_output):
        self.master = master
        self.ecommerce_system = ecommerce_system
        self.update_output = update_output

        self.dialog = tk.Toplevel(master)
        self.dialog.title("Add New Product")
        self.dialog.configure(bg="lightgreen")

        self.label = tk.Label(
            self.dialog,
            text="Enter Product Details:",
            font=("Arial", 12),
            bg="#f0f0f0",
        )
        self.label.pack(pady=10)

        self.id_label = tk.Label(self.dialog, text="Product ID:", bg="#f0f0f0")
        self.id_label.pack()
        self.id_entry = ttk.Entry(self.dialog, font=("Arial", 12))
        self.id_entry.pack(pady=5)

        self.name_label = tk.Label(self.dialog, text="Product Name:", bg="#f0f0f0")
        self.name_label.pack()
        self.name_entry = ttk.Entry(self.dialog, font=("Arial", 12))
        self.name_entry.pack(pady=5)

        self.price_label = tk.Label(self.dialog, text="Product Price:", bg="#f0f0f0")
        self.price_label.pack()
        self.price_entry = ttk.Entry(self.dialog, font=("Arial", 12))
        self.price_entry.pack(pady=5)

        self.add_button = ttk.Button(self.dialog, text="Add Product", command=self.add_new_product)
        self.add_button.pack(pady=10)

    def add_new_product(self):
        product_id = self.id_entry.get()
        product_name = self.name_entry.get()
        product_price = self.price_entry.get()

        if product_id.isdigit() and product_name and product_price.replace(".", "").isdigit():
            product_id = int(product_id)
            product_price = float(product_price)

            # Check if product ID already exists
            if any(p.id == product_id for p in self.ecommerce_system.products):
                messagebox.showerror("Error", "Product ID already exists. Please use a unique ID.")
            else:
                new_product = Product(product_id, product_name, product_price)
                self.ecommerce_system.products.append(new_product)
                self.update_output(f"New product added: {product_name} (ID: {product_id}, Price: ${product_price})")
                self.dialog.destroy()
        else:
            messagebox.showerror("Error", "Invalid input. Please enter valid product details.")


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.price * self.quantity


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        existing_item = next(
            (item for item in self.items if item.product.id == product.id), None
        )
        if existing_item:
            existing_item.quantity += quantity
        else:
            self.items.append(CartItem(product, quantity))

    def remove_item(self, product_id):
        self.items = [item for item in self.items if item.product.id != product_id]

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items)

    def show_cart(self):
        output = "Cart:\n"
        for item in self.items:
            output += f"{item.product.name} - Quantity: {item.quantity} - Total Price: ${item.get_total_price()}\n"
        output += f"Total Price: ${self.get_total_price()}"
        return output


class ECommerceSystem:
    def __init__(self):
        self.products = []
        self.cart = Cart()

    def show_products(self):
        output = "Available Products:\n"
        for product in self.products:
            output += f"ID: {product.id} - {product.name} - Price: ${product.price}\n"
        return output

    def add_product_to_cart(self, product_id, quantity):
        product = next((p for p in self.products if p.id == product_id), None)
        if product:
            self.cart.add_item(product, quantity)
            return f"{quantity} {product.name}(s) added to cart."
        else:
            return "Product not found."

    def remove_product_from_cart(self, product_id):
        self.cart.remove_item(product_id)
        return "Product removed from cart."

    def show_cart(self):
        return self.cart.show_cart()

    def place_order(self):
        time = datetime.datetime.now()
        time_check = time.strftime("%D %H:%M:%S")
        output = 'You have successfully ordered!\nThank you shopping with us.ShopPro© 2025.\n' + time_check
        self.cart = Cart()
        return output


def main():
    root = tk.Tk()
    ecommerce_gui = ECommerceGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()