# Dokumentacja - Alzheimer Predictor

## 📌 Opis projektu

Alzheimer Predictor to aplikacja desktopowa napisana w Pythonie, służąca do szacowania ryzyka zachorowania na chorobę Alzheimera na podstawie informacji uzyskanych od użytkownika. Program zbiera dane demograficzne, dotyczące stylu życia oraz historii medycznej, a następnie dokonuje predykcji na podstawie wytrenowanego modelu uczenia maszynowego XGBoost (XGBoost okazał się najlepszy).

Ze względu na ograniczoną wielkość plików, które można umieszczać na GitHubie, nie ma tu pliku wykonywalnego (main.exe). Można go wygenerować samemu przy pomocy podanego niżej polecenia lub otworzyć plik przesłany innym kanałem.

## 📦 Wymagania systemowe

Python 3.10 lub nowszy

System operacyjny: Windows 10/11

Pamięć RAM: min. 4GB

Wolne miejsce na dysku: min. 500MB

## 🛠 Technologie

Python (tkinter, joblib, scikit-learn, numpy, xgboost)

GUI: Tkinter

Model ML: XGBoostClassifier

Pakowanie do .exe: PyInstaller

## 📥 Instalacja

1. Pobranie repozytorium

 git clone https://github.com/KarolKobus/ug-studies-se.git
 cd ug-studies-se

2. Utworzenie środowiska wirtualnego i instalacja zależności

 python -m venv venv
 source venv/Scripts/activate  # Windows
 pip install -r requirements.txt

3. Uruchomienie aplikacji w trybie deweloperskim

 python main.py

## 🎯 Funkcjonalności

Ekran powitalny – prezentacja celu programu

Kwestionariusz – zbieranie informacji o użytkowniku w 6 etapach

Predykcja – model ML szacuje ryzyko choroby Alzheimera

Raport końcowy – prezentacja wyników użytkownikowi

## 📑 Struktura projektu

ug-studies-se/
├── assets/                 # Logo, ikony
├── model/                  # Model ML i skalowanie danych
│   ├── best_model.pkl      # Wytrenowany model XGBoost
│   ├── scalar.pkl          # StandardScaler dla zmiennych wejściowych
│   ├── prediction.py       # Skrypt do predykcji
├── gui/                    # Interfejs użytkownika
│   ├── main_window.py      # Ekran główny
│   ├── question1.py        # Pytania demograficzne
│   ├── question2.py        # Czynniki stylu życia
│   ├── question3.py        # Historia medyczna
│   ├── question4.py        # Pomiary kliniczne
│   ├── question5.py        # Ocena funkcjonalna
│   ├── question6.py        # Objawy
│   ├── result.py           # Raport końcowy
├── dist/                   # Folder z wygenerowanym plikiem .exe
├── requirements.txt        # Lista zależności
├── main.py                 # Główny plik uruchamiający aplikację

## 🚀 Tworzenie pliku .exe

Aby wygenerować plik wykonywalny .exe, uruchom:

pyinstaller --onefile --windowed --icon="ug-studies-se\assets\icon.ico" \
--add-data "ug-studies-se\assets\logo.png;assets/" \
--add-data "ug-studies-se\model\best_model.pkl;model/" \
--add-data "ug-studies-se\model\scalar.pkl;model/" \
--hidden-import=joblib --hidden-import=scipy --hidden-import=scipy.special \
--hidden-import=xgboost --hidden-import=numpy --hidden-import=numpy._core \
--hidden-import=numpy._core.multiarray --hidden-import=numpy.linalg \
--hidden-import=tkinter --hidden-import=sklearn --hidden-import=importlib.resources \
--collect-submodules xgboost --collect-submodules numpy \
--exclude-module xgboost.testing --exclude-module hypothesis main.py

Po zakończeniu kompilacji, plik .exe będzie w folderze dist/.

## 👨‍💻 Autorzy

Michał Wroński

Karol Kobus

## 📝 Licencja - otwarta
