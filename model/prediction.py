<<<<<<< HEAD
import joblib
import numpy as np
import os
import sys


def load_model_and_scaler():
    """ Wczytuje model i skaler, uwzględniając środowisko PyInstaller """
    if getattr(sys, 'frozen', False):  # Jeśli uruchomiono jako .exe
        base_path = os.path.join(sys._MEIPASS, "model")
    else:  # Uruchomienie w PyCharm
        base_path = os.path.dirname(os.path.abspath(__file__))

    model_path = os.path.join(base_path, "best_model.pkl")
    scaler_path = os.path.join(base_path, "scalar.pkl")

    print(f"DEBUG - Ścieżka modelu: {model_path}")
    print(f"DEBUG - Ścieżka skalera: {scaler_path}")

    if not os.path.exists(model_path):
        print(f"Błąd: Plik modelu nie istnieje: {model_path}")
        return None, None
    if not os.path.exists(scaler_path):
        print(f"Błąd: Plik skalera nie istnieje: {scaler_path}")
        return None, None

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
=======
import numpy as np
import os
import sys
import pickle

LOG_FILE = "log.txt"


def log_message(message):
    """Zapisuje logi do pliku i wypisuje je na ekran"""
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(message + "\n")
    print(message)


def load_model_and_scaler():
    """ Wczytuje model XGBoost i scaler, szukając ich w katalogu 'ug-studies-se/model' """

    # Pobieramy poprawną ścieżkę do katalogu model/
    project_base_path = os.path.dirname(os.path.abspath(sys.executable)) if getattr(sys, 'frozen',
                                                                                    False) else os.path.abspath(
        os.path.join(os.path.dirname(__file__), ".."))
    model_dir = os.path.join(project_base_path, "model")

    # Pliki modelu i skalera
    model_path = os.path.join(model_dir, "best_model.pkl")
    scaler_path = os.path.join(model_dir, "scalar_new.pkl")

    log_message(f"🔍 DEBUG - Szukam modelu w: {model_path}")
    log_message(f"🔍 DEBUG - Szukam skalera w: {scaler_path}")

    if not os.path.exists(model_path):
        log_message(f"❌ BŁĄD: Plik modelu NIE ISTNIEJE: {model_path}")
        return None, None
    if not os.path.exists(scaler_path):
        log_message(f"❌ BŁĄD: Plik skalera NIE ISTNIEJE: {scaler_path}")
        return None, None

    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        log_message("✅ Model XGBoost załadowany poprawnie.")
    except Exception as e:
        log_message(f"❌ BŁĄD przy wczytywaniu modelu: {e}")
        model = None

    try:
        with open(scaler_path, 'rb') as f:
            scaler = pickle.load(f)
        log_message("✅ Skaler załadowany poprawnie.")
    except Exception as e:
        log_message(f"❌ BŁĄD przy wczytywaniu skalera: {e}")
        scaler = None

>>>>>>> gui
    return model, scaler


def get_user_input():
    """ Pobiera dane od użytkownika, zapewniając odpowiednie typy danych """
    int_features = ["EducationLevel", "Hypertension"]

    float_features = [
        "MemoryComplaints", "BehavioralProblems", "SleepQuality", "CholesterolLDL",
        "CholesterolHDL", "MMSE", "FunctionalAssessment", "ADL"
    ]

    user_data = []

    print("Podaj wartości dla poniższych zmiennych:")
    for feature in int_features:
        while True:
            try:
                value = int(input(f"{feature} (liczba całkowita): "))
                user_data.append(value)
                break
            except ValueError:
                print("Błąd! Podaj liczbę całkowitą.")

    for feature in float_features:
        while True:
            try:
                value = float(input(f"{feature} (liczba zmiennoprzecinkowa): "))
                user_data.append(value)
                break
            except ValueError:
                print("Błąd! Podaj liczbę.")

    return np.array([user_data])  # Konwersja do tablicy NumPy

<<<<<<< HEAD
def predict_outcome(model, scaler, user_data):
    """ Przekształca dane użytkownika i dokonuje predykcji """
    user_data_scaled = scaler.transform(user_data)  # Normalizacja danych
    prediction = model.predict(user_data_scaled)
    return prediction

if __name__ == "__main__":
    # Wczytanie modelu i skalera
    model, scaler = load_model_and_scaler()

    if model is None or scaler is None:
        print("Błąd: Model lub skaler nie został poprawnie wczytany.")
    else:
        # Pobranie danych od użytkownika
        user_data = get_user_input()

        # Predykcja wyniku
        result = predict_outcome(model, scaler, user_data)

        print("\nPrzewidywana wartość y (klasa):", result[0])
=======

def predict_outcome(model, scaler, user_data):
    """ Normalizuje dane użytkownika i dokonuje predykcji modelem XGBoost """
    try:
        if scaler is not None:
            log_message("✅ Normalizuję dane przed predykcją...")
            user_data = scaler.transform(user_data)  # Skalowanie zmiennych
        prediction = model.predict(user_data)
        log_message(f"✅ Predykcja zakończona sukcesem: {prediction}")
        return prediction
    except Exception as e:
        log_message(f"❌ BŁĄD: Predykcja nie powiodła się: {e}")
        return None
>>>>>>> gui
