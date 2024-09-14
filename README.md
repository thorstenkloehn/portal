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
## Erstelle die Datenbank
```bash
sudo -u postgres -i # Als Postgres-Benutzer anmelden
createuser thorsten  # Benutzer erstellen
createdb -E UTF8 -O thorsten Django # Datenbank erstellen
psql -d Django -c "CREATE EXTENSION postgis;" # PostGIS-Erweiterung installieren
psql -d Django -c "CREATE EXTENSION hstore;" # Hstore-Erweiterung installieren
psql -d Django -c "ALTER TABLE geometry_columns OWNER TO thorsten;" # Rechte setzen
psql -d Django -c "ALTER TABLE spatial_ref_sys OWNER TO thorsten;" # Rechte setzen
psql -d Django -c "\password thorsten" # Passwort setzen
exit # Postgres-Benutzer abmelden
```
## Fügen Sie die folgenden Umgebungsvariablen in die .env-Datei ein
Mit dem Befehl `nano .env` können Sie die .env-Datei öffnen und die folgenden Umgebungsvariablen einfügen, mit Ihren eigenen Werten.
```bash
DEBUG=True 
SECRET_KEY=arschloch 
DATABASE_NAME=Django 
DATABASE_USER=thorsten
DATABASE_PASSWORD=Test
DATABASE_HOST=localhost
DATABASE_PORT=5432
ALLOWED_HOSTS=localhost
```
## Jetzt starten wir das Programm
```bash
python manage.py migrate # Datenbankmigrationen anwenden
python manage.py runserver # Entwicklungsserver starten 
python manage.py createsuperuser # Erstellen Sie einen Superuser
``` 
## G