import random
from _decimal import Decimal

from django.db.models import AutoField, PositiveIntegerField, BooleanField, CharField, TextField, EmailField, \
    DecimalField, DateField
from django.db.models.fields.related import ForeignKey, OneToOneField, ManyToManyField

from datetime import datetime, timedelta

def populate_model_with_data(model, num_records=10):
    model_fields = model._meta.fields
    model_relationships = model._meta.related_objects

    for _ in range(num_records):
        field_values = {}

        for field in model_fields:
            if hasattr(field, 'choices') and field.choices:
                random_choice = random.choice(field.choices)
                field_values[field.name] = random_choice[0]
            elif isinstance(field, AutoField):
                continue  # Skip AutoField
            elif isinstance(field, PositiveIntegerField):
                field_values[field.name] = random.randint(1, 100)
            elif isinstance(field, BooleanField):
                field_values[field.name] = random.choice([True, False])
            elif isinstance(field, CharField):
                field_values[field.name] = f"{model.__name__} {_+1}"
            elif isinstance(field, TextField):
                field_values[field.name] = f"A {model.__name__.lower()}"
            elif isinstance(field, EmailField):
                field_values[field.name] = f"{random.choice(['user', 'admin', 'customer'])}@example.com"
            elif isinstance(field, DecimalField):
                max_digits = field.max_digits
                decimal_places = field.decimal_places
                random_decimal = random.uniform(1, max_digits * 10)  # random decimal in range
                field_values[field.name] = Decimal(f"{random_decimal:.{decimal_places}f}")
            elif isinstance(field, DateField):
                # Create a random date between 2000-01-01 and today
                start_date = datetime(2000, 1, 1).date()
                end_date = datetime.today().date()
                delta = end_date - start_date
                random_days = random.randint(0, delta.days)
                field_values[field.name] = start_date + timedelta(days=random_days)
            elif isinstance(field, ForeignKey) or isinstance(field, OneToOneField):
                # Handle ForeignKey and OneToOneField relationships
                related_model = field.related_model
                field_values[field.name] = related_model.objects.order_by('?').first()
            elif isinstance(field, ManyToManyField):
                # Handle ManyToManyField relationships
                related_model = field.related_model
                field_values[field.name] = related_model.objects.order_by('?').all()

        instance = model.objects.create(**field_values)

        # If there are ManyToMany relationships, add them after creating the instance
        for field in model_relationships:
            if isinstance(field, ManyToManyField):
                related_model = field.related_model
                related_instances = related_model.objects.order_by('?')[:random.randint(1, 5)]
                setattr(instance, field.name, related_instances)
                instance.save()