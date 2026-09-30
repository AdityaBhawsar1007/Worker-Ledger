# Daily Wage Tracker and Worker Ledger

A Python command-line application for managing workers, daily attendance, wages and payments. It brings attendance records and payment calculations together so a user can see how much each worker has earned, how much has been paid and the remaining balance.

Developed as a first-semester programming project using functions, loops, lists, dictionaries and Python's built-in date-handling tools.

> **Data is kept only while the program is running.** This version does not save or load files. Exiting or closing the program clears all workers, attendance and payment entries.

## Problem Statement

Recording daily-wage attendance and payments manually can make it difficult to track custom wages, partial payments and outstanding balances. This project provides a simple menu-based system to organise those records and calculate totals during a work session.

It is intended as an academic prototype for small contractors, supervisors and anyone learning to build a basic worker-management application.

## Features

- **Worker management:** Add workers with their normal daily wages and view the worker list with automatic serial numbers.
- **Name-based selection:** Use worker names for attendance and payments. Name matching ignores uppercase and lowercase, and duplicate names are rejected.
- **Attendance:** Mark a worker present or absent for the computer's current date. Duplicate attendance for the same worker and date is blocked within the current cycle.
- **Custom daily wages:** Enter a different wage for a present worker or press Enter to use the normal wage.
- **Attendance register:** View all workers over a selected date range, with daily status, total present days, total absent days and total earned amount in one table.
- **Payments:** Record dated payments with optional notes and view a selected worker's payment history. Multiple payments to the same worker are supported.
- **Combined ledger:** View every worker's daily wage, attendance counts, total earned, total paid and balance in one table, followed by overall financial totals.
- **Cycle reset:** Clear attendance and payments for all workers after confirmation, while keeping their names and normal wages for the remainder of the session.

## Technologies and Concepts

| Technology or concept | Use in the project |
| --- | --- |
| Python 3 | Programming language |
| Windows Command Prompt | Running and interacting with the application |
| Functions and modules | Dividing the project into separate responsibilities |
| Lists and dictionaries | Holding workers, attendance and payments in memory |
| Conditions and loops | Menus, validation, searching and calculations |
| String methods | Cleaning names and comparing them without case sensitivity |
| String formatting | Displaying attendance and ledger tables |
| `datetime` and `timedelta` | Reading dates, using today's date and moving between days |
| `try/except` | Handling invalid dates and payment amounts |

No third-party packages, database or internet connection are required to run the application once Python is installed.

## Project Files

Keep the following files together in the same folder:

| File | Responsibility |
| --- | --- |
| `main.py` | Creates the three data lists and runs the main menu |
| `workers.py` | Adds, lists and finds workers |
| `attendance.py` | Marks attendance, handles dates and displays the attendance register |
| `payments.py` | Records payments and displays payment history |
| `ledger.py` | Calculates earnings and balances, displays the combined ledger and resets the cycle |
| `README.md` | Project overview and usage instructions |

Use these exact Python filenames. Download suffixes such as `workers(3).py` must be removed because the imports expect `workers.py`.

## Installation and Running

1. Install Python 3 and enable **Add Python to PATH** during installation if that option is shown.
2. Download or clone the project. If downloaded as a ZIP, extract it first.
3. Open the project folder in File Explorer, type `cmd` in its address bar and press Enter.
4. Check that Python is available:

   ```bat
   python --version
   ```

5. Start the application:

   ```bat
   python main.py
   ```

If your Windows installation uses the Python launcher instead, run:

```bat
py main.py
```

Run `main.py` to access the complete program. The other Python files provide functions used by the main menu.

## How to Use

The main menu contains:

```text
1. Add Worker
2. View Workers
3. Attendance
4. Payment
5. Worker Ledger
6. Exit
```

