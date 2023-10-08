import cv2
import easyocr
import os
import re
import numpy as np
from Levenshtein import distance as levenshtein_distance

# Erstelle einen EasyOCR-Reader
reader = easyocr.Reader(['de', 'en', 'fr'])


# Pfade zu den Bildern im 'license-plate'-Ordner
image_folder = 'license_plates'
image_paths = [os.path.join(image_folder, filename) for filename in os.listdir(image_folder)]

# Variablen zum Zählen der Ergebnisse
erkannt = 0
fast_erkannt = 0 
nicht_erkannt = 0

# Iteriere über jedes Bild und erkennne das Kennzeichen
for image_path in image_paths:
    try:
        # Lade das Bild als Numpy-Array
        img = cv2.imread(image_path)

        # Erhöhe den Kontrast
        img = cv2.convertScaleAbs(img, alpha=1.5, beta=0)

        # Führe eine Rauschunterdrückung durch
        img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)

        result = reader.readtext(img)

        # Extrahiere den Text jeder Erkennung und kombiniere sie zu einem String
        plate_text = ''.join([res[1] for res in result])

        # Entferne alle nicht-alphanumerischen Zeichen
        plate_text = re.sub(r'[^a-zA-Z0-9]', '', plate_text).upper()

        # Vergleiche das Ergebnis mit dem Dateinamen ohne die Endung
        filename = (os.path.splitext(os.path.basename(image_path))[0]).upper()
        if plate_text == filename:
            erkannt += 1
        else:
            ld = levenshtein_distance(filename,plate_text)
            print(f"{image_path}: Erwartetes Ergebnis: {filename}, Erkanntes Ergebnis: {plate_text}. ld ist {ld}")
            if(ld == 1):
                fast_erkannt += 1
            else:
                nicht_erkannt += 1

    except Exception as e:
        print(f"{e}")

erkennungsquote = ( (erkannt + fast_erkannt) / len(image_paths)) * 100
# Gib die Werte der Variablen aus
print(f"Erkannt: {erkannt}")
print(f"Toleranz: {fast_erkannt}")
print(f"Nicht erkannt: {nicht_erkannt}")
print(f"Erkennungsquote: {erkennungsquote}%")
