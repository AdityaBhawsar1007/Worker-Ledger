from workers import find_worker
from datetime import datetime, timedelta

def attendance_menu(workers, attendance):

    while True:
        print("\n----- ATTENDANCE -----")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Back to Main Menu")

        c = input("Enter your choice: ").strip()

        if c == "1":
            mark_attendance(workers, attendance)
        elif c == "2":
            view_attendance(workers, attendance)
        elif c == "3":
            return
        else:
            print("Invalid choice.")

def read_date(t):

    t = t.strip()

    try:
        return datetime.strptime(t, "%d-%m-%Y").date()
    except ValueError:
        return None

def next_date(date):

    return date + timedelta(days=1)

def date_text(date):

    return date.strftime("%d-%m-%Y")

def mark_attendance(workers, attendance):

    print("\n----- MARK ATTENDANCE -----")

    if len(workers) == 0:
        print("No workers added.")
        return

    name = input("Enter worker name: ").strip()

    worker = find_worker(workers, name)

    if worker == None:
        print("Worker not found.")
        return

    date = datetime.now().strftime("%d-%m-%Y")

    print(f"Attendance for {date}")
    print("\n1. Present")
    print("2. Absent")

    c = input("Enter attendance: ")

    if c == "1":
        status = "Present"
        amount = worker["wage"]

    elif c == "2":
        status = "Absent"
        amount = 0

    else:
        print("Invalid choice.")
        return

    for data in attendance:
        if (data["name"].lower() == name.lower() and data["date"] == date):
            print("Attendance already marked for this date.")
            return

    if status == "Present":
        cst_wage = input("Enter wage for today or press Enter for normal wage: ")

        if cst_wage != "":
            if cst_wage.isdigit():
                amount = int(cst_wage)
            else:
                print("Invalid amount.")
                return

    data = {"name": worker["name"],
            "date": date,
            "status": status,
            "amount": amount}

    attendance.append(data)

    print("Attendance marked successfully.")

def view_attendance(workers, attendance):

    print("\n----- ATTENDANCE REGISTER -----")

    if len(workers) == 0:
        print("No workers added.")
        return

    start = read_date(input("Enter start date (DD-MM-YYYY): "))
    end = read_date(input("Enter end date (DD-MM-YYYY): "))

    if start is None or end is None:
        print("Invalid date. Use a real date in DD-MM-YYYY format.")
        return
    if start > end:
        print("Start date cannot be after end date.")
        return

    print("\nAttendance from", date_text(start), "to", date_text(end))
    print("P = Present, A = Absent, - = Not marked")

    rows = []
    name_width = 12
    for worker in workers:
        daily = {}
        present = 0
        absent = 0
        earned = 0

        for data in attendance:
            if data["name"].lower() == worker["name"].lower():
                date = read_date(data["date"])
                if date is not None and start <= date <= end:
                    daily[date] = data["status"]
                    if data["status"] == "Present":
                        present = present + 1
                    elif data["status"] == "Absent":
                        absent = absent + 1
                    earned = earned + data["amount"]

        rows.append([worker["name"], daily, present, absent, earned])
        if len(worker["name"]) > name_width:
            name_width = len(worker["name"])

    dates = []
    current = start

    while current <= end:
        dates.append(current)
        if current == end:
            break

        current = next_date(current)

    header = "{:<5}{:<{width}}".format("No.", "Name", width=name_width + 2)

    for date in dates:
        header = header + "{:>12}".format(date_text(date))

    header = header + "{:>15}{:>14}{:>20}".format("Total Present", "Total Absent", "Total Amount (Rs.)")

    print(header)
    print("-" * len(header))

    serial = 1

    for row in rows:
        line = "{:<5}{:<{width}}".format(serial, row[0], width=name_width + 2)

        for date in dates:
            status = "-"

            if date in row[1]:
                if row[1][date] == "Present":
                    status = "P"
                elif row[1][date] == "Absent":
                    status = "A"

            line = line + "{:>12}".format(status)

        line = line + "{:>15}{:>14}{:>20}".format( row[2], row[3], row[4])

        print(line)
        serial = serial + 1