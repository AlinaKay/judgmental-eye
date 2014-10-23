import model
import csv

def load_users(session):

    with open('seed_data/u.user', 'rb') as f:
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            user = model.User(id = row[0], age = row[1], gender = row[2], zipcode = row[4])
            session.add(user)
    
    session.commit()

def load_movies(session):
    
    with open('seed_data/u.item', 'rb') as f:
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            movie = model.Movie(id = row[0], title = row[1].decode("latin-1"), release_date = row[2], imdb_url = row[4])
            session.add(movie)
    
    session.commit()


def load_ratings(session):

    with open('seed_data/u.data', 'rb') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            rating = model.Rating(user_id = row[0], movie_id = row[1], rating = row[2], timestamp = row[3])
            session.add(rating)
    
    session.commit()

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_users(session)
    load_movies(session)
    load_ratings(session)

if __name__ == "__main__":
    s= model.connect()
    main(s)