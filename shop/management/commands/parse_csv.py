import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from shop.models import Product

#We use the command tools so that we gain access to our models and database connections
#https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/ 


class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        # drop the data from the table so that if we rerun the file, we don't repeat values
        Product.objects.all().delete()
        print("table dropped successfully")
        # create table again

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        #   Dataset below contains more than 30,000 rows of data so we will use a sample of 4,000 rows
        with open(str(base_dir) + '/shop/kaggle_dataset/walmart_product_data_2019/marketing_sample_for_walmart_com-ecommerce__20191201_20191231__4k_data.csv', newline='', encoding="utf8") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)
                product = Product.objects.create(
                name = row[4],
                price = float(row[6]),
                )
                product.save()

        print("data parsed successfully")