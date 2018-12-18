import os
UTIL_DIRECTORY = os.getcwd()
PROJECT_DIRECTORY = os.path.abspath(os.pardir)
FILES_DIRECTORY = PROJECT_DIRECTORY + '/attachment_files'
SOURCE_FILES_DIRECTORY = PROJECT_DIRECTORY + '/source_files'
OTHER_DIRECTORY = PROJECT_DIRECTORY + '/other_files'


def create_random_string(size=30):
    import random
    import string
    rand_str = lambda n: ''.join([random.choice(string.ascii_lowercase) for i in range(n)])
    return rand_str(size)


def copy_file(source, dest):
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
    destination = directory + "/" + file_name + "_" + create_random_string() + "." + file_extension
    shutil.copy(source, destination)
    shutil.copystat(source, destination)
    return destination
