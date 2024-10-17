#Werte eingeben

try:
    kreditbetrag = int(input("Kreditbetrag "))
except ValueError:
    print("Das war keine gültige Zahl!")

try:
    laufzeit_jahre = int(input("Laufzeit "))
except ValueError:
    print("Das war keine gültige Zahl!")

try:
    zinssatz = int(input("Zinssatz in % "))
except ValueError:
    print("Das war keine gültige Zahl!")

#BERECHUNG

# Brechung der Monatsrate

def kreditrate_berechnen(kreditbetrag, zinssatz, laufzeit_jahre):
    # Zinssatz von Prozent in Dezimal umwandeln und monatlichen Zinssatz berechnen
    r = (zinssatz / 100) / 12
    # Anzahl der Monate berechnen
    n = laufzeit_jahre * 12
    # Annuitätenformel zur Berechnung der monatlichen Rate
    monatliche_rate = (kreditbetrag * r * (1 + r)**n) / ((1 + r)**n - 1)
    return monatliche_rate

monatliche_rate = kreditrate_berechnen(kreditbetrag, zinssatz, laufzeit_jahre)
print(f" f string: Die monatliche Rate beträgt: {monatliche_rate:.2f} Euro")







"""
#Zahlrunden
zahl = Rest
e = round(zahl, 2)
print(e)
"""
# Beispiel-Dictionary

mein_dict = {


    "Monatsrate": f" Die Monatsrate beträgt:{monatliche_rate:.2f} €",
        #Rest in Zeile ab 61
}

# Manuelle Formatierung
for key, value in mein_dict.items():
    print(f"{key}: {value}")


"""
    "Zinskosten gesamt": f"Die Monatsrate beträgt:{monatsrate}€",
    "Anuität": f"Die Monatsrate beträgt:{monatsrate}€",
    "Gesamtkosten": f"Die Gesamtkosten betragen:{sum_result}€",

try:
    bank = str(input("Bank "))
except ValueError:
    print("Das war keine gültige Wert!")

try:
    ansprechpatner = str(input("Ansprechpatner "))
except ValueError:
    print("Das war keine gültige Wert!")

#Uhrzeit
from datetime import datetime

# Aktuelles Datum und Uhrzeit
aktuelles_datum_und_uhrzeit = datetime.now()

# Formatierte Ausgabe
formatiertes_datum_und_uhrzeit = aktuelles_datum_und_uhrzeit.strftime("%Y-%m-%d %H:%M:%S")

uhrzeit = formatiertes_datum_und_uhrzeit    
print(uhrzeit)

#CSV
import csv
import os

# Pfad zur CSV-Datei
file_name = 'baurechner.csv'

# Überprüfen, ob die Datei existiert, um zu entscheiden, ob die Kopfzeile geschrieben werden muss
file_exists = os.path.exists(file_name)

# Öffne die CSV-Datei im Append-Modus ('a' steht für Anhängen)
with open(file_name, 'a', newline='') as csv_file:
    fieldnames = ['Uhrzeit', 'Monatsrate', 'Laufzeit', 'Preisempflung']

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Wenn die Datei neu erstellt wird, schreibe die Kopfzeile
    if not file_exists:
        writer.writeheader()

    # Schreibe die neuen Daten als neue Zeile
    writer.writerow({'Uhrzeit': greeting, 'Monatsrate':  f"{gerundete_zahl} €",'Laufzeit': f"{c} Monate",'Preisempflung': preis,})

#Sondertilung und Restschuld
try:
   sondertilgung = int(input("Sondertilgung "))
except ValueError:
    print("Das war keine gültige Zahl!")

#Berechnen der Restschuld
Restschuld = jahresrate - calculation_result
Restschuld = f"Die Restschuld zum Ende der Laufzeit {Restschuld} € "
print(Restschuld)

#Berechnen der Sondertilgung
sonder = sondertilgung * laufzeit
sondertilgung = f"Die Restschuld zum Ende der Laufzeit {sonder} € "
print(sondertilgung)

# Restschuld - Sondertilgung
Rest = Restschuld - sondertilgung
Rest = f"Der Rest mit Sondertilgung beträgt {Rest} € "
print(Rest)

#Zahlrunden
zahl = Rest
e = round(zahl, 2)
print(e)
"""