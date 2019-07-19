from django.shortcuts import render
import json
import requests
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


def check_type(user_id, type):
    type_listened_array = []
    type_songs_array = []
    try:
        type_listened_list = models.PlayList.objects.filter(
            user_id=user_id, emotion=2, type=type)
        if len(type_listened_list) == 1:
            type_songs = models.Song.objects.filter(type=type)
            for type_song in type_songs:
                if type_song.is_shelf == 1 and type_song.id != type_listened_list[0].song_id:
                    type_songs_array.append(type_song.id)
        elif len(type_listened_list) == 2:
            print(
                "There are more than two songs of this type that have never been heard of")
        elif len(type_listened_list) == 0:
            type_songs = models.Song.objects.filter(type=type)
            for type_song in type_songs:
                if type_song.is_shelf == 1:
                    type_songs_array.append(type_song.id)
        else:
            print("Illegal operation")
    except Exception as e:
        print(e)
    return type_songs_array


def public_residue(user_id):
    array = []
    listened_list = models.PlayList.objects.filter(
        user_id=user_id, type='public')
    listened_array = []
    for listened in listened_list:
        listened_array.append(listened.song_id)
    public_songs = models.Song.objects.filter(type='public')
    for song in public_songs:
        if song.is_shelf == 1 and song.id not in listened_array:
            array.append(song.id)
    return array


@csrf_exempt
def get_index_list(request):
    if request.method == "POST":
        phone = request.POST['phone'].replace(' ', '')
        list = []
        music = []
        try:
            user = models.User.objects.get(mobile=phone)
            taiwan_dic = check_type(user.id, 'taiwan')
            mainland_dic = check_type(user.id, 'mainland')
            japanese_dic = check_type(user.id, 'japanese')
            public_dic = public_residue(user.id)
            song_list = taiwan_dic + mainland_dic + japanese_dic + japanese_dic
            i = 0
            while(len(list) < 4):
                song = models.Song.objects.get(id=song_list[i])
                if song.is_shelf == 1 and song_list[i] not in list:
                    list.append(song_list[i])
                    dic = make_response(song_list[i], song.url, song.artist, song.name,
                                        song.album_img, song.artist_img, song.corpus_a, song.corpus_b)
                    music.append(dic)
                i = i + 1
            return HttpResponse(json.dumps(music), content_type="application/json")
        except:
            models.User.objects.create(mobile=phone)
            songs = models.Song.objects.all()
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
def add_playlist(request):
    if request.method == "POST":
        phone = request.POST['phone'].replace(' ', '')
        id = request.POST['id'].replace(' ', '')
        emotion = request.POST['emotion'].replace(' ', '')
        user_id = models.User.objects.get(mobile=phone).id
        type = models.Song.objects.get(id=id).type
        models.PlayList.objects.create(
            song_id=id, user_id=user_id, emotion=emotion, type=type)
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


def type_music_residue(user_id, type):
    array = []
    listened_list = models.PlayList.objects.filter(
        user_id=user_id, type=type)
    listened_array = []
    for listened in listened_list:
        listened_array.append(listened.song_id)
    type_songs = models.Song.objects.filter(type=type)
    for song in type_songs:
        if song.is_shelf == 1 and song.id not in listened_array:
            array.append(song.id)
    return array

def type_music(type):
    array = []
    type_songs = models.Song.objects.filter(type=type)
    for song in type_songs:
        if song.is_shelf == 1 and song.id:
            array.append(song.id)
    return array


@csrf_exempt
def get_list_with_phone(request):
    if request.method == "POST":
        list = []
        music = []
        phone = request.POST['phone'].replace(' ', '')
        if len(phone) == 11:
            print("dalu")
            try:
                user = models.User.objects.get(mobile=phone)
                listened_list = models.PlayList.objects.filter(
                    user_id=user.id)
                listened_array = []
                for listened in listened_list:
                    listened_array.append(listened.song_id)
                mainland_dic = type_music_residue(user.id, 'mainland')
                public_dic = type_music_residue(user.id, 'public')
                song_list = mainland_dic + public_dic
                while(len(list) < 4):
                    id = random.randint(1, len(song_list))
                    song = models.Song.objects.get(id=song_list[id])
                    if song.is_shelf == 1 and song_list[id] not in list:
                        list.append(song_list[id])
                        dic = make_response(song_list[id], song.url, song.artist, song.name,
                                            song.album_img, song.artist_img, song.corpus_a, song.corpus_b)
                        music.append(dic)
                return HttpResponse(json.dumps(music), content_type="application/json")
            except:
                models.User.objects.create(mobile=phone)
                mainland_dic = type_music('mainland')
                public_dic = type_music('public')
                song_list = mainland_dic + public_dic
                while(len(list) < 4):
                    id = random.randint(1, len(song_list))
                    song = models.Song.objects.get(id=song_list[id])
                    if song.is_shelf == 1 and song_list[id] not in list:
                        list.append(song_list[id])
                        dic = make_response(song_list[id], song.url, song.artist, song.name,
                                            song.album_img, song.artist_img, song.corpus_a, song.corpus_b)
                        music.append(dic)
                return HttpResponse(json.dumps(music), content_type="application/json")
        elif len(phone) == 10:
            try:
                user = models.User.objects.get(mobile=phone)
                listened_list = models.PlayList.objects.filter(
                    user_id=user.id)
                listened_array = []
                for listened in listened_list:
                    listened_array.append(listened.song_id)
                taiwan_dic = type_music_residue(user.id, 'taiwan')
                japanese_dic = type_music_residue(user.id, 'japanese')
                public_dic = type_music_residue(user.id, 'public')
                song_list = taiwan_dic + japanese_dic + public_dic
                while(len(list) < 4):
                    id = random.randint(1, len(song_list))
                    song = models.Song.objects.get(id=song_list[id])
                    if song.is_shelf == 1 and song_list[id] not in list:
                        list.append(song_list[id])
                        dic = make_response(song_list[id], song.url, song.artist, song.name,
                                            song.album_img, song.artist_img, song.corpus_a, song.corpus_b)
                        music.append(dic)
                return HttpResponse(json.dumps(music), content_type="application/json")
            except:
                models.User.objects.create(mobile=phone)
                taiwan_dic = type_music('taiwan')
                japanese_dic = type_music('japanese')
                public_dic = type_music('public')
                song_list = taiwan_dic + japanese_dic + public_dic
                while(len(list) < 4):
                    id = random.randint(1, len(song_list))
                    song = models.Song.objects.get(id=song_list[id])
                    if song.is_shelf == 1 and song_list[id] not in list:
                        list.append(song_list[id])
                        dic = make_response(song_list[id], song.url, song.artist, song.name,
                                            song.album_img, song.artist_img, song.corpus_a, song.corpus_b)
                        music.append(dic)
                return HttpResponse(json.dumps(music), content_type="application/json")
        else:
            print("wrong phone number")
    else:
        resp = {
            'code': '403',
            'message': 'wrong method, need POST',
        },
        return HttpResponse(json.dumps(resp), status='403', content_type="application/json")

    # check the city with phone numno
    # url = "https://tcc.taobao.com/"
    # if request.method == "POST":
    #     phone = request.POST['phone'].replace(' ', '')
    #     r = requests.get(url + 'cc/json/mobile_tel_segment.htm', params={'tel': phone})
    #     return HttpResponse(r.text, status='200', content_type="application/json")
    # else:
    #     pass
