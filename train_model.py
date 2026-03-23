import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load data
df = pd.read_csv("data/dataset.csv")  
# -----------------------------
# Model 1: Height → Weight
# -----------------------------
X1 = df[['Height', 'Age', 'Gender']]
y1 = df['Weight']

model_hw = LinearRegression()
model_hw.fit(X1, y1)

# Save model
pickle.dump(model_hw, open("model_height_to_weight.pkl", "wb"))

# -----------------------------
# Model 2: Weight → Height
# -----------------------------
X2 = df[['Weight', 'Age', 'Gender']]
y2 = df['Height']

model_wh = LinearRegression()
model_wh.fit(X2, y2)

# Save model
pickle.dump(model_wh, open("model_weight_to_height.pkl", "wb"))

print("Models trained and saved successfully ✅")