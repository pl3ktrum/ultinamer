import os


def _walk():
    for root, dirs, files in os.walk():
        print(root, dirs, files)