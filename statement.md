# Problem Statement

## Project Title

**Daily Wage Tracker and Worker Ledger**

## Background and Motivation

The thought of this project was inspired by witnessing my father's way of managing the workers under his contracting services. Most of the workers he hires are on a daily wage basis. He maintains a manual register of the workers and their daily attendance. He also calculates their total earnings at the end of each work cycle by considering their daily wage.

Some of them request advances and hence those payments are also recorded, to keep a track of the amount payable to them. Maintaining a record of each worker's attendance, along with the advances and final payments, makes the task tedious for my father, when there are a lot of workers involved.

This inspired me to design a simple Python program, that would collect all the details pertaining to a worker into a single entity and help in eliminating repetitive calculations.

## Problem to be Solved

Keeping track of daily-wage workers through a manual register necessitates that the contractor:

- Maintains the name and daily wage of each worker.

- Records the worker's attendance on a daily basis.

- Calculates their total earnings for the cycle from the attendance with possible modifications to the daily wage in a day.

- Records any advances and other payments made to the workers.

- Calculates the balance due payments by subtracting the total payments from total wages.

- Views the combined report of all the workers at the end of the cycle.

All of these tasks require the contractor to perform a lot of repetitive calculations and recordings which may result in errors and make the task tedious.

## Proposed Solution

The Daily Wage Tracker and Worker Ledger, is a menu driven Python application, that manages worker details, attendance, and payments made to them during a program session. The application calculates the total wages and balances due automatically and displays them collectively in a tabular column, for a better visual appeal as shown below.

**Remaining Balance = Total Earned Wages - Total Payments**

The above formula uses the total of all payments, including the advance payments that are recorded with the name of each worker.

A positive balance indicates the money due to the worker, and a negative balance indicates the overpayment or payment beyond the wages.

## Main Features

- **Worker management:** To add workers with their names and normal daily wages, and view the worker list.

- **Attendance management:** To mark a worker Present or Absent for the current date, with an option to add a custom wage for a Present day.

- **Attendance register:** To view attendance of all workers for a selected date range, with the number of present days, absent days and the amount earned for those present days.

- **Payment management:** To record a payment with a given date, amount and a note, along with viewing an individual worker's payments.

- **Combined ledger:** To display all workers attendance counts, amounts earned, payments, balances in combined table with overall amounts of all.

- **New cycle:** To confirm new cycle which clears all attendance and payments, but keeping the names of the workers and their normal wages during current run of the program.

## Example

A worker whose normal daily wage is Rs. 500 and he was present for 10 days, the total amount earned would be Rs. 5000. If he had received Rs. 1500 in advance, the balance due to him is calculated as:

**Rs. 5000 - Rs. 1,500 = Rs. 3,500**

The application calculates the balance using the amount earned from attendance and total payments.

## Scope and Limitations

The scope of this project is to develop a single-user, console based, academic application using Python functions, modules, lists, dictionaries and date handling. It does not involve the use of database or saving of records in files. All the records are temporary and the application is meant to display, but not implement, the actual register system.

The new cycle option clears all the attendance and payments, which also resets any advance or due amount, therefore those amounts cannot be carried forward.

## Expected Outcome

The project targets to provide a simplified way of recording and calculating wages of workers and their current dues. This helps in avoiding the repeated manual calculations that require a lot of repetitive steps. It uses the basic Python concepts to solve a common real-world problem that I witness in my father's day to day business.
