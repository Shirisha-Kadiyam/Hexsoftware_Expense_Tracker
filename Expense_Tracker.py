class Expense:
    def __init__(self,date,description,amount):
        self.date=date
        self.description=description
        self.amount=amount
class Expense_Tracker:
    def __init__(self):
        self.expenses=[]
    
    def add_expense(self,expense):
        self.expenses.append(expense)
    
    def remove_expense(self,index):
        if 0<=index<len(self.expenses):
            del self.expenses[index]
            print("expense removed successfully.")
        else:
            print("Invalid expense index.")
    
    def view_expenses(self):
        if len(self.expenses)==0:
            print("No expenses found.")
        else:
            print("Expense List:")
            for i, expense in enumerate(self.expenses,start=1):
                print(f"{i}.date: {expense.date} ,description: {expense.description} , amount: {expense.amount:.2f}")

            
    def total_expenses(self):
        total=sum(expense.amount for expense in self.expenses)
        print(f"total expenses:Rs{total:.2f}")

def main():
    tracker=Expense_Tracker()
        
    while True:
            print("\n Expense Tracker Menu:")
            print("1.Add Expense")
            print("2.Remove Expense")
            print("3.View Expense")
            print("4.Total Expense")
            print("5.Exit")

            choice=input("enter your choice(1-5):")
            if choice=="1":
                date=input("enter the date(yyyy-mm-dd):")
                description=input("enter the description:")
                amount=float(input("enter the amount:"))
                expense=Expense(date,description,amount)
                tracker.add_expense(expense)
                print("expense added successfully.")
            
            elif choice=="2":
                index=int(input("enter the expense index to remove:"))-1
                tracker.remove_expense(index)
            
            elif choice=="3":
                tracker.view_expenses()
            
            elif choice=="4":
                tracker.total_expenses()
            
            elif choice=="5":
                print("GoodBye!")
                break
            else:
                print("Invalid choice entered!try again")
if __name__=="__main__":
    main()
            


