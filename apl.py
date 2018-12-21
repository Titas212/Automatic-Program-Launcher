import os
import win32api
import re
import schedule
import time
import argparse
import this
""" import os and import win32api leidžia programai komunikuoti su kompiuterio sistema (Pvz. Windows).
    import re sukompiliuoja įvestą programos pavadinimą.
    import schedule and time leižia programai nustatyti tam tikrą programos įjungimo laiką.
    import argparse surenka įvestus žodžius iš terminal ir įdeda juos į argumentus. """

class PrintPath:
    def __init__(self, pavadinimas):    
        self.pavadinimas = pavadinimas
    

    def _find_file_path(self, root_folder, rex):
        for subdir, _, files in os.walk(root_folder):
            for file in files:
                result = rex.search(file)
                if result:
                    return print('Jūsų programa yra: ' + os.path.join(subdir, file))
    
    
    def find_file_path_in_all_drives(self, pavadinimas):
        rex = re.compile(self.pavadinimas)
        for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
            self._find_file_path(drive, rex)
    
    
    def print_path(self):
        """Ši funkcija į terminalą išveda jūsų norimos programos path.""" 
        self.find_file_path_in_all_drives(self.pavadinimas)
    


class FindingProgram:
    def __init__(self, scheduler, laikas, pavadinimas):
        self.scheduler = schedule
        self.laikas = laikas
        self.pavadinimas = pavadinimas
        

    def _find_file(self, root_folder, rex):
        """Ši funkcija ieško norimos programos įvairiuose failuose."""
        for subdir, _, files in os.walk(root_folder):
            for file in files:
                result = rex.search(file)
                if result:
                    os.startfile(os.path.join(subdir, file))
    


    def find_file_in_all_drives(self, pavadinimas):
        """Ši funkcija leidžia funkcijai find_file veikti kompiuterio drivuose (Pvz. Ieško norimos programos C Drive)."""
        rex = re.compile(self.pavadinimas)
        for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
            self._find_file(drive, rex)
   


    def run_program(self):
        """Panaudojami import schedule ir import time ir nustatomas programos įsijungimo laikas, bei kokia programa bus įjungta."""
        self.scheduler.every().days.at(self.laikas).do(self.find_file_in_all_drives, self.pavadinimas)
    

    
    def ivestu_duomenu_print(self):
        """Į terminalą išvedamas jūsų programos pavadinimas ir kada ji bus įjungta."""
        return print('Jūsų programa: ' + self.pavadinimas + ' bus įjungta ' + self.laikas + '.')
    


def testing_print(pavadinimas1, laikas1):
    """ Ši funkcija yra skirta testavimui """
    pavadinimas1_type = type(pavadinimas1)
    if laikas1 == None:
        return 'Jūsų programa: ' + pavadinimas1 + ' bus įjungta.'
    elif pavadinimas1 == None:
        return 'Įveskite programos pavadinimą.'
    elif pavadinimas1 == '' and laikas1 == '':
        return 'Įveskite programos pavadinimą ir jos įjungimo laiką.'
    elif pavadinimas1_type == int:
        return 'Įveskite programos pavadinimą ir jos įjungimo laiką.'
    else:
        return 'Jūsų programa: ' + pavadinimas1 + ' bus įjungta ' + laikas1 + '.'
 



def main():

    parser = create_parser()
    args = parser.parse_args()
    pavadinimas = args.pavadinimas
    laikas = args.laikas
    """Pavadinimo ir laiko argumentai patalpinami į kintamuosius."""
    tikrasis_laikas = laiko_patikrinimas(laikas)
    tikrasis_pavadinimas = pavadinimo_patikrinimas(pavadinimas)
    printing_program_path = PrintPath(pavadinimas = tikrasis_pavadinimas)
    finding_program_class = FindingProgram(scheduler = schedule, laikas = tikrasis_laikas, pavadinimas = pavadinimas)
    """Pavadinimo ir laiko argumentai patalpinami į kintamuosius."""
    funkciju_atlikimas_su_tikrom_reiksmem(tikrasis_pavadinimas, tikrasis_laikas, printing_program_path, finding_program_class)

    while True:
        """Šis while ciklas verčia programos įjungimo funkciją laukti iki tam tikro laiko."""
        schedule.run_pending()
        time.sleep(10)
    

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('pavadinimas', nargs='?', help = 'Irasykite programos pavadinima')
    """Patalpina įrašytą pavadinimą į argument."""
    parser.add_argument('laikas', nargs='?', help = 'Irasykite programos paleidimo laiką', type = str)
    """Patalpina įrašytą laiką į argument."""
    return parser


def laiko_patikrinimas(laikas):
    if laikas is None:
        laikas = '(Laikas neįvestas)'
        return laikas
    else:
        return laikas
def pavadinimo_patikrinimas(pavadinimas):
    try:
        int(pavadinimas)
        pavadinimas = '(Pavadinimas negali būti sudarytas tik iš skaičių)'
    except:
        pass
    if pavadinimas is None:
        pavadinimas = '(Pavadinimas neįvestas)'
        return pavadinimas
    else:
        return pavadinimas
def funkciju_atlikimas_su_tikrom_reiksmem(tikrasis_pavadinimas, tikrasis_laikas, printing_program_path, finding_program_class):
    if tikrasis_laikas == None:
        printing_program_path.print_path
    elif tikrasis_pavadinimas == None:
        print(tikrasis_pavadinimas)
    else:
        printing_program_path.print_path
        finding_program_class.ivestu_duomenu_print()
        finding_program_class.run_program()
    

if __name__ == '__main__':
    main()
