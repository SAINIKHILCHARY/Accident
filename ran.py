import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# Path to your data folder
data_folder = "data"

# Loop through all CSV files in data folder
for file in os.listdir(data_folder):
    if file.endswith(".csv"):
        print(f"\n🔹 Training model for dataset: {file}")
        
        # Load dataset
        df = pd.read_csv(os.path.join(data_folder, file))
        
        # Ensure required columns exist
        if "Deaths" not in df.columns or "Latitude" not in df.columns or "Longitude" not in df.columns:
            print(f"Skipping {file} (missing required columns)")
            continue

        # Convert Deaths into categories (Low/Medium/High)
        def categorize_deaths(x):
            if x <= 10:
                return "Low"
            elif x <= 30:
                return "Medium"
            else:
                return "High"

        df["Severity"] = df["Deaths"].apply(categorize_deaths)

        # Features and target
        X = df[["Latitude", "Longitude"]]
        y = df["Severity"]

        # Encode target labels
        y = LabelEncoder().fit_transform(y)

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Train Random Forest Classifier
        rf = RandomForestClassifier(n_estimators=100, random_state=42)
        rf.fit(X_train, y_train)

        # Predictions
        y_pred = rf.predict(X_test)

        # Evaluation
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print(classification_report(y_test, y_pred))
