# Generated by Django 4.2.4 on 2023-09-10 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("friends", "0004_alter_block_to_user"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="friend",
            options={"verbose_name": "Friend", "verbose_name_plural": "Friends"},
        ),
        migrations.AlterModelOptions(
            name="friendshiprequest",
            options={
                "verbose_name": "Friendship request",
                "verbose_name_plural": "Friendship requests",
            },
        ),
        migrations.RemoveField(
            model_name="friendshiprequest",
            name="message",
        ),
        migrations.AlterField(
            model_name="friend",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="friend",
            name="from_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="friends",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="friend",
            name="to_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="_friends",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="friendshiprequest",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="friendshiprequest",
            name="from_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="friendship_requests_sent",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="friendshiprequest",
            name="rejected_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="friendshiprequest",
            name="to_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="friendship_requests_recived",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.DeleteModel(
            name="Block",
        ),
    ]
