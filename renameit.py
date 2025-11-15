# renameit script
import os

# main function
def main():
    # show welcome message
    print_header("Welcome to ReNameIt")
    print("Enter help to get more information")
    
    while True:
        print()
        user_input = input("Please enter a command:")
        print()
        if user_input.lower() == "exit":
            break
        elif user_input.lower() == "help":
            print_help()
        elif user_input.lower() == "simple":
            simple_rename()
        else:
            print("Invalid input. Enter help for info.\n")


# print welcome
def print_header(message):
    print("+" + "-" * (len(message) + 2) + "+")
    print("| " + message + " |")
    print("+" + "-" * (len(message) + 2) + "+")
    return

# print help
def print_help():
    print_header("Help for ReNameIt")
    print("User Input > Description what will happen")
    print("exit       > will close/end the script")
    print("help       > will print this help")
    print("simple     > will start the simple rename function")
    pass

# simple rename function
def simple_rename():
    pass


# main task
main()