1. **Add workers:** Enter a non-empty, unique worker name and a positive daily wage in whole rupees.
2. **Mark attendance:** Open Attendance, choose Mark Attendance and enter the worker's name. Select Present or Absent. For Present, enter a custom wage or leave it blank to use the normal wage.
3. **View the register:** Open View Attendance and enter the start and end dates in `DD-MM-YYYY` format. Both dates are included in the report.
4. **Record a payment:** Open Payment, choose Record Payment and enter the name, date, positive whole-rupee amount and an optional note.
5. **Check the ledger:** Open Worker Ledger and choose View Workers Ledger to see all workers and financial totals.
6. **Start another cycle when needed:** Choose Clear Cycle and Start New Cycle, then type `CLEAR` to confirm. Any other response cancels the reset.
7. **Exit:** Choose option 6 when finished. All session data is discarded.

### Attendance Symbols

| Symbol | Meaning |
| --- | --- |
| `P` | Present |
| `A` | Absent |
| `-` | Attendance not marked |

An unmarked date is not counted as absent. Attendance marking uses today's computer date; the date range is used only when viewing the register.

### Wage and Balance Calculations

- **Present:** Earn the normal daily wage or the custom wage entered for that day.
- **Absent:** Earn zero for that day.
- **Total earned:** Sum of recorded attendance amounts.
- **Total paid:** Sum of recorded payments.
- **Balance:** Total earned minus total paid.

A positive balance is still payable to the worker. Zero means the amounts are settled. A negative balance indicates an advance or payment exceeding recorded earnings.

For example, with one present day for each worker:

| Worker | Normal daily wage | Wage recorded that day | Total paid | Balance |
| --- | ---: | ---: | ---: | ---: |
| Ravi | Rs. 500 | Rs. 500 | Rs. 300 | Rs. 200 |
| Sita | Rs. 600 | Rs. 650 (custom) | Rs. 700 | Rs. -50 |
| **Total** | — | **Rs. 1,150** | **Rs. 1,000** | **Rs. 150** |

The attendance register totals only the selected date range. The ledger totals all records in the current cycle, so the two reports can differ when a shorter attendance range is selected.

### Starting a New Cycle

A confirmed reset removes attendance records, payment history, earned totals and balances for all workers. It also removes unpaid amounts and advances; these are not carried forward. Worker names and normal daily wages remain until the program closes. There is no undo or cycle archive.

## Testing

Run `python main.py` and use the following manual checks. Use temporary sample data for testing.

| Test | Expected result |
| --- | --- |
| View workers before adding anyone | Displays `No workers added.` |
| Add `Ravi`, then try adding `ravi` | Rejects the duplicate name |
| Enter a blank name or zero daily wage | Rejects the entry |
| Mark a worker present and leave the custom wage blank | Uses the worker's normal daily wage |
| Mark another worker absent | Records zero earnings |
| Mark the same worker twice on the same date | Rejects the second attendance entry |
| View today's attendance for all workers | Shows the correct status and totals for each worker |
| Enter `31-02-2026` as a report or payment date | Rejects the invalid date |
| Enter a start date later than the end date | Rejects the report range |
| Record two payments to one worker | Includes both in payment history and the ledger |
| Pay more than a worker has earned | Shows a negative ledger balance |
| Cancel the cycle reset | Keeps all existing records |
| Confirm the cycle reset | Clears attendance and payments but keeps workers |
| Exit and restart | Starts with empty lists |

The uploaded version passed 46 functional and integration checks in a Linux Python environment, including a complete main-menu workflow. A Windows Command Prompt test should also be completed before submission. No automated test script is included among the five application files.

## Current Limitations

- Data is not preserved between runs.
- Attendance can only be marked for the current computer date and cannot be edited through the menu.
- Workers with the same name cannot be added separately.
- Amounts use whole rupees; decimal values are not supported. A custom attendance wage of zero is allowed.
- Long date ranges create wide attendance tables. Long names may affect alignment in the worker list and fixed-width ledger.
- The uploaded version still needs conversion-error handling for daily wages and custom attendance wages: unusual digit characters such as `²`, or excessively long numeric input, can cause `int()` to raise an error. Payment amounts already use `try/except`.

## Possible Future Improvements

- Optional file saving and loading.
- Editing attendance and payment entries.
- Exporting reports to CSV.
- Keeping previous cycles and carrying balances forward.
- A graphical interface.

## Author

**Aditya Bhawsar**  
B.Tech CSE, VIT Bhopal University 
