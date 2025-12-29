# renameit script
import os
import logging
import sys

# logger config
logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
formatter_stream = logging.Formatter("[%(asctime)s] {%(levelname)s} - %(message)s")
stream_handler.setFormatter(formatter_stream)
logger.addHandler(stream_handler)
file_handler = logging.FileHandler('log.txt')
formatter_file = logging.Formatter("[%(asctime)s] {%(levelname)s} %(name)s: #%(lineno)d - %(message)s")
file_handler.setFormatter(formatter_file)
logger.addHandler(file_handler)

# set the logging level
logger.setLevel(logging.WARNING)

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
            logger.warning(f"Invalid Input: {user_input}")

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
    logger.debug(f"Path to pictures: {fotos_path}")
    pictures = get_file_names(fotos_path)
    logger.debug(f"Found pictures: {pictures}")
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
            logger.info(f"Invalid Input for path: {user_input_path}. Nr. of tries: {failed_cnt}")
            if failed_cnt > 3:
                logger.info(f"Path input was invalid {failed_cnt} times.")
                return None

# 
def get_file_names(path):
    pictures = []
    pic_type_heic_cnt = 0
    pic_type_jpg_cnt = 0
    for file in os.listdir(path):
        if file.lower().count('.heic') > 0:
            pic_type_heic_cnt += 1
            logger.debug(f"Valid .heic file found: {file}")
            pictures.append(file)
        elif file.lower().count('.jpg') > 0:
            pic_type_jpg_cnt += 1
            logger.debug(f"Valid .jpg file found: {file}")
            pictures.append(file)
    logger.debug(f"{pic_type_heic_cnt} .HEIC Files, {pic_type_jpg_cnt} .JPG Files")
    return pictures


# main task
main()