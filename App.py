from tkinter import *
import tkinter as tk
from EmployeeView import EmployeeView
from ProductsView import ProductsView
from ChartView import ChartView


def create_title(root, current_row):
    title = Label(root, text='Manage Warehouse', width=30, fg="black", font=("arial", 24))
    title.grid(row=current_row, column=0)


class App:
    def __init__(self, manage):
        self.manage = manage

    def show(self):
        app_width = 750
        app_height = 900
        root = Tk()
        root.title('Manage App')
        root.geometry(f'{app_width}x{app_height}')
        row = 0
        create_title(root, row)
        row += 1

        # Create a common frame
        common_frame = tk.Frame(root)
        common_frame.grid(row=row, column=0, sticky='w')

        # Create EmployeeView and show
        employee_view = EmployeeView(common_frame, self.manage, 0)
        employee_view.show()

        # Create ProductView and show
        product_view = ProductsView(common_frame, self.manage, 1)
        product_view.show()

        # Create ChartView and show
        chart_view = ChartView(common_frame, self.manage, 2)
        chart_view.show()

        root.mainloop()
