# Multi-Stage ATM Transaction Audit

# Initial account balances
accounts = {
    "A101": 5000,
    "A102": 3000
}

# Transaction format: (type, account, amount, target_account)
transactions = [
    ("deposit", "A101", 2000, None),
    ("withdraw", "A101", 1000, None),
    ("transfer", "A101", 500, "A102"),
    ("withdraw", "A102", 10000, None),
    ("deposit", "A101", -500, None),
    ("withdraw", "A101", 500, None),
    ("withdraw", "A101", 500, None),
    ("withdraw", "A101", 500, None)
]

# Store transaction history
history = []
withdrawal_history = {}

print("ATM TRANSACTION AUDIT")
print("----------------------")

for transaction in transactions:

    operation, account, amount, target = transaction

    print("\nTransaction:", operation)
    print("Account:", account)
    print("Amount:", amount)

    # Check whether the account exists
    if account not in accounts:
        print("Invalid transaction: Account not found")
        continue

    # Check whether the amount is positive
    if amount <= 0:
        print("Invalid transaction: Amount must be positive")
        continue

    # Deposit operation
    if operation == "deposit":
        accounts[account] += amount
        print("Deposit successful")

    # Withdrawal operation
    elif operation == "withdraw":

        if amount > accounts[account]:
            print("Invalid transaction: Insufficient balance")
            continue

        accounts[account] -= amount

        withdrawal_history[account] = (
            withdrawal_history.get(account, 0) + 1
        )

        print("Withdrawal successful")

        # Detect repeated withdrawals
        if withdrawal_history[account] >= 3:
            print("Warning: Repeated withdrawals detected")

    # Transfer operation
    elif operation == "transfer":

        if target not in accounts:
            print("Invalid transaction: Target account not found")
            continue

        if amount > accounts[account]:
            print("Invalid transaction: Insufficient balance")
            continue

        accounts[account] -= amount
        accounts[target] += amount

        print("Transfer successful to", target)

    else:
        print("Invalid transaction type")
        continue

    # Record successful transactions
    history.append(transaction)

    print("Updated balance of", account, ":", accounts[account])

# Display final account balances
print("\nFINAL ACCOUNT BALANCES")
print("----------------------")

for account, balance in accounts.items():
    print(account, ":", balance)

# Display audit summary
print("\nAUDIT SUMMARY")
print("-------------")
print("Total transactions received:", len(transactions))
print("Successful transactions:", len(history))
print("Invalid transactions:", len(transactions) - len(history))
