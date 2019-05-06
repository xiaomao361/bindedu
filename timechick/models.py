from django.db import models

# Create your models here.


class User(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    first_name = models.CharField(
        max_length=128, default="", blank=True, verbose_name='姓')
    last_name = models.CharField(
        max_length=128, default="", blank=True, verbose_name='名')
    email = models.EmailField(default="", verbose_name='邮件', blank=True)
    mobile = models.CharField(
        max_length=128, default="", verbose_name='电话', blank=True)
    sex = models.CharField(max_length=32, choices=gender,
                           default="男", verbose_name='性别', blank=True)
    baidu_id = models.CharField(
        max_length=128, unique=True, verbose_name='百度ID')
    is_delete = models.BooleanField(
        default=False, blank=True, verbose_name='是否删除')
    note = models.TextField(
        max_length=256, default="", blank=True, verbose_name='备注')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.baidu_id

    class Meta:
        ordering = ["create_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class Song(models.Model):
    gender = (
        ('public', "通用音乐"),
        ('mainland', "大陆红歌"),
        ('taiwan', "台语歌"),
        ('japanese', "日语歌"),
    )

    name = models.CharField(
        max_length=128, default="", verbose_name='歌曲名称')
    artist = models.CharField(
        max_length=128, default="未知艺术家", verbose_name='艺术家')
    url = models.CharField(max_length=128, default="", verbose_name='歌曲地址')
    album_img = models.CharField(
        max_length=128, default="", verbose_name='专辑封面')
    artist_img = models.CharField(
        max_length=128, default="", verbose_name='艺术家图片')
    type = models.CharField(max_length=32, choices=gender, verbose_name='歌曲类型')
    is_shelf = models.BooleanField(
        default=True, verbose_name='是否上架')
    corpus_a = models.TextField(
        max_length=256, default="", blank=True, verbose_name='语料A')
    corpus_b = models.TextField(
        max_length=256, default="", blank=True, verbose_name='语料B')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["create_time"]
        verbose_name = "歌曲"
        verbose_name_plural = "歌曲"


class PlayList(models.Model):
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE, default="", verbose_name='用户')
    song = models.ForeignKey(
        'Song', on_delete=models.CASCADE, default="", verbose_name='歌曲')
    emotion = models.CharField(
        max_length=128, default="", verbose_name='情绪')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ["create_time"]
        verbose_name = "歌单"
        verbose_name_plural = "歌单"

#  response object


class ExpectResponse(models.Model):
    type = models.CharField(max_length=128, default="")
    text = models.CharField(max_length=128, default="")
    slot = models.CharField(max_length=128, default="")


class Slots(models.Model):
    slot = models.CharField(max_length=128, default="")
    name = models.CharField(max_length=128, default="")
    value = models.CharField(max_length=128, default="")


class Intent(models.Model):
    name = models.CharField(max_length=128, default="")
    slots = models.ForeignKey(
        'Slots', on_delete=models.CASCADE, default="")


class Context(models.Model):
    intent = models.ForeignKey(
        'Slots', on_delete=models.CASCADE, default="")
    expectResponse = models.ForeignKey(
        'ExpectResponse', on_delete=models.CASCADE, default="")


class Attributes(models.Model):
    key = models.CharField(max_length=128, default="")
    val = models.CharField(max_length=128, default="")


class Session(models.Model):
    attributes = models.ForeignKey(
        'Attributes', on_delete=models.CASCADE, default="")


class OutputSpeech(models.Model):
    type = models.CharField(max_length=128, default="")
    text = models.CharField(max_length=128, default="")
    ssml = models.CharField(max_length=128, default="")


class Reprompt(models.Model):
    outputSpeech = models.ForeignKey(
        'OutputSpeech', on_delete=models.CASCADE, default="")


class Response(models.Model):
    outputSpeech = models.ForeignKey(
        'OutputSpeech', on_delete=models.CASCADE, default="")
    reprompt = models.ForeignKey(
        'Reprompt', on_delete=models.CASCADE, default="")
    card = models.CharField(max_length=128, default="")
    directives = models.CharField(max_length=128, default="")
    expectSpeech = models.BooleanField(default=False, blank=True)
    shouldEndSession = models.BooleanField(default=False, blank=True)
