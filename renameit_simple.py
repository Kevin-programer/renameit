# simple rename script

import sys
import os
import logging

# logger config
logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
formatter_stream = logging.Formatter("[%(asctime)s] {%(levelname)s} - %(message)s")
stream_handler.setFormatter(formatter_stream)
logger.addHandler(stream_handler)
file_handler = logging.FileHandler('renameit_simple_log.txt')
formatter_file = logging.Formatter("[%(asctime)s] {%(levelname)s} %(name)s: #%(lineno)d - %(message)s")
file_handler.setFormatter(formatter_file)
logger.addHandler(file_handler)

# set the logging level
logger.setLevel(logging.WARNING)

def main():
    args = sys.argv
    if len(args) != 3:
        logger.warning(f"Too few arguments passed.")
        return 1
    logger.debug(f"Arguments: {args}")
    path = args[1]
    prefix = args[2]
    if os.path.exists(path):
        logger.debug(f"Path exists: {path}")
    else:
        logger.debug(f"Path does not exist: {path}")
        return 2
    
    files = os.listdir(path)
    logger.debug(f"Files in path: {files}")
    cnt = 0
    for file in files:
        cnt += 1
        # get file extension
        file_extension = file[file.find("."):]

        new_file_name = prefix + "_" + str(cnt).zfill(3) + file_extension
        logger.debug(f"File {file} will be renamed to {new_file_name}")
        os.rename(path + "/"+ file, path + "/" + new_file_name)

    return 0





main()