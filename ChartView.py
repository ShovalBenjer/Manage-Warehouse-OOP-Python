import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class ChartView:
    def __init__(self, root, manage, start_row):
        self.canvas = None
        self.fig = None
        self.chart_choice = None
        self.chart_options = None
        self.frame = None
        self.manage = manage
        self.root = root
        self.start_row = start_row

    def show(self):
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=self.start_row, column=0, sticky='w', padx=10)

        title = tk.Label(self.frame, text='Statistics', fg='blue', font=("arial", 16), pady=2)
        title.grid(row=0, column=0, sticky='w')

        self.chart_options = ["Choose Stats", "Quantity By Location", "Employee By Phone", "Employee By Gender"]
        self.chart_choice = tk.StringVar()
        self.chart_choice.set(self.chart_options[0])
        chart_option_menu = tk.OptionMenu(self.frame, self.chart_choice, *self.chart_options, command=self.update_chart)
        chart_option_menu.grid(row=1, column=0, sticky='w', pady=5)

    def update_chart(self, chart_option):
        if self.fig is not None:
            self.fig.clear()
        if chart_option == "Choose Stats":  # Skip if the user selected "Choose Stats"
            if self.canvas is not None:
                self.canvas.get_tk_widget().destroy()  # remove old canvas if it exists
            return
        self.fig = Figure(figsize=(6, 2), dpi=75)
        if self.canvas is not None:
            self.canvas.get_tk_widget().destroy()  # remove old canvas if it exists
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.get_tk_widget().grid(row=2, column=0, sticky='w')
        if chart_option == "Quantity By Location":
            locations, quantities = self.get_quantity_by_location()
            self.fig.add_subplot(111).bar(locations, quantities)
        elif chart_option == "Employee By Phone":
            prefixes, employees = self.get_employee_by_phone()
            self.fig.add_subplot(111).bar(prefixes, employees)
        elif chart_option == "Employee By Gender":
            genders, employees = self.get_employee_by_gender()
            self.fig.add_subplot(111).bar(genders, employees)
        self.canvas.draw()

    def get_quantity_by_location(self):
        locations = np.array([product.location for product in self.manage.warehouse.products])
        unique_locations, quantities = np.unique(locations, return_counts=True)
        return unique_locations, quantities

    def get_employee_by_phone(self):
        phone_prefixes = np.array([employee.phone_number[:3] for employee in self.manage.employees])
        unique_prefixes, employee_counts = np.unique(phone_prefixes, return_counts=True)
        return unique_prefixes, employee_counts

    def get_employee_by_gender(self):
        genders = np.array([employee.gender for employee in self.manage.employees])
        unique_genders, employee_counts = np.unique(genders, return_counts=True)
        return unique_genders, employee_counts
