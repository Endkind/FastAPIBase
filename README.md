# EnderFastAPIBase

**EnderFastAPIBase** ist eine einfache und erweiterbare Basis für FastAPI-Projekte. Sie bietet eine Struktur, in die du deine eigenen Module hinzufügen kannst. Diese Module werden automatisch beim Starten der Anwendung geladen. Zusätzlich unterstützt das Projekt die einfache Integration und Ausführung von Unit-Tests.

## Installation

1. **Repository klonen**:

    ```bash
   git clone https://github.com/Endkind/FastAPIBase
    cd FastAPIBase
   ```

2. **Abhängigkeiten installieren:** Stelle sicher, dass du Python 3.8+ installiert hast. Installiere die notwendigen Abhängigkeiten mit:

    ```bash
   pip install -r requirements.txt
   ```

## Nutzung

### Anwendung starten

Um die FastAPI-Anwendung zu starten, führe die main.py aus:

```bash
python main.py
```

Dies wird die Anwendung auf dem standardmäßigen FastAPI-Server starten, der unter [http://127.0.0.1:8000](http://127.0.0.1:8000) erreichbar ist.

### Module hinzufügen

Um ein neues Modul hinzuzufügen, folge diesen Schritten:

1. Erstelle im Ordner `modules` ein neues Verzeichnis für dein Modul, z.B. `my_module`.
2. In diesem Verzeichnis benötigst du mindestens eine `routes.py`-Datei. Der Inhalt der `routes.py` sollte wie folgt aussehen:

    ```python
    from fastapi import APIRouter

    router = APIRouter()
    ```

3. Füge weitere Dateien und Logik in deinem Modul hinzu, wenn nötig.
Diese `routes.py` wird beim Starten der `main.py` automatisch geladen und integriert.

### Beispielmodule

Im Projekt befindet sich ein Beispielmodul namens `example`. Dieses Modul enthält Beispiele für:

- **Routen:** Wie man Routen definiert und registriert.
- **Schemas:** Wie man Daten-Schemas für die Validierung erstellt.
- **DB-Models:** Wie man Datenbankmodelle erstellt.
- **Tests:** Beispielhafte Tests, die im `tests`-Ordner organisiert sind.

Du kannst das `example`-Modul als Orientierungshilfe verwenden, um eine Vorstellung davon zu bekommen, wie du deine eigenen Module strukturieren und implementieren kannst.

### Tests ausführen

Um alle Tests auszuführen, starte einfach die `test.py`:

```bash
python test.py
```

Das Skript sucht nach Testdateien im `tests`-Ordner im Root-Verzeichnis sowie in den `tests`-Unterordnern deiner Module. Testdateien müssen dem Muster `test*.py` entsprechen, um erkannt und ausgeführt zu werden.

#### Beispiele für Tests

Wenn du Tests für dein Modul `my_module` hinzufügen möchtest:

1. Erstelle im Modul-Verzeichnis `my_module` einen Unterordner namens `tests`.
2. Füge Testdateien hinzu, die dem Muster `test*.py` entsprechen, z.B. `modules/my_module/tests/test_example.py`.

Diese Tests werden dann automatisch ausgeführt, wenn du `test.py` startest.

### Code Coverage

1. Führe die Tests mit Coverage aus:

   ```bash
   coverage run test.py
   ```

2. Konvertiere die `.coverage`-Datei in verschiedene Formate:

-
  - `XML-Bericht:`

      ```bash
      coverage xml
      ```

      Erzeugt eine `coverage.xml`-Datei, die z.B. für CI/CD-Tools nützlich ist.
  - `HTML-Bericht:`

      ```bash
      coverage html
      ```

      Erzeugt einen HTML-Bericht im Ordner `htmlcov`, den du in deinem Browser öffnen kannst, um eine detaillierte Ansicht der Code Coverage zu erhalten.
  - `JSON-Bericht:`

      ```bash
      coverage json
      ```

      Erzeugt eine `coverage.json`-Datei, die in anderen Tools weiterverarbeitet werden kann.
  - `LCOV-Bericht:`

      ```bash
      coverage lcov
      ```

      Erzeugt eine `coverage.lcov`-Datei, die in LCOV-kompatiblen Tools verwendet werden kann.

## Lizenz

Dieses Projekt steht unter der [MIT-Lizenz](https://github.com/Endkind/FastAPIBase/blob/main/LICENSE).
