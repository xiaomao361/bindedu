from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


def make_respone(session, context, response):
    dict = {}
    dict['version'] = '2.0'
    dict['session'] = session
    dict['context'] = context
    dict['response'] = response
    return dict


@csrf_exempt
def launch_request(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body)
        print(received_json_data)
        return HttpResponse(json.dumps(received_json_data), content_type="application/json")


def ended_request(self):
    if request.method == "POST":
        received_json_data = json.loads(request.body)
        return HttpResponse(json.dumps(received_json_data), content_type="application/json")
