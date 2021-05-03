# Generated by Django 3.1.7 on 2021-05-02 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='root', max_length=50)),
                ('biography', models.CharField(default='N/A', max_length=100)),
                ('language', models.CharField(choices=[('English', 'English'), ('Bangla', 'Bangla')], default='English', max_length=7)),
                ('city', models.CharField(default='Dhaka', max_length=20)),
                ('website', models.CharField(default='N/A', max_length=20)),
                ('zipcode', models.IntegerField(default='zipcode')),
                ('state', models.CharField(choices=[('Ghorashal', 'Ghorashal'), ('Monohardi', 'Monohardi'), ('Shibpur', 'Shibpur'), ('Raipura', 'Raipura'), ('Madhabdi', 'Madhabdi'), ('Mirzapur', 'Mirzapur'), ('Dhanbari', 'Dhanbari'), ('Madhupur', 'Madhupur'), ('Chhagalnaiya', 'Chhagalnaiya'), ('Parshuram', 'Parshuram'), ('Bandarban', 'Bandarban'), ('Rangamati', 'Rangamati')], default='Dhaka', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.CharField(max_length=200)),
                ('level', models.CharField(choices=[('Beginner', 'Beginner'), ('Advanced', 'Advanced'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')], default='Not sure', max_length=20)),
                ('category', models.CharField(choices=[('Py', 'python'), ('DS', 'Data Science'), ('ML', 'Machine Learning'), ('DL', 'Deep Learning')], default=None, max_length=2)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='productimg')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('university_name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('Py', 'python'), ('DS', 'Data Science'), ('ML', 'Machine Learning'), ('DL', 'Deep Learning')], max_length=2)),
                ('experience', models.CharField(choices=[('Proffesional ', 'Proffesional'), ('Taught before casually', 'Taught before casually'), ('Never Taught', 'Never Taught')], max_length=30)),
                ('time_invest', models.CharField(choices=[('I am very busy at the time (0-2 hours)', 'I am very busy at the time (0-2 hours)'), ('Work on free time (2-4 hours)', 'Work on free time (2-4 hours)'), ('I have a lot of flexibility (5+ hours)', 'I have a lot of flexibility (5+ hours)'), ('Not Decided', 'Not Decided')], max_length=100)),
                ('biography', models.CharField(default='N/A', max_length=100)),
                ('language', models.CharField(choices=[('English', 'English'), ('Bangla', 'Bangla')], default='English', max_length=7)),
                ('city', models.CharField(default='Dhaka', max_length=20)),
                ('website', models.CharField(default='N/A', max_length=20)),
                ('customer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=30)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]