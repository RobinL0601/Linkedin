from django.core.management.base import BaseCommand
import pandas as pd
from core.models import JobPosting
from pathlib import Path

class Command(BaseCommand):
    help = 'Import job postings from CSV file'

    def handle(self, *args, **kwargs):
        # Get the base directory of your project
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        csv_file = base_dir / 'dataset' / 'Referral List.csv'
        
        # Delete existing job postings
        JobPosting.objects.all().delete()
        
        # Read CSV file using pandas
        df = pd.read_csv(csv_file)
        
        # Create job postings from DataFrame
        for _, row in df.iterrows():
            JobPosting.objects.create(
                company_name=row['CompanyName'],
                job_url=row['URL']
            )
        
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {len(df)} job postings')) 