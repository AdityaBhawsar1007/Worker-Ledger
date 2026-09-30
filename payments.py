from workers import find_worker
from attendance import read_date, date_text

def payment_menu(workers, payments):

    while True:
        print("\n----- PAYMENT -----")
        print("1. Record Payment")
        print("2. View Payments")
        print("3. Back to Main Menu")

        c = input("Enter your choice: ").strip()

        if c == "1":
            add_payment(workers, payments)
        elif c == "2":
            view_payments(workers, payments)
        elif c == "3":
            return
        else:
            print("Invalid choice.")


def add_payment(workers, payments):

    print("\n----- RECORD PAYMENT -----")

    if len(workers) == 0:
        print("No workers added.")
        return

    name = input("Enter worker name: ").strip()
    worker = find_worker(workers, name)

    if worker == None:
        print("Worker not found.")
        return

    date = read_date(input("Enter payment date (DD-MM-YYYY): "))

    if date is None:
        print("Invalid date. Use a real date in DD-MM-YYYY format.")
        return

    date = date_text(date)

    try:
        amount = int(input("Enter payment amount: ").strip())
    except ValueError:
        print("Please enter a valid whole-number amount.")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return
   
    note = input("Enter payment note: ").strip()

    payment = {"name": worker["name"] , "date": date , "amount": amount , "note": note}
    payments.append(payment)

    print("Payment recorded successfully.")

def view_payments(workers, payments):

    print("\n----- PAYMENT HISTORY -----")

    if len(payments) == 0:
        print("No payments recorded.")
        return

    name = input("Enter worker name: ").strip()
    worker = find_worker(workers, name)

    if worker == None:
        print("Worker not found.")
        return

    found = False

    for payment in payments:
        if payment["name"].lower() == name.lower():
            print(payment["date"], "- Rs.", payment["amount"], "-", payment["note"])

            found = True

    if found == False:
        print("No payments found.")
