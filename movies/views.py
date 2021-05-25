import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from owners.models import Owner
from .models import Dog


class DogsListView(View):
    def get(self, request):
        result = []
        datas = Dog.objects.select_related()
        for data in datas:
            result.append(
                {
                    'name': data.name,
                    'age': data.age,
                    'owner_name': data.owner.name
                }
            )
        
        return JsonResponse({'result': result}, status=200)

class DogReg(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            owner = Owner.objects.get(id=data['owner_id'], name=data['owner_name'])

            Dog.objects.create(
                name=data['name'],
                age=data['age'],
                owner=owner
            )
            
            return JsonResponse({'message': 'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message': 'INVALID_KEY'}, status=400)