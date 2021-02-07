# Generated by Django 3.1.6 on 2021-02-07 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('unit', models.CharField(choices=[('g', 'Gram'), ('kg', 'Kilogram'), ('cal', 'Calorie'), ('kcal', 'Kilocalorie')], default='g', max_length=5)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]