# Generated by Django 2.1.2 on 2018-10-16 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork_image_processor', '0002_auto_20181011_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('imageFile', models.ImageField(upload_to='static/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
