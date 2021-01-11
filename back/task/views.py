from django.http import JsonResponse

# Create your views here.
import requests
from rest_framework.views import APIView

class TaskListView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def get(self):
        response = requests.get('https://jsonplaceholder.typicode.com/todos')
        test = response.json()
        return JsonResponse(test, safe=False)
