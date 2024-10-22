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
    zinssatz = float(input("Zinssatz in % "))
except ValueError:
    print("Das war keine gültige Zahl!")
"""
try:
    tilgen = float(input("Sondertilgung"))
except ValueError:
    print("Das war keine gültige Zahl!")
"""
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
#print(f" f string: Die monatliche Rate beträgt: {monatliche_rate:.2f} Euro")

#Berechnen der Annuität
anu = monatliche_rate * 12
#print("Die jährliche Annuität beträgt: {zinsen:. 2f} Euro")

#Berechnen der gesamten Kosten
gesamtkosten = anu * laufzeit_jahre
#print(f" f string: Die gesamten Zinsen betragen: {gesamtkosten:.2f} Euro")

#Berechnen der gesamten Zinsen
zinsen = gesamtkosten - kreditbetrag
#print(f" f string: Die gesamten Kosten betragen: {zinsen :.2f} Euro")

"""
#Berechnen der Sondertilgung
sondertilgung = tilgen * laufzeit_jahre
#print(f" f string: Die gesamten Kosten betragen: {sondertilgung:.2f} Euro")

#Berechnen der Restschuld
restschuld = gesamtkosten - sondertilgung
#print(f" f string: Die gesamten Kosten betragen: {restschuld:.2f} Euro")
"""

# Beispiel-Dictionary
# Färben des Dictionary
farbe = "\033[90m"  # Grau
reset = "\033[0m"   # Zurücksetzen der Farbe
mein_dict = {

    "Monatsrate um bei 0 zu sein": f"{farbe}Die Monatsrate beträgt: {monatliche_rate:.2f}€{reset}",
    "Meine Rate": f"{farbe}Meine persönliche Rate: {monatliche_rate:.2f}€{reset}",
    "Annuität": f"{farbe}Die jährliche Annuität beträgt: {anu:.2f}€{reset}",
    "Zinsen gesamt": f"{farbe}Die Zinsen insgesamt: {zinsen:.2f}€{reset}",
   # "Sondertilgung": f"{farbe}Die Gesamtkosten betragen: {sondertilgung:.2f}€{reset}",
  #  "Restschuld": f"{farbe}Die Gesamtkosten betragen: {restschuld:.2f}€{reset}",
    "Gesamtkosten": f"{farbe}Die Gesamtkosten betragen: {gesamtkosten:.2f}€{reset}",

}

# Manuelle Formatierung
for key, value in mein_dict.items():
    print(f"{key}: {value}")
"""
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
file_name = 'Rechner ohne Restschulden.csv'

# Überprüfen, ob die Datei existiert, um zu entscheiden, ob die Kopfzeile geschrieben werden muss
file_exists = os.path.exists(file_name)

# Öffne die CSV-Datei im Append-Modus ('a' steht für Anhängen)
with open(file_name, 'a', newline='') as csv_file:
    fieldnames = ['Monatsrate', 'Zinsen', 'Annuität']

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Wenn die Datei neu erstellt wird, schreibe die Kopfzeile
    if not file_exists:
        writer.writeheader()

    # Schreibe die neuen Daten als neue Zeile
    writer.writerow({'Monatsrate': monatliche_rate, 'Annuität': annuitaet,'Zinsen':  zinsengesamt, 'Gesamtkosten':  gesamtkosten,})
"""

