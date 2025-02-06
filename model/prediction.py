import joblib
import numpy as np
import os
import sys


def load_model_and_scaler():
    """ Wczytuje zapisany model oraz skaler """
    # Pobranie katalogu, w którym znajduje się ten skrypt
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Ścieżki do plików pkl w tym samym folderze co skrypt
    model_path = os.path.join(script_dir, "best_model.pkl")
    scaler_path = os.path.join(script_dir, "scalar.pkl")

    # Sprawdzenie, czy pliki istnieją
    if not os.path.exists(model_path):
        print(f"Plik modelu nie istnieje: {model_path}")
        return None, None
    else:
        print(f"Odczyt modelu z: {model_path}")

    if not os.path.exists(scaler_path):
        print(f"Plik skalera nie istnieje: {scaler_path}")
        return None, None
    else:
        print(f"Odczyt skalera z: {scaler_path}")

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
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
