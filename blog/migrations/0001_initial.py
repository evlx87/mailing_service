# Generated by Django 4.2.7 on 2024-02-16 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('content', models.TextField(blank=True, null=True, verbose_name='содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='app_blog/', verbose_name='изображение')),
                ('views_count', models.IntegerField(default=0, verbose_name='просмотры')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
            ],
            options={
                'verbose_name': 'публикация',
                'verbose_name_plural': 'публикации',
                'ordering': ('-date_create',),
            },
        ),
    ]
