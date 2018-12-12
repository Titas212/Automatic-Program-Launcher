import os
import win32api
import re
# import os and import win32api leidžia programai komunikuoti su kompiuterio sistema (Pvz. Windows)
def find_file(root_folder, rex):
    for subdir, dirs, files in os.walk(root_folder):
        for file in files:
            result = rex.search(file)
            if result:
                os.startfile(os.path.join(subdir, file))
def find_file_in_all_drives(file_name):
    rex = re.compile(file_name)
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        find_file( drive, rex )
find_file_in_all_drives(input('Įveskite failo pavadinimą. '))
