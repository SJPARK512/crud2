from django.shortcuts import render
import json

from django.http import JsonResponse
from django.views import View
from movie.models import Movie, Actor


# Create your views here.


class ActorView(View):
    def post(self, request):
        data = json.loads(request.body)
        actor = Actor.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            date_of_birth=data['date_of_birth']
        )

        return JsonResponse({'MESSAGE': 'SUCCESS'}, status=201)

    def get(self, request):
        results = []
        actors = Actor.objects.all()
        for actor in actors:
            movielist = []
            movies = actor.movie.all()
            for movie in movies:
                movie_name = {
                    "title": movie.title
                }
                movielist.append(movie_name)
            results.append ({
                'first_name': actor.first_name,
                'last_name': actor.last_name,
                'movie_title': movielist
            })
        return JsonResponse({'results': results}, status=200)


class MovieView(View):
    def post(self, request):
        data = json.loads(request.body)
        movie = Movie.objects.create(
            title=data['title'],
            release_date=data['release_date'],
            running_time=data['running_time']
        )

        return JsonResponse({'MESSAGE': 'SUCCESS'}, status=201)

    def get(self, request):
        results = []
        movies = Movie.objects.all()
        for movie in movies:
            actors = movie.actor.all()
            actor_list = []

            for actor in actors:
                actor_name = {
                    'first_name': actor.first_name,
                    'last_name': actor.last_name
                }
                actor_list.append(actor_name)

            results.append({
                'title': movie.title,
                'running_time': movie.running_time,
                'actor_name': actor_list
            })
        return JsonResponse({'results': results}, status=200)
