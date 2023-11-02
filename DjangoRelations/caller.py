import os
from datetime import date, timedelta
from typing import List

import django

# Set up Django
from django.db.models import QuerySet, Sum, Count

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Author, Book, Artist, Song, Product, Review, DrivingLicense, Driver, Owner, Registration, \
    Car


def show_all_authors_with_their_books() -> str:
    authors_with_books = []

    authors = Author.objects.all().order_by('id')  # better way to do it with prefetch

    for author in authors:
        books = Book.objects.filter(author=author)

        if not books:
            continue

        titles = ', '.join(book.title for book in books)
        authors_with_books.append(f"{author.name} has written - {titles}!")

    return '\n'.join(authors_with_books)


def delete_all_authors_without_books() -> None:
    Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str) -> QuerySet[Song]:
    artist = Artist.objects.get(name=artist_name)
    return artist.songs.all().order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str) -> float:
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()

    total_rating = sum(r.rating for r in reviews)
    average_rating = total_rating / len(reviews)

    return average_rating

    # better way
    # product = Product.objects.annotate(
    #     total_ratings=Sum('review__rating'),
    #     num_reviews=Count('review')
    # ).get(name=product_name)
    #
    # average_rating = product.total_ratings / product.num_reviews
    #
    # return average_rating


def get_reviews_with_high_ratings(threshold: int) -> QuerySet[Review]:
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews() -> QuerySet[Product]:
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews() -> None:
    Product.objects.filter(reviews__isnull=True).delete()


def calculate_licenses_expiration_dates() -> str:
    licenses = DrivingLicense.objects.order_by('-license_number')

    return '\n'.join(str(l) for l in licenses)


def get_drivers_with_expired_licenses(due_date: date) -> QuerySet[Driver]:
    expiration_cutoff_date = due_date - timedelta(days=365)

    expired_drivers = Driver.objects.filter(drivinglicense__issue_date__gt=expiration_cutoff_date)

    return expired_drivers


def register_car_by_owner(owner: Owner) -> str:
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True, owner=owner).first()

    car.owner = owner
    car.registration = registration

    car.save()

    registration.registration_date = date.today()
    registration.car = car

    registration.save()

    return f"Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}."


