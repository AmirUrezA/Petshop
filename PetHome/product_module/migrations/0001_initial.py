# Generated by Django 4.2.3 on 2023-08-12 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='عنوان')),
                ('url_title', models.SlugField(max_length=250, null=True, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='نام')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('price', models.IntegerField(null=True, verbose_name='قیمت')),
                ('count', models.IntegerField(verbose_name='تعداد')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیرفعال')),
                ('slug', models.SlugField(blank=True, default='', unique=True, verbose_name='اسلاگ')),
                ('image', models.ImageField(null=True, upload_to='product_image', verbose_name='عکس محصول')),
                ('productcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_module.productcategory', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
                'ordering': ['price'],
            },
        ),
    ]