## Laden Sie das GitHub-Repository herunter
```bash
git clone https://github.com/thorstenkloehn/portal.git portal # Repository klonen
cd portal # In das Verzeichnis wechseln
python3 -m venv .venv # Erstellen Sie eine virtuelle Umgebung
source .venv/bin/activate # Aktivieren Sie die virtuelle Umgebung
```
## Installieren Sie die Abhängigkeiten
```bash
pip install -r requirements.in # Abhängigkeiten installieren
```
## Fügen Sie die folgenden Umgebungsvariablen in die .env-Datei ein
Mit dem Befehl `nano .env` können Sie die .env-Datei öffnen und die folgenden Umgebungsvariablen einfügen, mit Ihren eigenen Werten.
```bash
cp example.env .env
```
## OSM Datenbank in Modell Umwandeln
```
python manage.py startapp osm
python manage.py inspectdb > osm/models.py
python manage.py inspectdb Tabellenamen tabellename2 > osm/models.py
```

## Jetzt starten wir das Programm


```bash
python manage.py migrate # Datenbankmigrationen anwenden
python manage.py runserver # Entwicklungsserver starten 
python manage.py createsuperuser # Erstellen Sie einen Superuser
``` 