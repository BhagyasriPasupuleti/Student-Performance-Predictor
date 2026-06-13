import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("student_data.csv")

# Input features
X = data[["StudyHours", "Attendance"]]

# Output marks
y = data["Marks"]

# Create and train model
model = LinearRegression()
model.fit(X, y)

print("===== Student Performance Predictor =====")

hours = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance Percentage: "))

prediction = model.predict([[hours, attendance]])

print()
print("Predicted Marks:", round(prediction[0], 2))