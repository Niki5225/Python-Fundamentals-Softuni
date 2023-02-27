def increasing_or_decreasing(state_distances, current_element):
    current_index = 0
    for element in distances:
        if element <= current_element:
            element += current_element
            state_distances[current_index] = element
        else:
            element -= current_element
            state_distances[current_index] = element
        current_index += 1
    return state_distances


distances = list(map(int, input(). split(" ")))
removed_elements_value = 0
while len(distances) > 0:
    index = int(input())
    if 0 <= index < len(distances):
        current_element = distances.pop(index)
        removed_elements_value += current_element
        distances = increasing_or_decreasing(distances, current_element)
    elif index < 0:
        current_element = distances[0]
        removed_elements_value += current_element
        distances = increasing_or_decreasing(distances, current_element)
        distances[0] = distances[-1]
    elif index >= len(distances):
        current_element = distances[-1]
        removed_elements_value += distances[-1]
        distances = increasing_or_decreasing(distances, current_element)
        distances[-1] = distances[0]
print(removed_elements_value)
