# ---------------------------------------------------------------
# VERZWEIGUNGEN
# ---------------------------------------------------------------
def verzweigungen():

    # Aufgabe 1 (1 Punkt)
    # Welchen Datentyp gibt input() zurück?
    # Was muss gemacht werden, damit mit der Eingabe gerechnet werden kann?
    # Schreibe deine Antwort als Kommentar.


    # Aufgabe 2 (4 Punkte)
    # Frage den User nach seinem Alter und berechne den Eintrittspreis:
    #   unter 16    12 CHF
    #   16 bis 64   22 CHF
    #   ab 65       15 CHF
    # Gib den Preis wie folgt aus:   Eintritt: 22 CHF


    # Aufgabe 3 (2 Punkte)
    # Ein Alter kleiner als 0 oder grösser als 120 ist ungültig.
    # Gib in diesem Fall "Ungültiges Alter" aus und keinen Preis.

    pass


# ---------------------------------------------------------------
# SCHLEIFEN
# ---------------------------------------------------------------
def schleifen():

    # Aufgabe 4 (2 Punkte)
    # Frage den User nach der Anzahl Aufwärmrunden.
    # Gib mit einer for-Schleife für jede Runde eine Zeile aus,
    # danach "Aufwärmen beendet!".
    #   Anzahl Aufwärmrunden: 3
    #   Runde 1 von 3
    #   Runde 2 von 3
    #   Runde 3 von 3
    #   Aufwärmen beendet!


    # Aufgabe 5 (4 Punkte)
    # Die Kasse erfasst die Besucherzahlen pro Stunde.
    # Lies mit einer while-Schleife so lange Zahlen ein, bis 0 eingegeben wird.
    # Gib danach die Anzahl Stunden, das Total und den Durchschnitt pro Stunde aus.
    # Wird gleich zu Beginn 0 eingegeben, soll "Keine Daten erfasst." erscheinen.
    # Achtung: Eine Division durch 0 ist nicht erlaubt.
    #   Besucher in dieser Stunde (0 = Ende): 12
    #   Besucher in dieser Stunde (0 = Ende): 20
    #   Besucher in dieser Stunde (0 = Ende): 9
    #   Besucher in dieser Stunde (0 = Ende): 0
    #   Stunden: 3
    #   Total Besucher: 41
    #   Durchschnitt pro Stunde: 13.7


    # Aufgabe 6 (1 Punkt)
    # Wann verwendest du eine for-Schleife und wann eine while-Schleife?
    # Schreibe deine Antwort als Kommentar.

    pass


# ---------------------------------------------------------------
# LISTEN
# ---------------------------------------------------------------
def listen():
    # Die Liste enthält die Schwierigkeitsgrade aller Routen in der Kletter-Halle.
    # Die erste Route hat den Grad 3, die zweite den Grad 5 und so weiter.
    grade = [3, 5, 7, 4, 2, 8, 6, 5]

    # Aufgabe 7 (2 Punkte)
    # Gib die Anzahl Routen aus.
    # Gib den ersten und den letzten Grad aus.
    # Der letzte Grad darf nicht mit einer fixen Zahl wie grade[7] ausgelesen werden.

    # Aufgabe 8 (2 Punkte)
    # Gib die Grade der vierten, fünften und sechsten Route mit einem einzigen
    # Slicing-Ausdruck aus.
    #   [4, 2, 8]

    # Aufgabe 9 (3 Punkte)
    # Gib den höchsten und den tiefsten Grad aus.
    # Gib den Durchschnittsgrad aus.

    # Aufgabe 10 (3 Punkte)
    # Gib alle Routen mit einem Grad von 6 oder höher in diesem Format aus.
    # Die erste Route in der Liste ist Route 1.
    #   Route 3: Grad 7
    #   Route 6: Grad 8
    #   Route 7: Grad 6

    # Aufgabe 11 (2 Punkte)
    # Hänge eine neue Route mit dem Grad 1 an die Liste an.
    # Gib danach die Anzahl Routen erneut aus.

    pass


# ---------------------------------------------------------------
# FUNKTIONEN
# ---------------------------------------------------------------
# Die Funktionen geben ihr Ergebnis mit return zurück.
# Sie enthalten kein print() und kein input().

# Aufgabe 12 (3 Punkte)
# Die Funktion eintrittspreis() gibt den Preis gemäss Aufgabe 2 zurück.
# Bei einem ungültigen Alter wird 0 zurückgegeben.
def eintrittspreis(alter):
    pass


# Aufgabe 13 (3 Punkte)
# Die Funktion durchschnitt() gibt den Durchschnitt einer Zahlenliste zurück.
# Ist die Liste leer, wird 0 zurückgegeben.
def durchschnitt(zahlen):
    pass


# Aufgabe 14 (4 Punkte)
# Die Funktion schwierige_routen() gibt eine neue Liste mit allen Graden zurück,
# die grösser oder gleich grenze sind.
def schwierige_routen(grade, grenze):
    pass


# Aufgabe 15 (4 Punkte)
# Die Funktion gruppenpreis() erhält eine Liste mit dem Alter aller Personen
# einer Gruppe und gibt den Gesamtpreis zurück.
# Verwende dafür deine Funktion eintrittspreis().
# Ab 5 Personen gibt es 10 % Rabatt.
def gruppenpreis(alter_liste):
    pass


def funktionen():
    # Testaufrufe – nicht verändern
    grade = [3, 5, 7, 4, 2, 8, 6, 5]

    print(eintrittspreis(10))  # erwartet: 12
    print(eintrittspreis(30))  # erwartet: 22
    print(eintrittspreis(70))  # erwartet: 15
    print(eintrittspreis(-3))  # erwartet: 0
    print(durchschnitt([3, 5, 7, 4]))  # erwartet: 4.75
    print(durchschnitt([]))  # erwartet: 0
    print(schwierige_routen(grade, 6))  # erwartet: [7, 8, 6]
    print(schwierige_routen(grade, 9))  # erwartet: []
    print(gruppenpreis([30, 30, 10]))  # erwartet: 56
    print(gruppenpreis([30, 30, 10, 10, 70]))  # erwartet: 74.7
