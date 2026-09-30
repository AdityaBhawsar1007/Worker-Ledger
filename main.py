from workers import*
from attendance import*
from payments import*
from ledger import*

workers = []
attendance = []
payments = []

while True:

    print("\n------------------------------------")
    print("            WORKER LEDGER")
    print("------------------------------------")
    print("1. Add Worker")
    print("2. View Workers")
    print("3. Attendance")
    print("4. Payment")
    print("5. Worker Ledger")
    print("6. Exit")
    print("------------------------------------")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_worker(workers)
    elif choice == "2":
        view_workers(workers)
    elif choice == "3":
        attendance_menu(workers, attendance)
    elif choice == "4":
        payment_menu(workers, payments)
    elif choice == "5":
        ledger_menu(workers, attendance, payments)
    elif choice == "6":
       print("Thank you for using Worker Ledger.")
       break
    else:
        print("Invalid Choice!!!")
