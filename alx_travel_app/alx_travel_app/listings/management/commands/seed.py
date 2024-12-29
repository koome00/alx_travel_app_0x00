import random
from django.core.management.base import BaseCommand
from listings.models import Property
from faker import Faker

class Command(BaseCommand):
    help = "Populates the database with sample listings data."

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Delete existing data to avoid duplicates
        Property.objects.all().delete()

        # Generate sample data
        listings = []
        for _ in range(50):  # Create 50 sample listings
            listings.append(
                Property(
                    name=fake.company(),
                    description=fake.text(max_nb_chars=200),
                    location=fake.city(),
                    price_per_night=round(random.uniform(50, 500), 2),
                    created_at=fake.date_time_this_year(),
                    updated_at=fake.date_time_this_year(),
                )
            )

        # Bulk create listings
        Property.objects.bulk_create(listings)

        self.stdout.write(self.style.SUCCESS(f"Successfully created 50 sample listings."))
