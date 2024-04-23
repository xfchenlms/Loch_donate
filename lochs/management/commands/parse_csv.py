import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from lochs.models import Loch

class Command(BaseCommand):
    help = 'Load data from csv'
    
    def handle(self, *args, **options):
        
        # drop the data from the table so that if we rerun the file, we don't repeat values
        Loch.objects.all().delete()
        print("table dropped successfully")
        # create table again
        
        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/lochs/data/Lochs_in_Scotland.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)
                
                loch = Loch.objects.create(
                ObjectID = int(row[0]),
                LochCode = row[1],
                SurfaceArea = float(row[2]),
                AuthID = row[3],
                LochAuth = row[4],
                IslandName = row[5],
                LochName = row[6],
                Price = int(row[7]),
                )
                loch.save()
        print("data parsed successfully")