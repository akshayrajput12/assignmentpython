'''1.	Expense Tracker:
Build an expense tracking system where users can input their daily expenses, categorize them, and view spending patterns over time
'''
class Expense:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount, category):
        expense = Expense(description, amount, category)
        self.expenses.append(expense)

    def view_expenses(self):
        for expense in self.expenses:
            print(f"Description: {expense.description}\nAmount: {expense.amount}\nCategory: {expense.category}\n")

    def get_total_expenditure(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        return total

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Get Total Expenditure")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            description = input("Enter the expense description: ")
            amount = float(input("Enter the expense amount: "))
            category = input("Enter the expense category: ")
            tracker.add_expense(description, amount, category)
        elif choice == 2:
            tracker.view_expenses()
        elif choice == 3:
            total = tracker.get_total_expenditure()
            print(f"Total Expenditure: {total}")
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
