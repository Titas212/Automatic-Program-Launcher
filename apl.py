import os
import win32api
import re
import schedule
import time
import argparse
""" import os and import win32api leidžia programai komunikuoti su kompiuterio sistema (Pvz. Windows).
    import re
    import schedule and time leižia programai nustatyti tam tikrą programos įjungimo laiką.
    import argparse surenka įvestus žodžius iš terminal ir įdeda juos į argumentus. """

class PrintPath:
    def __init__(self, pavadinimas):    
        self.pavadinimas = pavadinimas
    

    def _find_file_path(self, root_folder, rex):
        for subdir, dirs, files in os.walk(root_folder):
            for file in files:
                result = rex.search(file)
                if result:
                    return print('Jūsų programa yra: ' + os.path.join(subdir, file))
    
    
    def find_file_path_in_all_drives(self, pavadinimas):
        rex = re.compile(self.pavadinimas)
        for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
            self._find_file_path(drive, rex)
    
    
    def print_path(self):
        self.find_file_path_in_all_drives(self.pavadinimas)


class FindingProgram:
    def __init__(self, scheduler, laikas, pavadinimas):
        self.scheduler = schedule
        self.laikas = laikas
        self.pavadinimas = pavadinimas
        

    def _find_file(self, root_folder, rex):
        for subdir, dirs, files in os.walk(root_folder):
            for file in files:
                result = rex.search(file)
                if result:
                    os.startfile(os.path.join(subdir, file))
    """Ši funkcija ieško norimos programos įvairiuose failuose."""


    def find_file_in_all_drives(self, pavadinimas):
        rex = re.compile(self.pavadinimas)
        for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
            self._find_file(drive, rex)
    """Ši funkcija leidžia funkcijai find_file veikti kompiuterio drivuose (Pvz. Ieško norimos programos C Drive)."""


    def run_program(self):

        self.scheduler.every().days.at(self.laikas).do(self.find_file_in_all_drives, self.pavadinimas)
    """Panaudojami import schedule ir import time ir nustatomas programos įsijungimo laikas, bei kokia programa bus įjungta."""

    
    def ivestu_duomenu_print(self):
        return print('Jūsų programa: ' + self.pavadinimas + ' bus įjungta ' + self.laikas + '.')
    """Į terminalą išvedamas jūsų programos pavadinimas ir kada ji bus įjungta."""


def testing_print(pavadinimas1, laikas1):
    if laikas1 == None:
        return 'Jūsų programa: ' + pavadinimas1 + ' bus įjungta.'
    elif pavadinimas1 == None:
        return 'Įveskite programos pavadinimą.'
    elif pavadinimas1 == '' and laikas1 == '':
        return 'Įveskite programos pavadinimą ir jos įjungimo laiką.'
    elif pavadinimas1 == int and laikas1 == int:
        return 'Įveskite programos pavadinimą ir jos įjungimo laiką.'
    else:
        return 'Jūsų programa: ' + pavadinimas1 + ' bus įjungta ' + laikas1 + '.'



def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('pavadinimas', help = 'Irasykite programos pavadinima')
    """Patalpina įrašytą pavadinimą į argument."""

    parser.add_argument('laikas', help = 'Irasykite programos paleidimo laiką', type = str)
    """Patalpina įrašytą laiką į argument."""

    args = parser.parse_args()
    pavadinimas = args.pavadinimas
    laikas = args.laikas

    finding_program_class = FindingProgram(scheduler = schedule, laikas = laikas, pavadinimas = pavadinimas)
    printing_program_path = PrintPath(pavadinimas = pavadinimas)
    """Pavadinimo ir laiko argumentai patalpinami į kintamuosius."""
    printing_program_path.print_path()
    finding_program_class.run_program()
    finding_program_class.ivestu_duomenu_print()
    while True:
            schedule.run_pending()
            time.sleep(10)
    """Šis while ciklas verčia programos įjungimo funkciją laukti iki tam tikro laiko."""

if __name__ == '__main__':
    main()
