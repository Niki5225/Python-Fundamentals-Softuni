electrons = int(input())
current_electron_shell = 1
electron_shells = []
while True:
    if electrons == 0:
        break
    formula = 2 * current_electron_shell ** 2
    if electrons >= formula:
        electrons -= formula
        electron_shells.append(formula)
        current_electron_shell += 1
    else:
        electron_shells.append(electrons)
        break
print(electron_shells)
