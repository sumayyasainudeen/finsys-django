# Generated by Django 4.1.4 on 2023-05-22 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0077_alter_retainerinvoices_invoice_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retainerinvoices',
            name='never_expiring',
        ),
    ]
