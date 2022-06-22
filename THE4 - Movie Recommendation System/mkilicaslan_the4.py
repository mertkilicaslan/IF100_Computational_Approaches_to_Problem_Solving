# mkilicaslan_the4
f = open("all_ratings.txt")
movie_dict = {}
f.readline()

for line in f:
    movie_line = line.strip().split("\t")
    movie_name = movie_line[2]

    if movie_name not in movie_dict:
        movie_dict[movie_name] = [float(movie_line[1]), movie_line[3].lower(), 1]
    else:
        movie_dict[movie_name][0] += float(movie_line[1])
        movie_dict[movie_name][-1] += 1

genre = input("Enter a genre: ").lower()
genre_list = []
for k in movie_dict:
    if genre in movie_dict[k][1]:
        genre_list.append((k, movie_dict[k][0] / movie_dict[k][-1]))


def sort_according_to_rate(elem):
    return -elem[-1]


genre_list.sort(key=sort_according_to_rate)

for movie, rate in genre_list:
    watch = input(f"Would you like to watch {movie} with rating {rate:.4f}: ").lower()
    while watch != "yes" and watch != "no":
        watch = input("You entered an incorrect input, please enter yes or no: ").lower()

    if watch == "yes":
        print("Enjoy the movie!")
        break

    elif watch == "no":
        if movie == genre_list[-1][0]:
            print("No movies left in this genre!")

f.close()
