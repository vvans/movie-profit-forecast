import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Imports data from movies.csv
film_data = pd.read_csv("movies.csv", encoding="latin-1")

# Changes data into acceptable format
def reshape_data(column_name):
    new_data = {}
    data = list(set(film_data[column_name]))
    for i in range(len(data)):
        new_data[data[i]] = i
    data.clear()
    data = [new_data[country] for country in film_data[column_name]]
    return data

# Reassigns columns to reshaped data
film_data["director"] = reshape_data("director")
film_data["genre"] = reshape_data("genre")
film_data["rating"] = reshape_data("rating")
film_data["star"] = reshape_data("star")

# Defines labels and results 
profit_factors = film_data[["budget", "score", "year", "votes", "runtime", "genre", "rating", "director", "star"]]
gross_profits = film_data[["gross"]]

# Splitting data into training and testing
x_train, x_test, y_train, y_test = train_test_split(
    profit_factors, gross_profits, train_size=0.8, test_size=0.2, random_state=6)

# Using linear regression to predict test resulsts
mlr = LinearRegression()
mlr.fit(x_train, y_train)
y_predict = mlr.predict(x_test)

print(mlr.score(x_train, y_train))
print(mlr.score(x_test, y_test))