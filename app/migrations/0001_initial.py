# Generated by Django 4.0 on 2022-02-18 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('isbn', models.PositiveIntegerField()),
                ('author', models.CharField(max_length=40)),
                ('category', models.CharField(choices=[('education', 'Education'), ('entertainment', 'Entertainment'), ('comics', 'Comics'), ('biography', 'Biography'), ('history', 'History'), ('novel', 'Novel'), ('fantasy', 'Fantasy'), ('thriller', 'Thriller')], default='education', max_length=30)),
            ],
        ),
    ]
