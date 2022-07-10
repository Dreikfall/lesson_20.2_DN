import pytest
from service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None
        assert isinstance(genre.id, int)

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        genre_d = {'name': 'Fishteh'}
        genre = self.genre_service.create(genre_d)
        assert genre.id is not None
        assert genre.name == 'Stas'

    def test_delete(self):
        res = self.genre_service.delete(1)
        assert res is None

    def test_update(self):
        genre_d = {'id': 2, 'name': 'Pokahontas'}
        self.genre_service.update(genre_d)
