from django.core.management.base import BaseCommand
from django.core import management,serializers

from datetime import date, time, datetime,timedelta

import csv,json

class Command(BaseCommand):
    help = 'Load data'
    raw_path = 'Movies/RawData/movie_metadata.csv'
    director_dict = {}
    country_dict = {}
    lan_dict = {}
    color_dict = {}
    content_dict = {}
    actor_dict = {}
    movie_dict = {}
    plot_dict = {}
    def reader(self,path):
        f = open(path,'r',encoding="utf8")
        reader = csv.reader(f)
        i = next(reader)
        reader = csv.DictReader(f, fieldnames = i)
        return reader

    def export_file(self,path,dataload):
        f = open( path, 'w')
        out = json.dumps(dataload, indent=4)
        f.write(out)

    def color_list(self):
        reader = self.reader(self.raw_path)
        col_dict = {}
        export_ar = []
        for row in reader:
            col_dict[row['color']] = 1;

        for i in col_dict.keys():
            export_dict = {}
            export_dict['model'] = 'Movies.Color'
            export_dict['pk'] = len(export_ar) + 1
            export_dict['fields'] = {}
            export_dict['fields']['color_name'] = i
            self.color_dict[i] = len(export_ar) + 1
            export_ar.append(export_dict)

        self.export_file('Movies/Fixtures/color.json',export_ar)

    def contentrate_list(self):
        reader = self.reader(self.raw_path)
        cr_dict = {}
        export_ar = []
        for row in reader:
            cr_dict[row['content_rating']] = 1;

        for i in cr_dict.keys():
            export_dict = {}
            export_dict['model'] = 'Movies.ContentRate'
            export_dict['pk'] = len(export_ar) + 1
            export_dict['fields'] = {}
            export_dict['fields']['contentrate_name'] = i
            self.content_dict[i] = len(export_ar) + 1
            export_ar.append(export_dict)

        self.export_file('Movies/Fixtures/contentrate.json',export_ar)

    def plot_list(self):
        reader = self.reader(self.raw_path)
        plot_str = {}
        export_ar = []
        for row in reader:
            for item in row['plot_keywords'].split('|'):
                plot_str[item] = 1

        for i in plot_str.keys():
            export_dict = {}
            export_dict['model'] = 'Movies.Plot'
            export_dict['pk'] = len(export_ar) + 1
            export_dict['fields'] = {}
            export_dict['fields']['plot_name'] = i
            self.plot_dict[i] = len(export_ar) + 1
            export_ar.append(export_dict)

        self.export_file('Movies/Fixtures/plot.json',export_ar)

    def plotmovie_list(self):
        reader = self.reader(self.raw_path)
        export_ar = []
        for row in reader:
            for item in row['plot_keywords'].split('|'):
                export_dict = {}
                export_dict['model'] = 'Movies.PlotMovie'
                export_dict['pk'] = len(export_ar) + 1
                export_dict['fields'] = {}
                export_dict['fields']['id_plot'] = self.plot_dict[item]
                export_dict['fields']['id_movie'] = self.movie_dict[row['movie_title']]
                export_ar.append(export_dict)
        self.export_file('Movies/Fixtures/plotmovie.json',export_ar)
    def country_list(self):
        reader = self.reader(self.raw_path)
        con_dict = {}
        export_ar = []
        for row in reader:
            con_dict[row['country']] = 1;

        for i in con_dict.keys():
            export_dict = {}
            export_dict['model'] = 'Movies.Country'
            export_dict['pk'] = len(export_ar) + 1
            export_dict['fields'] = {}
            export_dict['fields']['country_name'] = i
            self.country_dict[i] = len(export_ar) + 1
            export_ar.append(export_dict)

        self.export_file('Movies/Fixtures/country.json',export_ar)

    def language_list(self):
        reader = self.reader(self.raw_path)
        lan_dict = {}
        export_ar = []
        for row in reader:
            lan_dict[row['language']] = 1;

        for i in lan_dict.keys():
            export_dict = {}
            export_dict['model'] = 'Movies.Language'
            export_dict['pk'] = len(export_ar) + 1
            export_dict['fields'] = {}
            export_dict['fields']['language_name'] = i
            self.lan_dict[i] = len(export_ar) + 1
            export_ar.append(export_dict)

        self.export_file('Movies/Fixtures/language.json',export_ar)

    def director_list(self):
        reader = self.reader(self.raw_path)
        dir_dict = {}

        export_ar = []
        for row in reader:
            dir_dict[row['director_name']] = 1;

        for i in dir_dict.keys():
            export_dict = {}
            export_dict['model'] = 'Movies.Director'
            export_dict['pk'] = len(export_ar) + 1
            export_dict['fields'] = {}
            export_dict['fields']['director_name'] = i
            self.director_dict[i] = len(export_ar) + 1
            export_ar.append(export_dict)

        self.export_file('Movies/Fixtures/director.json',export_ar)
    def actor_list(self):
        reader = self.reader(self.raw_path)
        act_dict = {}
        export_ar = []

        for row in reader:
            act_dict[row['actor_1_name']] = 1;
            act_dict[row['actor_2_name']] = 1;
            act_dict[row['actor_3_name']] = 1;
        for i in act_dict:
            export_dict = {}
            export_dict['model'] = 'Movies.Actor'
            export_dict['pk'] = len(export_ar) + 1
            export_dict['fields'] = {}
            export_dict['fields']['actor_name'] = i
            self.actor_dict[i] = len(export_ar) + 1
            export_ar.append(export_dict)

        self.export_file('Movies/Fixtures/actor.json',export_ar)
    def movie_actor(self):
        reader = self.reader(self.raw_path)
        movact_dict = {}
        export_ar = []

        for row in reader:
            movact_dict[row['actor_1_name']] = []
            movact_dict[row['actor_2_name']] = []
            movact_dict[row['actor_3_name']] = []

        reader = self.reader(self.raw_path)

        for row in reader:
            movact_dict[row['actor_1_name']].append(self.movie_dict[row['movie_title']])
            movact_dict[row['actor_2_name']].append(self.movie_dict[row['movie_title']])
            movact_dict[row['actor_3_name']].append(self.movie_dict[row['movie_title']])

        for actor in movact_dict.keys():
            for movie_id in movact_dict[actor]:
                export_dict = {}
                export_dict['model'] = 'Movies.MovieActor'
                export_dict['pk'] = len(export_ar) + 1
                export_dict['fields'] = {}
                export_dict['fields']['id_actor'] = self.actor_dict[actor]
                export_dict['fields']['id_movie'] = movie_id

                export_ar.append(export_dict)

        self.export_file('Movies/Fixtures/actormovie.json',export_ar)

    def movie_list(self):
        reader = self.reader(self.raw_path)
        mov_dict = {}
        export_ar = []

        for row in reader:
            export_dict = {}
            export_dict['model'] = 'Movies.Movie'
            export_dict['pk'] = len(export_ar) + 1
            export_dict['fields'] = {}
            export_dict['fields']['movie_title'] = row['movie_title']
            export_dict['fields']['movie_director_name'] = self.director_dict[row['director_name']]
            export_dict['fields']['movie_country'] = self.country_dict[row['country']]
            export_dict['fields']['movie_language'] = self.lan_dict[row['language']]
            export_dict['fields']['movie_budget'] = int(row['budget'].strip() or 0)
            export_dict['fields']['movie_year'] = int(row['title_year'].strip() or 0)
            export_dict['fields']['movie_imdb_score'] = float(row['imdb_score'].strip() or 0.0)
            export_dict['fields']['movie_imdb_link'] = row['movie_imdb_link']
            export_dict['fields']['movie_aspect_ratio'] = float(row['aspect_ratio'].strip() or 0.0)
            export_dict['fields']['movie_facebook_likes'] = int(row['movie_facebook_likes'].strip() or 0)
            export_dict['fields']['movie_num_voted_users'] = int(row['num_voted_users'].strip() or 0)
            export_dict['fields']['movie_gross'] = int(row['gross'].strip() or 0)
            export_dict['fields']['movie_duration'] = int(row['duration'].strip() or 0)
            export_dict['fields']['movie_director_facebook_likes'] = int(row['director_facebook_likes'].strip() or 0)
            export_dict['fields']['movie_color'] = self.color_dict[row['color']]
            export_dict['fields']['movie_cast_total_facebook_likes'] =  int(row['cast_total_facebook_likes'].strip() or 0)
            export_dict['fields']['movie_content_rate'] = self.content_dict[row['content_rating']]
            export_dict['fields']['movie_facenumber_in_poster'] = int(row['facenumber_in_poster'].strip() or 0)
            export_dict['fields']['movie_num_critc_for_review'] = int(row['num_critic_for_reviews'].strip() or 0)
            export_dict['fields']['movie_num_user_for_reviews'] = int(row['num_user_for_reviews'].strip() or 0)
            export_dict['fields']['movie_genres'] = []
            for item in row['plot_keywords'].split('|'):
                export_dict['fields']['movie_genres'].append(self.plot_dict[item])
            self.movie_dict[row['movie_title']] = len(export_ar) + 1
            export_ar.append(export_dict)


        self.export_file('Movies/Fixtures/movie.json',export_ar)



    def handle(self, *args, **options):
        print ("Precargando modelos:")
        ini_date = datetime.now()
        print("Cargando ContentRate")
        self.contentrate_list()
        print("Cargando Directors")
        self.director_list()
        print("Cargando Plots")
        self.plot_list()
        print("Cargando Color")
        self.color_list()
        print("Cargando Language")
        self.language_list()
        print("Cargando Countries")
        self.country_list()
        print("Cargando Movies")
        self.movie_list()
        print("Cargando Actors")
        self.actor_list()
        print("Cargando Movie - Actors")
        self.movie_actor()
        management.call_command('loaddata','contentrate','director','color','actor','country','language','movie','actormovie','plot')
        duration = datetime.now() - ini_date
        print ("Ejecucion en ", duration.total_seconds(), "segundos")
