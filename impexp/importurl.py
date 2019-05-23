import json, requests,sqlite3
from datetime import datetime, timedelta

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

insert_movies = 'INSERT INTO movies(title, description, genre) VALUES (?,?,?)'
insert_schedules = 'INSERT INTO schedules(date, movie_id, total_amount, price) VALUES (?,?,?,?)'

url = "http://www.omdbapi.com/?s=inception&apikey=3800e6b5"
headers = {'user-agent':'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'}
response = requests.get(url, headers)
python_dictionary_values = json.loads(response.text)

class ImportUrl:

    def __init__(self, days = 7):
        self.days = days

    def import_all_movies(self):
        select_movies()
        if (len(movie_ids) > 0):
            import_movies()
            movies = get_movies()
            create_schedule(movies)

    def get_all_movies(self):
        movies = get_movies()


def select_movies():
    select_movie = True
    while select_movie:
        if input('Select movie: (y/n) ').lower() == 'y':
            movie_id = input('Write movie Id from IMDB : ')
            movie_ids.append(movie_id)
        else:
            select_movie = False
    
def create_schedule(movies):
        data = []
        today = datetime.today()
        ('Creating movie schedule ...')
        for movie in movies:            
            for i in range(14):
                modified_date = today + timedelta(i)    
                modified_date = modified_date.replace(hour=9, minute=0, second=0, microsecond=0)
                for j in range(5): 
                    modified_date_time = modified_date + timedelta(hours=j*3)
                    schedule_data = (modified_date_time,movie[0], 20, 7.99)
                    data.append(schedule_data)
        #print(data)        
        cursor.executemany(insert_schedules, data)
    
def get_movies():
    select = '''SELECT id,title from movies'''
    cursor.execute(select)
    return cursor.fetchall()  

def import_movies():
        data=[]
        print('Creating movie db ...')
        for i, ids in enumerate(movie_ids):
            url = "http://www.omdbapi.com/?i=" + ids+ "&apikey=3800e6b5"
            response = requests.get(url, headers)
            movie_dictionary = json.loads(response.text)
            movie_data = (movie_dictionary["Title"], movie_dictionary["Plot"],  movie_dictionary["Genre"])              
            data.append(movie_data)
        cursor.executemany(insert_movies, data)
    
import_url = ImportUrl()
import_url.import_all_movies()
