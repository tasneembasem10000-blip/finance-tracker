import tkinter as tk

class Transaction:
# الكلاس ده بيمثل أي عملية مالية (سواء دخل أو مصروف)
    def __init__(self,amount,category,date):
        self.amount = amount                                  # تخزين قيمة الفلوس (مثلاً 100 جنيه)
        self.category = category                              # نوع العملية (أكل - مرتب - مواصلات...)
        self.date = date                                      # تاريخ العملية
    
    def get_summary(self):
        return f"{self.category} - {self.amount} on {self.date}"
    

class Expense(Transaction):                                                                            # Expense Class (مصروف)
    def get_summary(self):
        return f"Expense: {self.category} - {self.amount} on {self.date}"
    

class Income(Transaction):                                                                             # Income Class (دخل)
    def get_summary(self):
        return f"Income: {self.category} + {self.amount} on {self.date}"


class FinanceManager:                                                                                 # اداره كل العمليات المالية
    def __init__(self):
        self.transactions = []                                                                        
    
    def add_transaction(self ,transaction):                                                           # بنضيف object (Expense أو Income)
        self.transactions.append(transaction)                                                         

    def get_all_transactions(self):                                                                     # عرض كل العمليات
        return self.transactions
    
    def delete_transaction(self , index):                                                               # حذف عملية
        if 0 <= index < len(self.transactions):
            self.transactions.pop(index)

    def get_balance(self):                                                                               # حساب الرصيد النهائي
        total = 0
        for t in self.transactions:
            if isinstance(t,Expense):
                total -= t.amount
            else :
                total += t.amount
        return total
    
#################################
#              GUI              
#################################
manager = FinanceManager()

root = tk.Tk()
root.title("Finance Tracker")
root.geometry("400x500")
root.configure(bg="#FFE5B4")

title = tk.Label(root, text="Finance Tracker 💰", font=("Arial", 18, "bold"), bg="#FFE5B4")
title.pack(pady=10)

def update_balance():
    balance = manager.get_balance()
    balance_label.config(text=f"Balance: {balance} 💰")

#inputs&frames

input_frame = tk.Frame(root, bg="#DAA06D")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Amount", bg="#DAA06D").pack()
amount_entry = tk.Entry(input_frame)
amount_entry.pack()

tk.Label(input_frame, text="Category", bg="#DAA06D").pack()
category_entry = tk.Entry(input_frame)
category_entry.pack()

type_var = tk.StringVar(value="Expense")


radio_frame = tk.Frame(root, bg="#FFE5B4")
radio_frame.pack()
tk.Radiobutton(radio_frame, text="Expense", variable=type_var, value="Expense",
               bg="#FFE5B4", selectcolor="#FDFFFB").pack(side="left", padx=15)
tk.Radiobutton(radio_frame, text="Income", variable=type_var, value="Income",
               bg="#FFE5B4", selectcolor="#FFFFFF").pack(side="left", padx=15)

button_frame = tk.Frame(root, bg="#FFE5B4")
button_frame.pack(pady=10)


def add_transaction():
    amount = float(amount_entry.get())
    category = category_entry.get()
    if type_var.get() == "Expense":
        t = Expense(amount, category, "today")
    else:
        t = Income(amount, category, "today")
    manager.add_transaction(t)
    refresh_list()
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)

tk.Button(button_frame, text="Add", command=add_transaction, bg="green", fg="white", width=10).pack(side="left", padx=5)


balance_label = tk.Label(root, text="Balance: 0 💰", font=("Arial", 14, "bold"), bg="#7BA05B")
balance_label.pack(pady=10)

list_box = tk.Listbox(root, width=50)
list_box.pack(pady=10)

def refresh_list():                                                                         # تحديث الرصيد مع كل تحديث
    list_box.delete(0, tk.END)
    for t in manager.get_all_transactions():
        list_box.insert(tk.END, t.get_summary())
    update_balance()

def delete_transaction():                                                                # حذف عنصر بعد تحديده
    selected = list_box.curselection()
    if not selected:
        return
    index = selected[0]
    manager.delete_transaction(index)
    refresh_list()

tk.Button(button_frame, text="Delete", command=delete_transaction, bg="red", fg="white", width=10).pack(side="left", padx=5)


root.mainloop()
        

    





    
