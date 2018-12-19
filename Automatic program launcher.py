import os
import win32api
import re
import schedule
import time
import argparse
# import os and import win32api leidžia programai komunikuoti su kompiuterio sistema (Pvz. Windows).
# import re
# import schedule and time leižia programai nustatyti tam tikrą programos įjungimo laiką.
# import argparse surenka įvestus žodžius iš terminal ir įdeda juos į argumentus.
def find_file(root_folder, rex):
    for subdir, dirs, files in os.walk(root_folder):
        for file in files:
            result = rex.search(file)
            if result:
                os.startfile(os.path.join(subdir, file))
# Ši funkcija ieško norimos programos įvairiuose failuose.

def find_file_in_all_drives(pavadinimas):
    rex = re.compile(pavadinimas)
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        find_file( drive, rex )
# Ši funkcija leidžia funkcijai find_file veikti kompiuterio drivuose (Pvz. Ieško norimos programos C Drive).
def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('pavadinimas', help = 'Irasykite programos pavadinima')
# Patalpina įrašytą pavadinimą į argument.
    
    parser.add_argument('laikas', help = 'Irasykite programos paleidimo laiką', type = str)
# Patalpina įrašytą laiką į argument.
    
    args = parser.parse_args()
    pavadinimas = args.pavadinimas
    laikas = args.laikas
# Pavadinimo ir laiko argumentai patalpinami į kintamuosius.
    
    schedule.every().days.at(args.laikas).do(find_file_in_all_drives, pavadinimas)
# Panaudojami import schedule ir import time ir nustatomas programos įsijungimo laikas, bei kokia programa bus įjungta.
    
    print('Jūsų programa: ' + pavadinimas + ' bus įjungta ' + laikas + '.')
# Į terminalą išvedamas jūsų programos pavadinimas ir kada ji bus įjungta.
    
    while True:
        schedule.run_pending()
        time.sleep(10)
# Šis while ciklas verčia programos įjungimo funkciją laukti iki tam tikro laiko.

if __name__ == '__main__':
    main()
