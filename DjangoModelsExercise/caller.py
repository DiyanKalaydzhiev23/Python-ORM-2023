import os
import django

# Set up Django
from django.core.exceptions import ValidationError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import CustomPersonBonusExample

try:
    invalid_person = CustomPersonBonusExample(
        name="Diyan",
        age=150,
    )

    invalid_person.full_clean()
except ValidationError as e:
    print(e)