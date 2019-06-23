from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from timechick import models
import random


def make_response(id, url, singer, name, album_img, artist_img, corpus_a, corpus_b):
    dic = {}
    dic['id'] = id
    dic['url'] = url
    dic['singer'] = singer
    dic['name'] = name
    dic['album_img'] = album_img
    dic['artist_img'] = artist_img
    dic['corpus_a'] = corpus_a
    dic['corpus_b'] = corpus_b
    return dic


@csrf_exempt
def get_index_list(request):
    if request.method == "POST":
        phone = request.POST['phone'].replace(' ', '')
        try:
            user = models.User.objects.get(mobile=phone)
            listened_list = models.PlayList.objects.filter(user_id=user.id)
            listened_array = []
            for listened in listened_list:
                listened_array.append(listened.id)
            songs = models.Song.objects.all()
            list = []
            music = []
            while(len(list) < 4):
                id = random.randint(1, len(songs))
                song = models.Song.objects.get(id=id)
                if song.is_shelf == 1 and id not in list and id not in listened_array:
                    list.append(id)
                    dic = make_response(id, song.url, song.artist, song.name,
                                        song.album_img, song.artist_img, song.corpus_a, song.corpus_b)
                    music.append(dic)
            return HttpResponse(json.dumps(music), content_type="application/json")
        except:
            models.User.objects.create(mobile=phone)
            songs = models.Song.objects.all()
            list = []
            music = []
            while(len(list) < 4):
                id = random.randint(1, len(songs))
                song = models.Song.objects.get(id=id)
                if song.is_shelf == 1 and id not in list:
                    list.append(id)
                    dic = make_response(id, song.url, song.artist, song.name,
                                        song.album_img, song.artist_img, song.corpus_a, song.corpus_b)
                    music.append(dic)
            return HttpResponse(json.dumps(music), content_type="application/json")
    else:
        resp = {
            'code': '403',
            'message': 'wrong method, need POST',
        },
        return HttpResponse(json.dumps(resp), status='403', content_type="application/json")


@csrf_exempt
def app_playlist(request):
    if request.method == "POST":
        phone = request.POST['phone'].replace(' ', '')
        id = request.POST['id'].replace(' ', '')
        emotion = request.POST['emotion'].replace(' ', '')
        user_id = models.User.objects.get(mobile=phone).id
        models.PlayList.objects.create(
            song_id=id, user_id=user_id, emotion=emotion)
        resp = {
            'code': '200',
            'message': 'success',
        },
        return HttpResponse(json.dumps(resp), status='200', content_type="application/json")
    else:
        resp = {
            'code': '403',
            'message': 'wrong method, need POST',
        },
        return HttpResponse(json.dumps(resp), status='403', content_type="application/json")
