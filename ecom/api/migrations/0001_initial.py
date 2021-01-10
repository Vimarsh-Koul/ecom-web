from django.db import migrations
from api.user.models import customuser

class Migration(migrations.Migration):
    def seed_data(self,apps, schema_editor):
        user = customuser(name="vimarsh",
        email="vimarsh@company.com",
        is_staff=True,
        is_superuser=True,
        phone="123456789",
        gender="Male"
        )

        user.set_password("12345")
        user.save()

    
    dependencies = [
      
    ]

    operations =[
        migrations.RunPython(seed_data),
    ]