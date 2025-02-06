#----------------------Importowanie bibliotek-------------------------#
import os
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import confusion_matrix, accuracy_score  # Macierz błędu i miara dokładności
from sklearn.model_selection import cross_val_score  # Walidacja krzyżowa / k-fold
from sklearn.linear_model import LogisticRegression # Regresja logistyczna
from sklearn.neighbors import KNeighborsClassifier # Klasyfikacja K-sąsiadów
from sklearn.svm import SVC # Modele klasyfikacyjne SVM
from sklearn.tree import DecisionTreeClassifier # Drzewo decyzyjne
from sklearn.ensemble import RandomForestClassifier # Las losowy
from xgboost import XGBClassifier # Model XGBoost

#------------------Wczytanie danych testowych i treningowych-----------------------------#
# Pobranie katalogu, w którym znajduje się ten skrypt
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ścieżka do pliku CSV w tym samym folderze co skrypt
file_path = os.path.join(script_dir, "dataset.pkl")

# Sprawdzenie, czy plik istnieje
if not os.path.exists(file_path):
    print(f"Plik nie istnieje: {file_path}")
else:
    print(f"Odczyt danych z: {file_path}")

#---------------Wczytanie zbiorów----------------------------#
X_train, X_test, y_train, y_test = joblib.load("dataset.pkl")

#---------------Ocena różnych modeli klasyfikacyjnych--------#

# Lista modeli do oceny
models = {
    "Regresja logistyczna": LogisticRegression(random_state=10),
    "KNN": KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2),
    "SVM": SVC(kernel='linear', random_state=10),
    "Kernel SVM": SVC(kernel='rbf', random_state=10),
    "Drzewo decyzyjne": DecisionTreeClassifier(criterion='entropy', random_state=10),
    "Las losowy": RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=10),
    "XGBoost": XGBClassifier()
}

# Tworzenie pustej listy do przechowywania wyników
results = []

# Iteracja przez modele
for model_name, model in models.items():
    # Dopasowanie modelu
    model.fit(X_train, y_train)
    
    # Predykcja na zbiorze testowym
    y_pred = model.predict(X_test)
    accuracy = round(accuracy_score(y_test, y_pred) * 100, 2)
    
    # Walidacja krzyżowa
    cross_val_accuracies = cross_val_score(estimator=model, X=X_train, y=y_train, cv=10)
    cross_val_mean = round(cross_val_accuracies.mean() * 100, 2)
    cross_val_std = round(cross_val_accuracies.std() * 100, 2)
    
    # Dodanie wyników do listy
    results.append([model_name, accuracy, cross_val_mean, cross_val_std])

# Konwersja wyników do DataFrame
df_results = pd.DataFrame(results, columns=["Model", "Accuracy", "CrossVal Mean", "CrossVal Std"])

# Sortowanie według kryteriów
sorted_df = df_results.sort_values(by=["CrossVal Mean", "CrossVal Std", "Accuracy"], 
                                   ascending=[False, True, False],ignore_index=True)

# Połączenie pełnego zbioru danych
X = np.vstack((X_train, X_test))  # Łączenie wierszy dla cech
y = np.hstack((y_train, y_test))  # Łączenie wierszy dla etykiet

# Pobranie nazwy najlepszego modelu
final_model = sorted_df.iloc[0]["Model"]

# Pobranie instancji modelu z oryginalnego słownika
best_model_instance = models[final_model]

# Trenowanie modelu na pełnym zbiorze treningowym
best_model_instance.fit(X, y)

#------------------Zapisujemy model do pliku .pkl---------------------------------#
model_file_path = os.path.join(script_dir, "best_model.pkl")

joblib.dump(best_model_instance, model_file_path)

print(f"Zapisano plik: {model_file_path}")

if os.path.exists(model_file_path):
    print("Plik best_model.pkl został pomyślnie zapisany!")
else:
    print("Błąd: plik best_model.pkl nie został znaleziony po zapisie!")