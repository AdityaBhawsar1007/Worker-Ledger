from workers import find_worker

def ledger_menu(workers, attendance, payments):

    while True:
        print("\n----- LEDGER MENU -----")
        print("1. View Workers Ledger")
        print("2. Clear Cycle and Start New Cycle (All Workers)")
        print("3. Back to Main Menu")

        c = input("Enter your choice: ").strip()

        if c == "1":
            view_ledger(workers, attendance, payments)
        elif c == "2":
            start_new_cycle(workers, attendance, payments)
        elif c == "3":
            return
        else:
            print("Invalid choice.")

def start_new_cycle(workers, attendance, payments):

    print("\n----- START NEW CYCLE -----")

    if len(attendance) == 0 and len(payments) == 0:
        print("The current cycle is already empty.")
        return

    print("This will clear attendance and payments for ALL workers.")
    print("Earned wages, paid amounts and balances will reset to zero.")
    print("Any unpaid wages or advances will also be cleared.")
    print("Worker names and daily wages will be kept.")
    print("This cannot be undone in the program.")

    cnf = input("Type CLEAR to confirm, or press Enter to cancel: ")

    if cnf.strip().upper() != "CLEAR":
        print("New cycle cancelled. No records were cleared.")
        return

    attendance.clear()
    payments.clear()
    print("New cycle started successfully for all workers.")

def wage_earned(name, attendance):

    total = 0
    for record in attendance:
        if record["name"].lower() == name.lower():
            total = total + record["amount"]
    return total

def payment_calc(name, payments):

    total = 0
    for payment in payments:
        if payment["name"].lower() == name.lower():
            total = total + payment["amount"]
    return total

def attendance_record(name, attendance):

    p = 0
    a = 0

    for record in attendance:
        if record["name"].lower() == name.lower():
            if record["status"] == "Present":
                p = p + 1
            elif record["status"] == "Absent":
                a = a + 1
    return p, a

def view_ledger(workers, attendance, payments):

    print("\n----- ALL WORKERS LEDGER -----")

    if len(workers) == 0:
        print("No workers added.")
        return

    row_format = "{:<5}{:<25}{:>12}{:>10}{:>10}{:>15}{:>15}{:>15}"

    header = row_format.format("No.", "Name", "Daily Wage", "Present", "Absent","Total Earned", "Total Paid", "Balance")

    print(header)
    print("-" * len(header))

    s = 1
    t_earned = 0
    t_paid = 0
    t_balance = 0

    for worker in workers:

        name = worker["name"]
        earned = wage_earned(name, attendance)
        paid = payment_calc(name, payments)
        balance = earned - paid
        present, absent = attendance_record(name, attendance)

        print(row_format.format(
            s, name, worker["wage"], present, absent,
            earned, paid, balance
        ))

        t_earned = t_earned + earned
        t_paid = t_paid + paid
        t_balance = t_balance + balance
        s = s + 1

    print("-" * len(header))

    print(row_format.format(
        "", "TOTAL", "", "", "",
        t_earned, t_paid, t_balance
    ))

    print("\nNegative balance means an advance paid to the worker.")
