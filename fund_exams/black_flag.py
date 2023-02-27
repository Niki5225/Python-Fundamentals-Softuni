days_of_the_purge = int(input())
daily_purge = int(input())
expected_purge = int(input())
total_gain = 0
for day in range(1, days_of_the_purge + 1):
    total_gain += daily_purge
    if day % 3 == 0:
        total_gain += 0.5 * daily_purge
    if day % 5 == 0:
        total_gain -= 0.3 * total_gain
if total_gain >= expected_purge:
    print(f"Ahoy! {total_gain:.2f} plunder gained.")
else:
    percentage = (total_gain / expected_purge) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")