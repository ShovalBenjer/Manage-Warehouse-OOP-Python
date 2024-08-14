from Employee import Employee
from Manager import Manager
from data_utils import input_exception, employee_exception, phone_exception, id_exception
import tkinter as tk
from tkinter import ttk, messagebox


class EmployeeView:
    def __init__(self, root, manage, start_row):
        self.employee_list = None
        self.total_text = None
        self.employee_filter = None
        self.error_label = None
        self.manage = manage
        self.root = root
        self.start_row = start_row
        self.entries = []

    def show_error(self, message):
        self.error_label.config(fg='red')
        self.error_label["text"] = message

    def show(self):
        frame = tk.Frame(self.root)
        frame.grid(row=self.start_row)

        # Switch position of the title and error label
        title = tk.Label(frame, text='Employees', fg='blue', font=("arial", 16), padx=10)
        title.grid(row=0, column=0, sticky='w')

        # Additional empty label to create a gap
        tk.Label(frame, text='', pady=10).grid(row=1, column=0)

        self.error_label = tk.Label(frame, text='', fg='red', font=("arial", 12))
        self.error_label.grid(row=1, column=0, columnspan=6, sticky='w', padx=10, pady=2)

        labels = ["ID", "FirstName", "LastName", "PhoneNumber", "Address", "Gender"]
        for i, label in enumerate(labels):
            entry_frame = tk.Frame(frame)
            entry_frame.grid(row=2, column=i)
            tk.Label(entry_frame, text=label, fg='blue', font=("arial", 10)).grid(row=0, column=0)
            if label == "Gender":
                entry = ttk.Combobox(entry_frame, values=["M", "F"], width=6)
                entry.set("M")
            else:
                entry = tk.Entry(entry_frame, width=20)
            entry.grid(row=1, column=0, padx=5, pady=2)
            self.entries.append(entry)

        add_button = tk.Button(frame, text="Add", command=self.add_employee)
        add_button.grid(row=3, column=0, sticky='w', padx=10, pady=2)

        self.total_text = tk.StringVar()
        self.total_text.set(f'Filter Employees({len(self.manage.employees)}):')
        total_label = tk.Label(frame, textvariable=self.total_text)
        total_label.grid(row=4, column=0, sticky='w', pady=5, padx=10)

        self.employee_filter = ttk.Combobox(frame, values=["All", "Employee", "Manager"])
        self.employee_filter.set("All")
        self.employee_filter.grid(row=4, column=1, sticky='w')
        self.employee_filter.bind('<<ComboboxSelected>>', self.update_filter)

        self.employee_list = ttk.Treeview(frame, columns=("#1", "#2", "#3", "#4", "#5"), show='headings', height=5)
        for i in range(5):
            self.employee_list.column("#" + str(i + 1), width=90)
        self.employee_list.heading("#1", text="Type")
        self.employee_list.heading("#2", text="ID")
        self.employee_list.heading("#3", text="First Name")
        self.employee_list.heading("#4", text="Last Name")
        self.employee_list.heading("#5", text="Phone Number")
        self.employee_list.grid(row=5, column=0, columnspan=6, sticky='w', padx=10, pady=3)
        self.populate_employee_list()  # Populate employee list at the beginning

    def add_employee(self):
        e_id, firstname, lastname, phone_number, address, gender = [entry.get() for entry in self.entries]

        input_error_message = input_exception(e_id)
        if input_error_message:
            self.show_error(input_error_message)
            return

        employee_error_message = employee_exception(self.manage.employees, e_id)
        if employee_error_message:
            self.show_error(employee_error_message)
            return

        if not id_exception(e_id):
            self.show_error(f"Id '{e_id}' is not correct.")
            return
        if not firstname:
            self.show_error("First name must not be empty.")
            return
        if not lastname:
            self.show_error("Last name must not be empty.")
            return
        phone_error_message = phone_exception(phone_number)
        if phone_error_message:
            self.show_error(phone_error_message)
            return
        if not address:
            self.show_error("Address must not be empty.")
            return

        new_employee = Employee(e_id, firstname, lastname, phone_number, address, gender)

        if self.manage.add_employee(new_employee):
            self.total_text.set(f'Filter Employees({len(self.manage.employees)}):')
            self.populate_employee_list()
            for entry in self.entries:
                entry.delete(0, 'end')
            messagebox.showinfo("Success", f"Employee '{firstname} {lastname}' was added successfully.")
        else:
            self.show_error("Failed to add employee.")

    def update_filter(self, event):
        filter_value = self.employee_filter.get()
        self.populate_employee_list(filter_value)

    def populate_employee_list(self, filter_value="All"):
        for i in self.employee_list.get_children():
            self.employee_list.delete(i)
        filtered_employees = 0
        for employee in self.manage.employees:
            employee_type = "Manager" if isinstance(employee, Manager) else "Employee"
            if filter_value == "All" or filter_value == employee_type:
                self.employee_list.insert('', 'end', values=(
                    employee_type, employee.e_id, employee.firstname, employee.lastname, employee.phone_number))
                filtered_employees += 1
        self.total_text.set(f'Filter Employees({filtered_employees}):')
