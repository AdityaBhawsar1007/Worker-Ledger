# Problem Statement

## Project Title

Daily Wage Tracker and Worker Ledger

## Background and Motivation

The idea for this project came from observing how my father manages workers in his contracting work. Many workers work under him, and each worker has a fixed daily wage. He records their attendance in a register and manually calculates their total earnings at the end of each work cycle.

Some workers take advance payments during the cycle. These amounts must also be recorded and deducted from their earnings to find the remaining amount payable. Keeping track of attendance, advances and final payments together can become time-consuming, especially when there are many workers.

This real-life situation motivated me to develop a simple Python program that brings these details together and reduces repeated manual calculations.

## Problem to Be Solved

Managing daily-wage workers through a manual register requires the contractor to:

- Maintain each worker's name and daily wage.
- Record daily attendance accurately.
- Calculate earnings from attendance, including any changes in the wage for a particular day.
- Track advance payments and other payments made during the cycle.
- Deduct payments from earnings to calculate the remaining balance.
- Review all workers' totals at the end of the cycle.

Doing these tasks manually can lead to missed entries, calculation mistakes and difficulty checking how much is still payable to each worker.

## Proposed Solution

The Daily Wage Tracker and Worker Ledger is a menu-driven Python application that manages worker details, attendance and payments during a program session. It calculates earnings and balances automatically and displays all workers together in a tabular ledger.

The program uses the following calculation:

**Remaining Balance = Total Earned Wages - Total Payments**

Advance payments are included in total payments. A positive balance shows the amount still payable, while a negative balance shows that the worker has received more than their recorded earnings.

## Main Features

1. **Worker management:** Add workers with their names and normal daily wages, and view the worker list.
2. **Attendance management:** Mark a worker Present or Absent for the current date, with an optional custom wage for a present worker.
3. **Attendance register:** View all workers' attendance for a selected date range, along with present days, absent days and earned amounts.
4. **Payment management:** Record payments with a date, amount and note, and view an individual worker's payment history.
5. **Combined ledger:** Display all workers' attendance counts, earnings, payments and balances in one table, with overall financial totals.
6. **New cycle:** Clear attendance and payments after confirmation while retaining worker names and normal wages during the current session.

## Example

If a worker earns Rs. 500 per day and is present for 10 days, their total earnings are Rs. 5,000. If they have already received Rs. 1,500 in advance, the remaining amount payable is:

**Rs. 5,000 - Rs. 1,500 = Rs. 3,500**

The program calculates this balance from the recorded attendance and payments.

## Scope and Limitations

This version is a single-user, console-based academic project built using Python functions, modules, lists, dictionaries and date handling. It does not use a database or save data to files. All records are lost when the program closes, so it demonstrates the workflow but does not yet fully replace a permanent register.

Starting a new cycle clears all attendance and payments, including any unpaid balance or advance. These amounts are not automatically carried forward. Worker details are retained only while the program remains running.

## Expected Outcome

The project aims to simplify attendance and wage calculations, reduce repeated manual work and provide a clear view of each worker's current balance. It applies introductory Python concepts to a practical problem observed in my father's work.
