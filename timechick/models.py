from django.db import models


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
        max_length=128, default="", verbose_name='电话', unique=True, blank=True)
    sex = models.CharField(max_length=32, choices=gender,
                           default="男", verbose_name='性别', blank=True)
    is_delete = models.BooleanField(
        default=False, blank=True, verbose_name='是否删除')
    note = models.TextField(
        max_length=256, default="", blank=True, verbose_name='备注')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mobile

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
    url = models.CharField(max_length=512, default="", verbose_name='歌曲地址')
    album_img = models.CharField(
        max_length=128, default="", blank=True, verbose_name='专辑封面')
    artist_img = models.CharField(
        max_length=128, default="", blank=True, verbose_name='艺术家图片')
    type = models.CharField(max_length=32, blank=True,
                            choices=gender, verbose_name='歌曲类型')
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
    gender = (
        ('public', "通用音乐"),
        ('mainland', "大陆红歌"),
        ('taiwan', "台语歌"),
        ('japanese', "日语歌"),
    )
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE, default="", verbose_name='用户')
    song = models.ForeignKey(
        'Song', on_delete=models.CASCADE, default="", verbose_name='歌曲')
    emotion = models.CharField(
        max_length=128, default="", verbose_name='情绪')
    type = models.CharField(max_length=32, blank=True,
                            choices=gender, verbose_name='歌曲类型')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["create_time"]
        verbose_name = "歌单"
        verbose_name_plural = "歌单"
