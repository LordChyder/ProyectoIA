import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv('data/dataset_riasec_etiquetas.csv')

X = df.drop(['archivo', 'etiqueta_RIASEC'], axis=1)
y = df['etiqueta_RIASEC']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Precisión:", model.score(X_test, y_test))
joblib.dump(model, 'model/modelo_riasec.pkl')