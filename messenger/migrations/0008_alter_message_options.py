# Generated by Django 4.2.4 on 2023-12-04 21:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("messenger", "0007_alter_room_admin"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="message",
            options={
                "ordering": ["timestamp"],
                "verbose_name": "Message",
                "verbose_name_plural": "Messages",
            },
        ),
    ]
