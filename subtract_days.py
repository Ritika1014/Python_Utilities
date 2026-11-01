from datetime import datetime, timedelta

print("Date Subtraction Demo")
print("=" * 25)

current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)

print(f"Current date: {current_date.strftime('%Y-%m-%d')}")
print(f"Date five days ago: {five_days_ago.strftime('%Y-%m-%d')}")

print("\nDone!")
