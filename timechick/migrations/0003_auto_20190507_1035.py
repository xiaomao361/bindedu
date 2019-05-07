# Generated by Django 2.2 on 2019-05-07 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timechick', '0002_attributes_context_expectresponse_intent_outputspeech_reprompt_response_session_slots'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='context',
            name='expectResponse',
        ),
        migrations.RemoveField(
            model_name='context',
            name='intent',
        ),
        migrations.RemoveField(
            model_name='intent',
            name='slots',
        ),
        migrations.RemoveField(
            model_name='reprompt',
            name='outputSpeech',
        ),
        migrations.RemoveField(
            model_name='response',
            name='outputSpeech',
        ),
        migrations.RemoveField(
            model_name='response',
            name='reprompt',
        ),
        migrations.RemoveField(
            model_name='session',
            name='attributes',
        ),
        migrations.DeleteModel(
            name='Attributes',
        ),
        migrations.DeleteModel(
            name='Context',
        ),
        migrations.DeleteModel(
            name='ExpectResponse',
        ),
        migrations.DeleteModel(
            name='Intent',
        ),
        migrations.DeleteModel(
            name='OutputSpeech',
        ),
        migrations.DeleteModel(
            name='Reprompt',
        ),
        migrations.DeleteModel(
            name='Response',
        ),
        migrations.DeleteModel(
            name='Session',
        ),
        migrations.DeleteModel(
            name='Slots',
        ),
    ]