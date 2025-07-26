import pandas as pd
import joblib

# Load a test dataset (scaled & processed) - replace path as needed
X_test = pd.read_csv('data/processed/diabetes_test_processed.csv')

# Separate features and target
y_test = X_test.pop('Outcome')

# Load your trained model
model = joblib.load('models/best_diabetes_model.pkl')

# Make predictions
y_pred = model.predict(X_test)

# Check if predictions were made (print first 10 predicted labels)
print("First 10 predictions:", y_pred[:10])

# Optionally, compute simple accuracy as a quick check
accuracy = (y_pred == y_test).mean()
print(f"Prediction accuracy on test set: {accuracy:.2f}")

# If no errors occur and predictions print, model is trained!
