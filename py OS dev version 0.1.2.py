print("Welcome to py OS dev version 0.1.2")
print("Made by Arnav Jaiswal")
print("Updated version of py OS dev version 0.1.1")
print("Updated on 19-6-2025")

while True:
    command = input('pyos>  ').strip().lower()

    if command == "help":
        print("commands --")
        print("help")
        print("about")
        print("what's new")
        print("exit")

    elif command == "about":
        print("py OS dev version 0.1.2")
        print("Updated version of py OS dev version 0.1.1")
        print("Made by Arnav Jaiswal on 19-6-2025")
        print("Kernel version 1.0.1")

    elif command == "what's new":
        print("----------what's new---------")
        print("New kernel version")
        print("Infinite commands operable unless you had done exit")

    elif command == "exit":
        input('press enter to exit...')
        break

    else:
        print("bad command")