from django import forms

from common.session_decorator import session_decorator
from musicApp.settings import session
from musics.models import Album


class AlbumBaseForm(forms.Form):
    album_name = forms.CharField(
        label="Album Name:",
        max_length=30,
        required=True,
    )

    image_url = forms.URLField(
        label="Image URL:",
        required=True,
    )

    price = forms.DecimalField(
        label="Price:",
        min_value=0.0,
        required=True,
    )


class AlbumCreateForm(AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(AlbumBaseForm):
    pass


class SongBaseForm(forms.Form):
    song_name = forms.CharField(
        label='Song Name:',
        max_length=30,
        required=True,
    )

    album = forms.ChoiceField(
        label="Album:",
        choices=[],
    )

    @session_decorator(session)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        albums = session.query(Album).all()
        self.fields['album'].choices = [(album.id, album.album_name) for album in albums]


class SongCreateForm(SongBaseForm):
    music_file_data = forms.FileField(
        label="Music File:",
        required=True,
    )
