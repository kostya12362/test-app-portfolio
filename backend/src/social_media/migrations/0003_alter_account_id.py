# Generated by Django 5.1.6 on 2025-03-14 16:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("social_media", "0002_remove_account_accounts_social__2f66b2_idx_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
