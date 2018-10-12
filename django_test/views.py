from django.http import HttpResponse
from django_test.models import User
from django_test.forms import CreateUserForm
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
        'not created': True,
    }
    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            instance_model = form.save()
            payload['ok'] = True
            payload['id'] = instance_model.id

    return HttpResponse(payload, content_type="application/json")


def get_user(request, id):
    payload = {
        'not existed': True,
    }
    if request.method == 'GET':
        user = User.objects.filter(id=id).first()
        print(user)
        if user:
            payload = json.dumps(user.as_json())

    return HttpResponse(payload, content_type="application/json")


def delete_user(request, id):
    payload = {
        'delete fail': True,
    }
    if request.method == 'GET':
        user = User.objects.filter(id=id).first()
        if user:
            user.delete()
            payload={
                'user_deleted': True
            }

    return HttpResponse(payload, content_type="application/json")


