import joblib
import os

# Load the model
model_path = os.path.join(os.path.dirname(__file__), "model.joblib")
model = joblib.load(model_path)

def predict(features):
    """
    Predict Iris species from features.
    
    Args:
        features: List or array of 4 features [sepal_length, sepal_width, petal_length, petal_width]
    
    Returns:
        Predicted class (0: setosa, 1: versicolor, 2: virginica)
    """
    # Ensure features is in the right format (2D array for sklearn)
    if len(features) == 4:
        features = [features]
    
    prediction = model.predict(features)[0]
    return prediction

