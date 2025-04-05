# Generated by Django 5.1.2 on 2025-04-05 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0006_postapplication"),
    ]

    operations = [
        migrations.AddField(
            model_name="postapplication",
            name="cv",
            field=models.ForeignKey(
                blank=True,
                help_text="CV utilisé pour la candidature",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="post.pdfdocument",
            ),
        ),
        migrations.AddField(
            model_name="postapplication",
            name="interview",
            field=models.ForeignKey(
                blank=True,
                help_text="Entretien lié à la candidature",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="post.interviewresponse",
            ),
        ),
    ]
