notes = []

while True:
    command = input("Enter keyword: ")
    if command == "add":
        note = input("Enter note: ")
        notes.append(note)
    elif command == "earliest":
        print("\n".join(notes))
    elif command == "latest":
        print("\n".join(notes[::-1]))
    elif command == "longest":
        print("\n".join(sorted(notes, key=len, reverse=True)))
    elif command == "shortest":
        print("\n".join(sorted(notes, key=len)))
    elif command == "Exit":
        break
    else:
        print("Unknown command")