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

#--------------MODEL REGRESJI LOGISTYCZNEJ-------------------#
log_reg_classifier = LogisticRegression(random_state=10)

# Dopasowanie modelu regresji logistycznej do zbioru treningowego
log_reg_classifier.fit(X_train, y_train)

# Tworzenie macierzy pomyłek (confusion matrix)
y_pred_log_reg = log_reg_classifier.predict(X_test)
log_reg_cm = confusion_matrix(y_test, y_pred_log_reg)
print(round(accuracy_score(y_test, y_pred_log_reg) * 100, 2))

# Zastosowanie walidacji krzyżowej (k-fold cross validation)
log_reg_accuracies = cross_val_score(estimator=log_reg_classifier, X=X_train, y=y_train, cv=10)
print("Dokładność modelu regresji logistycznej: {:.2f} %".format(log_reg_accuracies.mean() * 100))
print("Odchylenie standardowe (regresja logistyczna): {:.2f} %".format(log_reg_accuracies.std() * 100))

#--------------MODEL K-NAJBLISZYCH SASIADÓW-------------------#
knn_classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)

# Dopasowanie modelu k-najbliższych sąsiadów do zbioru treningowego
knn_classifier.fit(X_train, y_train)

# Tworzenie macierzy pomyłek
y_pred_knn = knn_classifier.predict(X_test)
knn_cm = confusion_matrix(y_test, y_pred_knn)
print(round(accuracy_score(y_test, y_pred_knn) * 100, 2))

# Zastosowanie walidacji krzyżowej
knn_accuracies = cross_val_score(estimator=knn_classifier, X=X_train, y=y_train, cv=10)
print("Dokładność modelu k-najbliższych sąsiadów: {:.2f} %".format(knn_accuracies.mean() * 100))
print("Odchylenie standardowe (k-najbliżsi sąsiedzi): {:.2f} %".format(knn_accuracies.std() * 100))

#--------------MODEL SVM (support vector machine)-------------------#
svm_classifier = SVC(kernel='linear', random_state=10)

# Dopasowanie modelu SVM do zbioru treningowego
svm_classifier.fit(X_train, y_train)

# Tworzenie macierzy pomyłek
y_pred_svm = svm_classifier.predict(X_test)
svm_cm = confusion_matrix(y_test, y_pred_svm)
print(round(accuracy_score(y_test, y_pred_svm) * 100, 2))

# Zastosowanie walidacji krzyżowej
svm_accuracies = cross_val_score(estimator=svm_classifier, X=X_train, y=y_train, cv=10)
print("Dokładność modelu SVM: {:.2f} %".format(svm_accuracies.mean() * 100))
print("Odchylenie standardowe (SVM): {:.2f} %".format(svm_accuracies.std() * 100))

#--------------MODEL KERNEL SVM-------------------#
k_svm_classifier = SVC(kernel='rbf', random_state=10)

# Dopasowanie modelu kernel SVM do zbioru treningowego
k_svm_classifier.fit(X_train, y_train)

# Tworzenie macierzy pomyłek
y_pred_k_svm = k_svm_classifier.predict(X_test)
k_svm_cm = confusion_matrix(y_test, y_pred_k_svm)
print(round(accuracy_score(y_test, y_pred_k_svm) * 100, 2))

# Zastosowanie walidacji krzyżowej
k_svm_accuracies = cross_val_score(estimator=k_svm_classifier, X=X_train, y=y_train, cv=10)
print("Dokładność modelu kernel SVM: {:.2f} %".format(k_svm_accuracies.mean() * 100))
print("Odchylenie standardowe (kernel SVM): {:.2f} %".format(k_svm_accuracies.std() * 100))

#--------------MODEL DRZEWA KLASYFIKACYJNEGO-------------------#
dt_classifier = DecisionTreeClassifier(criterion='entropy', random_state=10)

# Dopasowanie modelu drzewa decyzyjnego do zbioru treningowego
dt_classifier.fit(X_train, y_train)

# Tworzenie macierzy pomyłek
y_pred_dt = dt_classifier.predict(X_test)
dt_cm = confusion_matrix(y_test, y_pred_dt)
print(round(accuracy_score(y_test, y_pred_dt) * 100, 2))

# Zastosowanie walidacji krzyżowej
dt_accuracies = cross_val_score(estimator=dt_classifier, X=X_train, y=y_train, cv=10)
print("Dokładność modelu drzewa decyzyjnego: {:.2f} %".format(dt_accuracies.mean() * 100))
print("Odchylenie standardowe (drzewo decyzyjne): {:.2f} %".format(dt_accuracies.std() * 100))

#--------------MODEL LASU LOSOWEGO-------------------#
rf_classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=10)

# Dopasowanie modelu lasu losowego do zbioru treningowego
rf_classifier.fit(X_train, y_train)

# Tworzenie macierzy pomyłek
y_pred_rf = rf_classifier.predict(X_test)
rf_cm = confusion_matrix(y_test, y_pred_rf)
print(round(accuracy_score(y_test, y_pred_rf) * 100, 2))

# Zastosowanie walidacji krzyżowej
rf_accuracies = cross_val_score(estimator=rf_classifier, X=X_train, y=y_train, cv=10)
print("Dokładność modelu lasu losowego: {:.2f} %".format(rf_accuracies.mean() * 100))
print("Odchylenie standardowe (las losowy): {:.2f} %".format(rf_accuracies.std() * 100))

#--------------MODEL XGBOOST-------------------#
xgb_classifier = XGBClassifier()

# Dopasowanie modelu XGBoost do zbioru treningowego
xgb_classifier.fit(X_train, y_train)

# Tworzenie macierzy pomyłek
y_pred_xgb = xgb_classifier.predict(X_test)
xgb_cm = confusion_matrix(y_test, y_pred_xgb)
print(round(accuracy_score(y_test, y_pred_xgb) * 100, 2))

# Zastosowanie walidacji krzyżowej
xgb_accuracies = cross_val_score(estimator=xgb_classifier, X=X_train, y=y_train, cv=10)
print("Dokładność modelu XGBoost: {:.2f} %".format(xgb_accuracies.mean() * 100))
print("Odchylenie standardowe (XGBoost): {:.2f} %".format(xgb_accuracies.std() * 100))
