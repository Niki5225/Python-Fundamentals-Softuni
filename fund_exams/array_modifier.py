def swap(index1, index2):
    array[index1], array[index2] = array[index2], array[index1]


def multiply(ind1, ind2):
    multiplied_element = array[ind1] * array[ind2]
    array[ind1] = multiplied_element


array = list(map(int, input().split(" ")))
current_command = input()
while True:
    if current_command == "end":
        break
    command = current_command.split(" ")
    type_of_command = command[0]
    if type_of_command == "swap":
        first_index = int(command[1])
        second_index = int(command[2])
        swap(first_index, second_index)
    elif type_of_command == "multiply":
        index_1 = int(command[1])
        index_2 = int(command[2])
        multiply(index_1, index_2)
    elif type_of_command == "decrease":
        for element in range(len(array)):
            array[element] -= 1
    current_command = input()
array_str = [str(num) for num in array]
print(", ".join(array_str))
