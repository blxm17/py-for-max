"""
Python Datentypen Übersicht
--------------------------
"""

# Numerische Datentypen
print("1. Numerische Datentypen:")
# Integer (Ganze Zahlen)
ganze_zahl = 42
print(f"Integer: {ganze_zahl}, Typ: {type(ganze_zahl)}")

# Float (Gleitkommazahlen)
gleitkomma = 3.14
print(f"Float: {gleitkomma}, Typ: {type(gleitkomma)}")

# Complex (Komplexe Zahlen)
komplex = 1 + 2j
print(f"Complex: {komplex}, Typ: {type(komplex)}")

# Boolean (Wahrheitswerte)
print("\n2. Boolean:")
wahr = True
falsch = False
print(f"Boolean True: {wahr}, Typ: {type(wahr)}")
print(f"Boolean False: {falsch}, Typ: {type(falsch)}")

# String (Zeichenketten)
print("\n3. String:")
text = "Hallo Welt"
print(f"String: {text}, Typ: {type(text)}")
# Mehrzeiliger String
mehrzeilig = """Dies ist ein
mehrzeiliger
String"""
print(f"Mehrzeiliger String: {mehrzeilig}")

# Liste (veränderbar)
print("\n4. Liste:")
liste = [1, 2, 3, "Python", True]
print(f"Liste: {liste}, Typ: {type(liste)}")

# Tuple (unveränderbar)
print("\n5. Tuple:")
tupel = (1, 2, 3, "Python")
print(f"Tuple: {tupel}, Typ: {type(tupel)}")

# Dictionary (Schlüssel-Wert-Paare)
print("\n6. Dictionary:")
woerterbuch = {"name": "Python", "version": 3.9, "ist_aktiv": True}
print(f"Dictionary: {woerterbuch}, Typ: {type(woerterbuch)}")

# Set (Menge, einzigartige Elemente)
print("\n7. Set:")
menge = {1, 2, 3, 3, 4, 4, 5}  # Doppelte werden automatisch entfernt
print(f"Set: {menge}, Typ: {type(menge)}")

# Frozenset (unveränderbare Menge)
print("\n8. Frozenset:")
feste_menge = frozenset([1, 2, 3, 4, 5])
print(f"Frozenset: {feste_menge}, Typ: {type(feste_menge)}")

# None (Null-Wert)
print("\n9. None:")
nichts = None
print(f"None: {nichts}, Typ: {type(nichts)}")

# Bytes und Bytearray
print("\n10. Bytes und Bytearray:")
bytes_obj = b"Hello"
bytearray_obj = bytearray(b"Hello")
print(f"Bytes: {bytes_obj}, Typ: {type(bytes_obj)}")
print(f"Bytearray: {bytearray_obj}, Typ: {type(bytearray_obj)}")

# Range (Zahlenbereich)
print("\n11. Range:")
zahlenbereich = range(5)
print(f"Range: {zahlenbereich}, Typ: {type(zahlenbereich)}")
print(f"Range Inhalt: {list(zahlenbereich)}")

# Memoryview (Speicheransicht)
print("\n12. Memoryview:")
speicher = memoryview(bytes_obj)
print(f"Memoryview: {speicher}, Typ: {type(speicher)}")
