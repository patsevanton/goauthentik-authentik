# Generated by Django 3.0.6 on 2020-06-06 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("passbook_providers_saml", "0002_default_saml_property_mappings"),
    ]

    operations = [
        migrations.AddField(
            model_name="samlprovider",
            name="sp_binding",
            field=models.TextField(
                choices=[("redirect", "Redirect"), ("post", "Post")], default="redirect"
            ),
        ),
    ]
