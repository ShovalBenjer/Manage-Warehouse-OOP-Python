import tkinter as tk
from tkinter import ttk


class ProductsView:
    def __init__(self, root, manage, start_row):
        self.product_filter = None
        self.product_list = None
        self.total_text = None
        self.manage = manage
        self.root = root
        self.start_row = start_row
        self.entries = []

    def show(self):
        frame = tk.Frame(self.root)
        frame.grid(row=self.start_row, column=0, sticky='w')  # Add sticky='w'

        self.root.columnconfigure(0, weight=1)  # Configure the column to expand

        title = tk.Label(frame, text='Products', fg='blue', font=("arial", 16), padx=10, pady=0)
        title.grid(row=0, column=0, sticky='w')

        self.total_text = tk.StringVar()
        self.total_text.set(f'Filter Products({len(self.manage.warehouse.products)}):')
        total_label = tk.Label(frame, textvariable=self.total_text)
        total_label.grid(row=1, column=0, sticky='w', pady=0, padx=10)

        self.product_filter = ttk.Combobox(frame, values=self.get_locations())
        self.product_filter.set("All")
        self.product_filter.grid(row=1, column=0, sticky='w', padx=10)
        self.product_filter.bind('<<ComboboxSelected>>', self.update_filter)

        self.product_list = ttk.Treeview(frame, columns=("#1", "#2", "#3", "#4"), show='headings', height=5)
        for i in range(4):
            self.product_list.column("#" + str(i + 1), width=113)
        self.product_list.heading("#1", text="SKU")
        self.product_list.heading("#2", text="Name")
        self.product_list.heading("#3", text="Quantity")
        self.product_list.heading("#4", text="Location")
        self.product_list.grid(row=2, column=0, columnspan=4, sticky='w', padx=10, pady=3)

        self.populate_product_list()  # Populate product list at the beginning

    def populate_product_list(self):
        for product in self.manage.warehouse.products:
            self.product_list.insert('', 'end', values=(product.sku, product.name, product.quantity, product.location))

    def update_filter(self, event):
        filter_value = self.product_filter.get()
        for product in self.product_list.get_children():
            self.product_list.delete(product)
        products_in_location = []
        for product in self.manage.warehouse.products:
            if filter_value == "All" or product.location == filter_value:
                self.product_list.insert('', 'end',
                                         values=(product.sku, product.name, product.quantity, product.location))
                products_in_location.append(product)
        self.total_text.set(f'Filter Products({len(products_in_location)}):')  # Update the total count

    def get_locations(self):
        locations = set(product.location for product in self.manage.warehouse.products)
        locations_list = sorted(list(locations))  # Sort the locations
        locations_list.insert(0, "All")
        return locations_list
