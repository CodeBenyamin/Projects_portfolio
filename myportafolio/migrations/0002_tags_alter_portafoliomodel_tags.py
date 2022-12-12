# Generated by Django 4.1.4 on 2022-12-11 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myportafolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='portafoliomodel',
            name='tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myportafolio.tags'),
        ),
    ]