 🚀 Predictor Project

A Machine Learning based prediction system built using Python for data analysis, model training, and accurate predictions. It features dual-directional forecasting to predict height from weight or weight from height.

🛠️ Tech Stack
  Python
  Pandas
  NumPy
  Scikit-learn

 ✨ Features
Dual-Directional Prediction:** Predicts height based on weight, or weight based on height.
Data Preprocessing:** Cleans and structures data for optimal model performance.
Model Training:** Utilizes trained regression models (`.pkl` files) for quick inference.
Accuracy Evaluation:** Includes validation checks to ensure reliable prediction output.

🔄 How It Works
The system prompts the user sequentially to capture the known variable before calculating the missing metric:

1. Select Input Type: Choose whether you want to enter a Height or a Weight.
2. Provide Value:Enter the numerical value for your chosen metric.
3. Generate Prediction:The corresponding model processes the input and instantly predicts the output value.
   

▶️ Run the Project

 1. Install Dependencies
Ensure you have all the required libraries installed:
```bash
pip install -r requirements.txt
