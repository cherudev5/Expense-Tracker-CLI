import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

# Database initialization and connection
conn = sqlite3.connect('ExpenseTracker.db')
c = conn.cursor()

# Create tables if they don't exist
c.execute('''CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                starting_balance REAL
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS expenses (
                expense_id INTEGER PRIMARY KEY,
                user_id INTEGER,
                expense_name TEXT,
                amount REAL,
                date TEXT,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )''')

# Class for handling user operations
class User:
    def __init__(self, first_name, last_name, starting_balance):
        self.first_name = first_name
        self.last_name = last_name
        self.starting_balance = starting_balance

    def save_to_db(self):
        c.execute('''INSERT INTO users (first_name, last_name, starting_balance)
                    VALUES (?, ?, ?)''', (self.first_name, self.last_name, self.starting_balance))
        conn.commit()

# Class for handling expense operations
class Expense:
    def __init__(self, user_id, expense_name, amount):
        self.user_id = user_id
        self.expense_name = expense_name
        self.amount = amount
        self.date = datetime.now().strftime("%Y-%m-%d")

    def save_to_db(self):
        c.execute('''INSERT INTO expenses (user_id, expense_name, amount, date)
                    VALUES (?, ?, ?, ?)''', (self.user_id, self.expense_name, self.amount, self.date))
        conn.commit()

# Function to prompt user for input and validate
def get_valid_input(prompt, data_type):
    while True:
        user_input = input(prompt)
        try:
            return data_type(user_input)
        except ValueError:
            print("Invalid input. Please try again.")

# Function to generate detailed expense report
def generate_expense_report(user_id):
    c.execute('''SELECT expense_name, amount, date FROM expenses WHERE user_id=?''', (user_id,))
    expenses = c.fetchall()
    total_expense = sum(expense[1] for expense in expenses)
    return expenses, total_expense

# Function to plot budget vs. actual spending
def plot_budget_vs_actual(user_id, starting_balance):
    expenses, total_expense = generate_expense_report(user_id)
    labels = ['Starting Balance', 'Total Expense']
    values = ['Ksh{:.2f}'.format(starting_balance), 'Ksh{:.2f}'.format(total_expense)]

    plt.bar(labels, values, color=['blue', 'red'])
    plt.xlabel('Categories')
    plt.ylabel('Amount')
    plt.title('Budget vs. Actual Spending')
    plt.show()

# Function to view all expenses
def view_expenses(user_id):
    expenses, total_expense = generate_expense_report(user_id)
    if not expenses:
        print("No expenses found.")
    else:
        print("\nExpense Report:")
        for expense in expenses:
            print("Expense: {}, Amount: Ksh{:.2f}, Date: {}".format(expense[0], expense[1], expense[2]))
        print("Total Expense: Ksh{:.2f}".format(total_expense))
# Function to edit expenses       
def edit_expense(user_id):
    view_expenses(user_id)
    expense_id = get_valid_input("\nEnter the ID of the expense you want to edit: ", int)

    new_expense_name = input("Enter the new expense name: ")
    new_amount = get_valid_input("Enter the new amount: ", float)

    Expense.edit_expense(expense_id, new_expense_name, new_amount)
    print("Expense edited successfully!")
    
# Main function to handle user interaction
def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    # Check if user exists
    c.execute('''SELECT * FROM users WHERE first_name=? AND last_name=?''', (first_name, last_name))
    user = c.fetchone()

    if user:
        user_id = user[0]
        starting_balance = user[3]
        print("Welcome back, {} {}!".format(first_name, last_name))
    else:
        starting_balance = get_valid_input("Enter your starting balance: Ksh", float)
        new_user = User(first_name, last_name, starting_balance)
        new_user.save_to_db()
        user_id = c.lastrowid
        print("Welcome, {} {}!".format(first_name, last_name))

    while True:
        print("\nChoose an option:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Generate Expense Report")
        print("4. Edit Expense")
        print("5. Plot Budget vs. Actual Spending")
        print("6. Exit")

        option = get_valid_input("Enter your choice: ", int)

        if option == 1:
            expense_name = input("Enter the expense name: ")
            amount = get_valid_input("Enter the amount: Ksh", float)
            new_expense = Expense(user_id, expense_name, amount)
            new_expense.save_to_db()
            print("Expense added successfully!")

        elif option == 2:
            view_expenses(user_id)

        elif option == 3:
            expenses, total_expense = generate_expense_report(user_id)
            print("Total Expense: Ksh{:.2f}".format(total_expense))
            new_balance = starting_balance - total_expense
            print("New Balance: Ksh{:.2f}".format(new_balance))

        elif option == 4:
            edit_expense(user_id)
            
        elif option == 5:
            plot_budget_vs_actual(user_id, starting_balance)

        elif option == 6:
            break

        else:
            print("Invalid option. Please choose again.")

    conn.close()

if __name__ == "__main__":
    main()
