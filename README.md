# House Price Prediction
The house price prediction project is a machine learning model that uses Random Forest Regressor to predict the price of a house based on its features such as the number of bedrooms, bathrooms, square footage and location.

The Random Forest Regressor is an ensemble learning method that combines multiple decision trees to create a more robust and accurate model. This algorithm is well-suited for regression tasks and can handle complex datasets with many features.

To train this model, Kaggle dataset of bengaluru house prices was used, that included features such as the number of bedrooms, bathrooms, square footage, location, and other relevant factors, as well as their corresponding sale prices. A cleaned dataset was trained on Random Forest Regressor model, which learned to predict the sale price of a house based on these features.

To deploy this model, a web application was built using Flask, a Python web framework. This web application takes user input for 4 features of a house, the number of bedrooms, bathrooms, square footage, and location, and uses the trained model to predict the sale price of the house in Lakhs. The application then displays this prediction to the user.

