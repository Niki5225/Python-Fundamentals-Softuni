followers = {}
while True:
    line = input()
    if line == "Log out":
        break
    command = line.split(": ")
    type_action = command[0]
    username = command[1]
    if type_action == "New follower":
        if username not in followers.keys():
            followers[username] = [0, 0]
    elif type_action == "Like":
        likes = int(command[2])
        if username not in followers.keys():
            followers[username] = [0, 0]
        followers[username][0] += likes
    elif type_action == "Blocked":
        if username not in followers.keys():
            print(f"{username} doesn't exist.")
        else:
            del followers[username]
    elif type_action == "Comment":
        if username not in followers.keys():
            followers[username] = [0, 0]
        followers[username][1] += 1
print(f"{len(followers)} followers")
for key in followers.keys():
    total = int(followers[key][0]) + int(followers[key][1])
    print(f"{key}: {total}")
