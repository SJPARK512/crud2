from django.shortcuts import render
import json

from django.http import JsonResponse
from django.views import View
from owner.models import Owners, Dogs


# Create your views here.


class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)
        owners = Owners.objects.create(name=data['name'], email=data['email'], age=data['age'])

        return JsonResponse({'MESSAGE': 'SUCCESS'}, status=201)

    def get(self, request):
        owners = Owners.objects.all()


        results = []
        for owner in owners:
            doglist = []
            dogs = owner.dogs_set.all()
            for dog in dogs:
                    dog_info={
                        "name" : dog.name,
                        "age" : dog.age
                    }
                    doglist.append(dog_info)

            results.append({

                "name": owner.name,
                "email": owner.email,
                "age": owner.age,
                "dog list" : doglist
            }
            )

        return JsonResponse({'results': results}, status=200)


class DogsView(View):

    def post(self, request):
        data = json.loads(request.body)
        owner = Owners.objects.get(name=data['owner'])
        Dogs.objects.create(
            name=data['name'],
            age=data['age'],
            owner = owner)

        return JsonResponse({'MESSAGE': 'SUCCESS'}, status=201)

    def get(self, request):
        dogs = Dogs.objects.all()
        results = []
        for dog in dogs:
            results.append({

                "name": dog.name,
                "age": dog.age,
                "owner": dog.owner.name
            }
            )

        return JsonResponse({'results': results}, status=200)
