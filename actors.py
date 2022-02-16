# by Kami Bigdely
# Extract class
first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],
          ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']


class Actor:
    def __init__(self, first_name, last_name, birth_year, movie, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movie = movie
        self.email = email

    def print_info(self):
        print(self.first_name, self.last_name)
        print('Movies Played: ', end='')
        for movie in self.movie:
            print(movie, end=' ')
        print()

    def send_hiring_email(self):
        print("email sent to: ", self.email)


actors = []
for i in range(len(first_names)):
    actors.append(
        Actor(first_names[i], last_names[i], birth_year[i], movies[i], emails[i]))

for actor in actors:
    if actor.birth_year > 1985:
        actor.print_info()
        actor.send_hiring_email()
