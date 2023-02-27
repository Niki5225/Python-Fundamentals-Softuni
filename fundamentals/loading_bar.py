def loading_bar(number):
    state_of_the_bar = []
    symbols_for_changing = number // 10
    for symbol in range(0, symbols_for_changing):
        state_of_the_bar.append('%')
    return state_of_the_bar


current_number = int(input())
final_state_of_the_bar = loading_bar(current_number)

for _ in range(len(final_state_of_the_bar), 10):
    final_state_of_the_bar.append('.')
complete = True
for element in final_state_of_the_bar:
    if element != '%':
        complete = False
        break
final_state_of_the_bar_opened = "".join(final_state_of_the_bar)
if current_number != 100:
    print(f"{current_number}% [{final_state_of_the_bar_opened}]")
    print("Still loading...")
else:
    print(f"{current_number}% Complete!")
    print(f"[{final_state_of_the_bar_opened}]")
