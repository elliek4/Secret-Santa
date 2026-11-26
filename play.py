import random
import time

# intro
print()
print("Welcome to the Secret Santa game!")
print("Let's get started!")
print()
print("Please enter the full names of the participants:")

participants = []
assignments = [] # keeps track of who hasn't been assigned

while True:
    name = input("Enter your full name or done to finish: ")
    if name.lower() == 'done':
        break
    participants.append(name.casefold())
    assignments.append(name.casefold())

print()
print("Participants entered:")
for index, participant in enumerate(participants):
    print(f"{index + 1}. {participant}")
print()
print("Now let's assign Secret Santa partners!")


for participant in participants:
    print()
    print(f"Assigning Secret Santa for {participant}")
    print()
    input("Press Enter to continue:")
    print()

    # Extract the current participant's last name using your loop method
    participant_last = ""
    found_space = False
    for letter in range(len(participant)):
        if found_space:
            participant_last += participant[letter]
        if letter > 0 and participant[letter - 1] == " ":
            found_space = True
            participant_last += participant[letter]

    # Pick a random assignment and get their last name
    assignment = random.choice(assignments)
    last_name = ""
    found_space = False
    for letter in range(len(assignment)):
        if found_space:
            last_name += assignment[letter]
        if letter > 0 and assignment[letter - 1] == " ":
            found_space = True
            last_name += assignment[letter]

    # Keep picking if it's yourself or someone with the same last name
    while (assignment == participant) or (last_name == participant_last):
        assignment = random.choice(assignments)
        last_name = ""
        found_space = False
        for letter in range(len(assignment)):
            if found_space:
                last_name += assignment[letter]
            if letter > 0 and assignment[letter - 1] == " ":
                found_space = True
                last_name += assignment[letter]

    print(f"You got {assignment}")
    assignments.remove(assignment)
    print("This will disappear in 5 seconds")
    seconds = 5
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r", flush=True)
        time.sleep(1)
        seconds -= 1
    print("\033[H\033[J", end="")  # Clear the screen
    print()
    print("Next participant:")
    

print("All Secret Santa assignments are complete!")
print("Thank you for playing!")
print("Happy Holidays!")
print()