# Kennzeichen-Erkennung mit EasyOCR

Dieses Projekt verwendet EasyOCR, um Kennzeichen aus Bildern zu erkennen und die Ergebnisse mit den erwarteten Werten zu vergleichen.
Das Projekt wurde im Rahmen einer Projektarbeit in Kollaboration mit [ParsaMires](https://github.com/ParsaMires) erstellt.

## Voraussetzungen

Bevor Sie den Code ausführen können, stellen Sie sicher, dass Sie die folgenden Abhängigkeiten installiert haben:

- Python 3.x

Installieren Sie die benötigten Pakete mit den folgenden `pip`-Befehlen:


```bash
pip install opencv-python
pip install easyocr
pip install python-Levenshtein
```
## Verwendung
Stellen Sie sicher, dass Sie einen Ordner namens license_plates im gleichen Verzeichnis wie Ihr Skript haben. Dieser Ordner sollte die Bilder der Kennzeichen enthalten, die Sie erkennen möchten.
Führen Sie den Code mit dem folgenden Befehl aus:
```bash
python ocr_easyocr.py
```
