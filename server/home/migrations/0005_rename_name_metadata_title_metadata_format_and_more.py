# Generated by Django 4.2.7 on 2023-12-24 14:57

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.search
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_metadata_home_metada_descrip_92bd52_gin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metadata',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='metadata',
            name='format',
            field=models.CharField(choices=[('pdf', 'PDF'), ('doc', 'DOC'), ('ppt', 'PPT'), ('txt', 'TXT'), ('img', 'IMG'), ('video', 'Video'), ('audio', 'Audio'), ('other', 'Other')], default='other', max_length=10),
        ),
        migrations.AddField(
            model_name='metadata',
            name='status',
            field=models.CharField(default='pending', max_length=15),
        ),
        migrations.AddField(
            model_name='metadata',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='metadata',
            name='verified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='description_vector',
            field=django.contrib.postgres.search.SearchVectorField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('hi', 'Hindi'), ('te', 'Telugu'), ('ta', 'Tamil'), ('ml', 'Malayalam'), ('kn', 'Kannada'), ('od', 'Odia'), ('bn', 'Bengali'), ('gu', 'Gujarati'), ('mr', 'Marathi'), ('pa', 'Punjabi'), ('ur', 'Urdu'), ('otr', 'Other')], default='other', max_length=3),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='meta_id',
            field=models.BigIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='states',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('ad', 'Andhra Pradesh'), ('ar', 'Arunachal Pradesh'), ('as', 'Assam'), ('br', 'Bihar'), ('cg', 'Chattisgarh'), ('dl', 'Delhi'), ('ga', 'Goa'), ('gj', 'Gujarat'), ('hr', 'Haryana'), ('hp', 'Himachal Pradesh'), ('jk', 'Jammu and Kashmir'), ('jh', 'Jharkhand'), ('ka', 'Karnataka'), ('kl', 'Kerala'), ('ld', 'Lakshadweep Islands'), ('mp', 'Madhya Pradesh'), ('mh', 'Maharashtra'), ('mn', 'Manipur'), ('ml', 'Meghalaya'), ('mz', 'Mizoram'), ('nl', 'Nagaland'), ('od', 'Odisha'), ('py', 'Pondicherry'), ('pb', 'Punjab'), ('rj', 'Rajasthan'), ('sk', 'Sikkim'), ('tn', 'Tamil Nadu'), ('ts', 'Telangana'), ('tr', 'Tripura'), ('up', 'Uttar Pradesh'), ('uk', 'Uttarakhand'), ('wb', 'West Bengal'), ('an', 'Andaman and Nicobar Islands'), ('ch', 'Chandigarh'), ('dnhdd', 'Dadra & Nagar Haveli and Daman & Diu'), ('la', 'Ladakh')], max_length=10), size=32),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='type',
            field=models.CharField(choices=[('report', 'Report'), ('case_study', 'Case Study'), ('interview', 'Interview'), ('journal_article', 'Journal Article'), ('journal_edition', 'Journal Edition'), ('study', 'Study'), ('manual', 'Manual'), ('directory', 'Directory'), ('other', 'Other')], default='other', max_length=20),
        ),
    ]
