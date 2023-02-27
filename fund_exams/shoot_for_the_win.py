def reduce_values(target_sequence, index):
    current_target = target_sequence[index]
    target_sequence[index] = -1
    for current_index in range(len(target_sequence)):
        if target_sequence[current_index] == -1:
            continue
        if target_sequence[current_index] <= current_target:
            target_sequence[current_index] += current_target
        else:
            target_sequence[current_index] -= current_target
    return target_sequence


def shoot_for_the_win(target_sequence):
    count_targets = 0
    while True:
        command = input()
        if command == "End":
            break
        index = int(command)
        if 0 <= index < len(target_sequence) and index != -1:
            count_targets += 1
            reduce_values(target_sequence, index)
    convert_into_string = [str(num) for num in target_sequence]
    print(f"Shot targets: {count_targets} -> {' '.join(convert_into_string)}")


data = list(map(int, input().split(" ")))
shoot_for_the_win(data)
