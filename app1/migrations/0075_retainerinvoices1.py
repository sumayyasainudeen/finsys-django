# Generated by Django 4.1.4 on 2023-05-20 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0074_delete_retainerinvoices'),
    ]

    operations = [
        migrations.CreateModel(
            name='RetainerInvoices1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('billing_address', models.CharField(max_length=100, null=True)),
                ('invoice_date', models.DateField(null=True)),
                ('expiry_date', models.DateField(null=True)),
                ('never_expiring', models.CharField(max_length=100, null=True)),
                ('invoice_number', models.IntegerField(max_length=100, null=True)),
                ('reference_number', models.IntegerField(max_length=100, null=True)),
                ('place_of_supply', models.CharField(max_length=100, null=True)),
                ('total_amount', models.FloatField(max_length=100, null=True)),
                ('customer_notes', models.CharField(max_length=100, null=True)),
                ('terms_conditions', models.CharField(max_length=100, null=True)),
                ('comments', models.CharField(max_length=100, null=True)),
                ('attachment', models.ImageField(null=True, upload_to='retainer_invoices/')),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
    ]
