# Predicting-gross-profit-of-movies
This is a linear regression algorithm that I wrote which predicts gross profit of movies using Python and the Sikit-Learn library.

# Data cleaning
The data originally was not in integer format, which meant that I had to reshape the data. However, the data also wasn't in a binary format which complicated the process. In other datasets for example, a column of "over_18" would have a binary result, either "true" or "false". In this dataset however, the column "director", like many other columns, had many unique results. I fixed this issue by assigning each result an integer value. For example, if the column "genre" returned ["adventure", "adventure", "action", "horror", "fantasy", "action", "horror"], I would assign each individual value with an alternative integer value. 
{"adventure": 0
"action": 1
"horror": 2
"fantasy": 3}
Therefore, the new list would return [0, 0, 1, 2, 3, 1, 3]. Now that the values are in integer format, the algorithm can now be trained properly.

# Removing data
Some of the columns were of little relevance and actually reduced the accuracy of the algorithm. For example, the column "writer" should be removed, as the writer of a film generally will not attract ticket sales. However, the column "star" should certainly be used as it will greatly improve the algorithm. The star of a movie, unlike the writer, can attract ticket sales and thereby improve the gross profit.

# Conclusion
The final accuracy of the algorithm is around 65%. 
