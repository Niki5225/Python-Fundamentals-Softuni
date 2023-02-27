class Party:

    def __init__(self):
        self.people = []

    def final_list(self):
        return self.people


party = Party()
while True:
    command = input()
    if command == "End":
        break
    party.people.append(command)
print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
