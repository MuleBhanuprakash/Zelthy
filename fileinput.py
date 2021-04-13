import errno
import os
from datetime import datetime


def creation(i, filename):
    mydir = os.path.join(
        os.getcwd(),
        datetime.now().strftime('%d-%m-%y'))
    try:
        os.makedirs(mydir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise  # This was not a "directory exist" error..
    with open(os.path.join(mydir, filename), 'w') as d:
        d.writelines(i)


i = input("please enter file details:")
creation(i, filename='file.txt')
