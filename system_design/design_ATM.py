"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

Requirements and Goals of the System #
The main components of the ATM that will affect interactions between the ATM and its users are:
Card reader: to read the users’ ATM cards.
Keypad: to enter information into the ATM e.g. PIN. cards.
Screen: to display messages to the users.
Cash dispenser: for dispensing cash.
Deposit slot: For users to deposit cash or checks.
Printer: for printing receipts.
Communication/Network Infrastructure: it is assumed that the ATM has a communication infrastructure to communicate with the bank upon any transaction or activity.
The user can have two types of accounts: 1) Checking, and 2) Savings, and should be able to perform the following five transactions on the ATM:

Balance inquiry: To see the amount of funds in each account.
Deposit cash: To deposit cash.
Deposit check: To deposit checks.
Withdraw cash To withdraw money from their checking account.
Transfer funds: To transfer funds to another account.

Here are the actors of the ATM system and their use cases:

Operator: The operator will be responsible for the following operations:

Turning the ATM ON/OFF using the designated Key-Switch.
Refilling the ATM with cash.
Refilling the ATM’s printer with receipts.
Refilling the ATM’s printer with INK.
Take out deposited cash and checks.

Customer: The ATM customer can perform the following operations:

Balance inquiry: the user can view his/her account balance.
Cash withdrawal: the user can withdraw a certain amount of cash.
Deposit funds: the user can deposit cash or checks.
Transfer funds: the user can transfer funds to other accounts.

Bank Manager: The Bank Manager can perform the following operations:

Generate a report to check total deposits.
Generate a report to check total withdrawals.
Print total deposits/withdrawal reports.
Checks the remaining cash in the ATM.

"""


