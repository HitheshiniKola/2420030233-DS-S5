import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression


print("----- Linear Regression -----")

X_linear = np.array([[1000], [1200], [1500], [1800], [2000]])

y_linear = np.array([50, 55, 65, 80, 90])

linear_model = LinearRegression()

linear_model.fit(X_linear, y_linear)

new_house_size = np.array([[1700]])
predicted_price = linear_model.predict(new_house_size)
print("Training House Sizes:")
print(X_linear.flatten())
print("\nTraining House Prices:")
print(y_linear)
print("\nPredicted Price for 1700 sq.ft house:")
print(predicted_price[0])
print("\n\n----- Logistic Regression -----")
X_logistic = np.array([[40], [50], [60], [70], [80], [90]])

y_logistic = np.array([0, 0, 0, 1, 1, 1])

logistic_model = LogisticRegression()

logistic_model.fit(X_logistic, y_logistic)

test_price = np.array([[75]])
purchase_prediction = logistic_model.predict(test_price)

purchase_probability = logistic_model.predict_proba(test_price)
print("Training House Prices:")
print(X_logistic.flatten())
print("\nPurchase Labels:")
print(y_logistic)
print("\nTest House Price:", test_price[0][0])
print("\nPurchase Prediction:")
print(purchase_prediction[0])
print("\nPrediction Probabilities:")
print(purchase_probability)
