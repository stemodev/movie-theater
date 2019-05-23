import json, requests, sqlite3
import sys

sys.path.append("C:\Source\Python\Advanced\movie-theater")

from db.SQLite import *

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d



connection = sqlite3.connect('pythonsqlite.db')
connection.row_factory = dict_factory
cursor = connection.cursor()

movie_ids=["tt6139732", "tt1489887", "tt7752126"]

insert = 'INSERT INTO movies(title, description, genre) VALUES (?,?,?)'

url = "http://www.omdbapi.com/?s=inception&apikey=3800e6b5"
headers = {'user-agent':'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'}
response = requests.get(url, headers)
python_dictionary_values = json.loads(response.text)

def select_movies():
    select_movie = True
    while select_movie:
        if input('Select movie: (y/n) ').lower() == 'y':
            movie_id = input('Write movie Id from IMDB : ')
            movie_ids.append(movie_id)
        else:
            select_movie = False
    
def import_db():
    print('Creating movie db ...')
    get_data_from_imdb()

def get_data_from_imdb():
    data=[]
    for i, ids in enumerate(movie_ids):
        url = "http://www.omdbapi.com/?i=" + ids+ "&apikey=3800e6b5"
        response = requests.get(url, headers)
        movie_dictionary = json.loads(response.text)
        movie_data = (movie_dictionary["Title"], movie_dictionary["Plot"],  movie_dictionary["Genre"])              
        data.append(movie_data)
    cursor.executemany(insert, data)

def create_movie_table():
    pass

def main():
    select_movies()
    if(len(movie_ids) > 0):
        import_db()

    select = '''SELECT id,title from movies'''
    cursor.execute(select)
    results = cursor.fetchall()
    print(results)
    
    select_all_movies(connection)
    

main()