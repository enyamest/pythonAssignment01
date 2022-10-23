print("Ahmed Capstone Financial Statement")
print()

CAPSTONE_INVESTMENT = 50_000  # 50,000 GHC

CURRENCY_FORMAT = "GHC {:0,.2f}"

print(f"Investment =  {CURRENCY_FORMAT.format(CAPSTONE_INVESTMENT)}")
print()

marketing_expenses_amount = CURRENCY_FORMAT.format(CAPSTONE_INVESTMENT * 0.25)
print(f"Marketing expenses = {marketing_expenses_amount}")
print()


operational_expense_amount = CURRENCY_FORMAT.format(CAPSTONE_INVESTMENT * 0.50)
print(f"Operational expenses = {operational_expense_amount}")
print()


user_acquisition_amount = CAPSTONE_INVESTMENT * 0.25
user_acquisition_amount_formatted = CURRENCY_FORMAT.format(user_acquisition_amount)
print(f"Users acquisition expenses = {user_acquisition_amount_formatted}")
print()

print(f"Cost to acquire one user = GHC 5.00")
print()

number_users_acquired = user_acquisition_amount/5
print(f"Number of users that can be acquired = {int(number_users_acquired):,}")