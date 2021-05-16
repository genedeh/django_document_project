# Generated by Django 3.2.3 on 2021-05-16 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='doc_img',
            field=models.ImageField(default='/static/doc_image.png', upload_to='', verbose_name='document_img'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_name',
            field=models.CharField(blank=True, default='Document771995992012537', max_length=120, unique=True, verbose_name='document_name'),
        ),
    ]
