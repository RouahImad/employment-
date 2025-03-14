# Generated by Django 5.1.2 on 2025-03-14 23:11

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="PDFDocument",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Title of the PDF document", max_length=255
                    ),
                ),
                (
                    "pdf_file",
                    models.FileField(help_text="Uploaded PDF file", upload_to="pdfs/"),
                ),
                (
                    "uploaded_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Date and time when the file was uploaded",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "notification",
                    models.TextField(help_text="Message of the notification"),
                ),
                (
                    "read",
                    models.BooleanField(
                        default=False,
                        help_text="Indicates if the notification has been read",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Date and time when the notification was created",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="User receiving the notification",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(help_text="Title of the job post", max_length=200),
                ),
                (
                    "description",
                    models.TextField(help_text="Detailed description of the job post"),
                ),
                (
                    "final_date",
                    models.DateField(
                        blank=True,
                        help_text="Application deadline for the job post",
                        null=True,
                    ),
                ),
                (
                    "uploaded_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="Date and time when the post was created",
                    ),
                ),
                (
                    "accepted",
                    models.BooleanField(
                        default=False,
                        help_text="Indicates if the candidate has been accepted",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="User who created the job post",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="InterviewResponse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "question",
                    models.TextField(
                        help_text="Interview question asked to the candidate"
                    ),
                ),
                (
                    "answer",
                    models.TextField(help_text="Candidate's response to the question"),
                ),
                (
                    "timestamp",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Timestamp when the response was recorded",
                    ),
                ),
                (
                    "approved",
                    models.BooleanField(
                        default=False, help_text="Indicates if the response is approved"
                    ),
                ),
                (
                    "score",
                    models.FloatField(
                        default=0.0, help_text="Score assigned to the response"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="User who provided the response",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        help_text="Job post associated with the interview",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="post.post",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Report",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date",
                    models.DateField(
                        auto_now_add=True,
                        help_text="Date when the report was generated",
                    ),
                ),
                ("message", models.TextField(help_text="Content of the report")),
                (
                    "post",
                    models.ForeignKey(
                        help_text="Job post associated with the report",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="post.post",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="User associated with the report",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
