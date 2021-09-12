import imdb

e = imdb.IMDb()
search = e.get_top250_movies()

for i in range(10):
    print(search[i])