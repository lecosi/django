from django_servi.http import HttpResponse
from django_test.models import User
import json


def list_users(request):
    payload = {
        'existed': False,
    }
    if request.method == 'GET':
        users = User.objects.all()
        if users:
            results = [ob.as_json() for ob in users]
            payload = json.dumps(results)

    return HttpResponse(payload, content_type="application/json")


def create_user(request):
    payload = {
        'existed': False,
    }
    if request.method == 'POST':
        print()

    return HttpResponse(payload, content_type="application/json")
