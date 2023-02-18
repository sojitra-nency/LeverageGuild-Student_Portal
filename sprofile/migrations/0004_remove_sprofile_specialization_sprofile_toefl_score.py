# Generated by Django 4.1.5 on 2023-02-02 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "sprofile",
            "0003_sprofile_gre_score_sprofile_ilets_score_sprofile_lor_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(model_name="sprofile", name="specialization",),
        migrations.AddField(
            model_name="sprofile",
            name="toefl_score",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
