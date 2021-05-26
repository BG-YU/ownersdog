import json
from django.views import View
from django.http import JsonResponse
from .models import Owner

class OwnersListView(View):
    def get(self, request):        
        result = []
        owners = Owner.objects.all()

        for owner in owners:
            result.append(
                {
                    'id': owner.id,
                    'name': owner.name,
                    'email': owner.email,
                    'age': owner.age
                }
            )

        return JsonResponse({'result': result}, status=200)

class OwnersDogList(View):
    def get(self, request):
        result = []
        datas = Owner.objects.all()

        for data in datas:
            dog_list = []
            for dog in data.dog_set.filter(owner_id=data.id):
                dog_list.append(
                    {
                        'name': dog.name,
                        'age': dog.age
                    }
                )
            
            result.append(
                {
                    'name': data.name,
                    'age': data.age,
                    'dog_list': dog_list
                }
            )
            

        return JsonResponse({'result': result}, status=200)

class OwnersReg(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            Owner.objects.create(
                name=data['name'], 
                email=data['email'], 
                age=data['age']
            )

            return JsonResponse({'message': 'SUCCESS'}, status=201)
        except KeyError:
            return  JsonResponse({'message': 'INVALID_KEY'}, status=400)