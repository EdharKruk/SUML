from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

predic = model.predict(X_test)
acc = accuracy_score(y_test, predic)
print("Accuracy:", acc)

if not os.path.exists("app"):
    os.mkdir("app")
joblib.dump(model, "app/model.joblib")
