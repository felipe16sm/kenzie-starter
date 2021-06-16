import csv
import pytz
from django.core.management.base import BaseCommand
from datetime import datetime, tzinfo
from kenzie_starter_app.models import Category, Creator, Location, Project, Subcategory

import ipdb


class Command(BaseCommand):
    help = "Populate database"

    def add_arguments(self, parser):
        parser.add_argument("projects", help="Projects file")

    def handle(self, *args, **kwargs):
        projects = kwargs["projects"]

        with open(projects) as file:
            csv_data = csv.DictReader(file, delimiter=",")

            counter = 0
            lines = 0

            # Contar a quantidade de linhas
            for line in file:
                lines += 1

            file.seek(0)

            for row in csv_data:

                creator = Creator.objects.get_or_create(
                    name=row["creator_name"], slug=row["creator_slug"]
                )[0]

                location = Location.objects.get_or_create(
                    country=row["location_country"],
                    country_full=row["location_expanded_country"],
                    state=row["location_state"],
                    localized_name=row["location_localized_name"],
                    name=row["location_name"],
                )[0]

                category = Category.objects.get_or_create(name=row["category_name"])[0]

                subcategory = Subcategory.objects.get_or_create(
                    name=row["subcategory"], category_id=category.id
                )[0]

                project = Project.objects.get_or_create(
                    name=row["name"],
                    description=row["blurb"],
                    backers=row["backers_count"],
                    created_at=datetime.fromtimestamp(
                        int(row["created_at"]), tz=pytz.UTC
                    ),
                    deadline=datetime.fromtimestamp(int(row["deadline"]), tz=pytz.UTC),
                    goal=row["goal"],
                    pledged=row["pledged"],
                    usd_pledged=row["usd_pledged"],
                    currency=row["currency"],
                    launched_at=datetime.fromtimestamp(
                        int(row["launched_at"]), tz=pytz.UTC
                    ),
                    state=row["state"],
                    state_changed_at=datetime.fromtimestamp(
                        int(row["state_changed_at"]), tz=pytz.UTC
                    ),
                    subcategory_id=subcategory.id,
                    creator_id=creator.id,
                    location_id=location.id,
                )[0]

                # ipdb.set_trace()

                counter += 1

                if counter % 100 == 0:
                    self.stdout.write(f"\tProcessed {counter} of {lines}")
