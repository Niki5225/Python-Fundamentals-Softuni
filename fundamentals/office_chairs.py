def chairs_checker(rooms):
    needed_chairs = 0
    left_chairs = 0
    for room in range(1, rooms + 1):
        command = input().split(" ")
        chairs = len(command[0])
        visitors = int(command[1])
        diff = abs(chairs - visitors)
        if chairs < visitors:
            print(f"{diff} more chairs needed in room {room}")
            needed_chairs += diff
        else:
            left_chairs += diff
    return needed_chairs, left_chairs


current_rooms = int(input())
needed_chairs, left_chairs = chairs_checker(current_rooms)
if left_chairs >= needed_chairs:
    print(f"Game On, {left_chairs - needed_chairs} free chairs left")
