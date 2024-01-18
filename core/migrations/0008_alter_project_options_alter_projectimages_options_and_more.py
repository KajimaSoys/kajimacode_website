# Generated by Django 4.1.5 on 2024-01-18 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_skill_options_alter_skill_skill_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['order'], 'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterModelOptions(
            name='projectimages',
            options={'ordering': ['order'], 'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['order'], 'verbose_name': 'Навык', 'verbose_name_plural': 'Навыки'},
        ),
        migrations.AddField(
            model_name='project',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Порядок'),
        ),
        migrations.AddField(
            model_name='projectimages',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Порядок'),
        ),
        migrations.AddField(
            model_name='skill',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Порядок'),
        ),
    ]
