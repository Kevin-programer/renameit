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
    return 0

# print help
def print_help():
    print_header("Help for ReNameIt")
    print("User Input > Description what will happen")
    print("(1) exit       > will close/end the script")
    print("(2) help       > will print this help")
    print("(3) simple     > will start the simple rename function")
    return 0

# simple rename function
def simple_rename():
    fotos_path = get_path()
    print(fotos_path)
    pictures = get_file_names(fotos_path)
    print(pictures)
    pass

# ask user for path to directory with pictures
def get_path():
    failed_cnt = 0
    user_input_path = ''
    while True:
        user_input_path = input("Please enter the path to the directory of your fotos:")
        if os.path.isdir(user_input_path):
            return user_input_path
        else:
            failed_cnt += 1
            if failed_cnt > 3:
                return None

# 
def get_file_names(path):
    pictures = []
    pic_type_heic_cnt = 0
    pic_type_jpg_cnt = 0
    for file in os.listdir(path):
        if file.lower().count('.heic') > 0:
            pic_type_heic_cnt += 1
            print(file)
            pictures.append(file)
        elif file.lower().count('.jpg') > 0:
            pic_type_jpg_cnt += 1
            print(file)
            pictures.append(file)
    
    return pictures


# main task
main()