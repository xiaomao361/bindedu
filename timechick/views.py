from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from timechick import models
from django.forms.models import model_to_dict
from timechick import tresponse

@csrf_exempt
def launch_request(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body)

        # context
        context = {}
        intent = tresponse.Intent('')
        expectResponse = tresponse.ExpectResponse('', '', '')
        context['intent'] = intent.__dict__
        context['expectResponse'] = []
        context['expectResponse'].append(expectResponse.__dict__)

        # session 
        received_session = received_json_data['session']
        session = {}
        attributes = tresponse.Attributes(received_session['new'], received_session['sessionId'])
        session['attributes'] = attributes.__dict__
        
        # response
        response = {}
        outputSpeech = tresponse.OutputSpeech('PlainText', '欢迎', '')
        response['outputSpeech'] = outputSpeech.__dict__
        response['reprompt'] = {}
        response['card'] = {}
        response['directives'] = []
        response['expectSpeech'] = False
        response['shouldEndSession'] = False

        # data
        data = {}
        data['version'] = "2.0"
        data['context'] = context
        data['session'] = session
        data['response'] = response
        print(data)
        return HttpResponse(json.dumps(data), content_type="application/json")


def ended_request(self):
    if request.method == "POST":
        received_json_data = json.loads(request.body)
        return HttpResponse(json.dumps(received_json_data), content_type="application/json")
