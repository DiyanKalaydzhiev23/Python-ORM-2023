from django.db import models

# showmigrations
# sqlmigrate main_app 0001_initial
class Shoe(models.Model):
    brand = models.CharField(
        max_length=25,
    )

    size = models.PositiveIntegerField()


# makemigrations main_app --name migrate_unique_brands --empty
class UniqueBrands(models.Model):
    brand_name = models.CharField(
        max_length=25,
    )


class EventRegistration(models.Model):
    event_name = models.CharField(
        max_length=60,
    )

    participant_name = models.CharField(
        max_length=50,
    )

    registration_date = models.DateField()

    def __str__(self):
        return f"{self.participant_name} - {self.event_name}"


class Student(models.Model):
    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
    )

    age = models.PositiveIntegerField()

    grade = models.CharField(
        max_length=10,
    )

    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Supplier(models.Model):
    name = models.CharField(
        max_length=100,
    )

    contact_person = models.CharField(
        max_length=50,
    )

    email = models.EmailField(
        unique=True,
    )

    phone = models.CharField(
        max_length=20,
        unique=True,
    )

    address = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.phone}"


# makemigrations main_app --name migrate_age_group --empty
class Person(models.Model):
    name = models.CharField(
        max_length=40,
    )

    age = models.PositiveIntegerField()

    age_group = models.CharField(
        max_length=20,
        default='No age group',
    )

    def __str__(self):
        return f"Name: {self.name}"


class Smartphone(models.Model):
    brand = models.CharField(
        max_length=100,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=1,
    )

    category = models.CharField(
        max_length=20,
        default="empty",
    )


class Order(models.Model):
    STATUS_CHOICES = (
        ("P", "Pending"),
        ("Cpd", "Completed"),
        ("Cnd", "Cancelled"),
    )

    product_name = models.CharField(
        max_length=30,
    )

    customer_name = models.CharField(
        max_length=100,
    )

    order_date = models.DateField()

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
    )

    amount = models.PositiveIntegerField(
        default=1,
    )

    product_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    warranty = models.CharField(
        max_length=100,
        default="No warranty",
    )

    delivery = models.DateField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Order #{self.pk} - {self.customer_name}"
