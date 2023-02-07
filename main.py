__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# My code
import os
from zipfile import ZipFile

cache_folder_name = "cache"
zip_file = "\data.zip"
folder_path = os.path.dirname(__file__)
cache_path = os.path.join(folder_path, cache_folder_name)


def clean_cache():
    isExist = os.path.exists(cache_path)
    if not isExist:
        os.makedirs(cache_path)
    else:
        for file in os.scandir(cache_path):
            os.remove(file.path)


# clean_cache()


def cache_zip(zip_file_path, cache_folder_path):
    with ZipFile(zip_file_path, 'r') as zip_Object:
        clean_cache()
        zip_Object.extractall(path=cache_folder_path)


# cache_zip(folder_path+zip_file, cache_path)


def cached_files():
    cache_list = []
    for file in os.listdir(cache_path):
        path = os.path.join(cache_path, file)
        if os.path.isfile(path):
            cache_list.append(path)
    return cache_list


# cached_files()

def find_password(list_of_files=cached_files()):
    for file in list_of_files:
        with open(file) as f:
            for line in f:
                if "password" in line:
                    return line.strip()[10:]


# print(find_password())
