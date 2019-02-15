import os

# Directory paths
UTIL_DIRECTORY = os.getcwd()

PROJECT_DIRECTORY = os.path.abspath(os.path.join(UTIL_DIRECTORY, os.pardir))

UTIL_DIRECTORY = UTIL_DIRECTORY.replace("\\", "/")
PROJECT_DIRECTORY = PROJECT_DIRECTORY.replace("\\", "/")

FILES_DIRECTORY = PROJECT_DIRECTORY + '/attachment_files'
if not os.path.exists(FILES_DIRECTORY):
    PROJECT_DIRECTORY = UTIL_DIRECTORY
    FILES_DIRECTORY = PROJECT_DIRECTORY + '/attachment_files'
SOURCE_FILES_DIRECTORY = PROJECT_DIRECTORY + '/source_files'
OTHER_DIRECTORY = PROJECT_DIRECTORY, '/other_files'


def create_random_string(size=30):
    """
                    Generate a random string of size 30 by default
    :param size:
    :return:
    """
    import random
    import string
    rand_str = lambda n: ''.join([random.choice(string.ascii_lowercase) for i in range(n)])
    return rand_str(size)


def copy_file(source, dest):
    """
                    Copy a file from the source path to destination path
    :param source: Path of a source file
    :param dest: Path of the destination file
    :return: Path of the copied file
    """
    import shutil
    file = source.split("/")[-1]
    file_name = file.split(".")[0]
    file_extension = file.split(".")[-1]
    if dest == "attachment":
        directory = FILES_DIRECTORY
    elif dest == "source_file":
        directory = SOURCE_FILES_DIRECTORY
    else:
        directory = OTHER_DIRECTORY

    if not os.path.exists(directory):
        os.makedirs(directory)
    destination = directory + "/" + file_name + "_" + create_random_string() + "." + file_extension
    shutil.copy(source, destination)
    shutil.copystat(source, destination)
    return destination
