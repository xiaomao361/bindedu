# Generated by Django 2.2 on 2019-05-06 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timechick', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='', max_length=128)),
                ('val', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ExpectResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='', max_length=128)),
                ('text', models.CharField(default='', max_length=128)),
                ('slot', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='OutputSpeech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='', max_length=128)),
                ('text', models.CharField(default='', max_length=128)),
                ('ssml', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Reprompt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outputSpeech', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='timechick.OutputSpeech')),
            ],
        ),
        migrations.CreateModel(
            name='Slots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(default='', max_length=128)),
                ('name', models.CharField(default='', max_length=128)),
                ('value', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attributes', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='timechick.Attributes')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.CharField(default='', max_length=128)),
                ('directives', models.CharField(default='', max_length=128)),
                ('expectSpeech', models.BooleanField(blank=True, default=False)),
                ('shouldEndSession', models.BooleanField(blank=True, default=False)),
                ('outputSpeech', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='timechick.OutputSpeech')),
                ('reprompt', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='timechick.Reprompt')),
            ],
        ),
        migrations.CreateModel(
            name='Intent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('slots', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='timechick.Slots')),
            ],
        ),
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expectResponse', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='timechick.ExpectResponse')),
                ('intent', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='timechick.Slots')),
            ],
        ),
    ]