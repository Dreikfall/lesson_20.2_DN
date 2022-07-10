import pytest
from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None
        assert isinstance(movie.id, int)

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            'title': 'Donald *uck',
            'description': 'Adventures Donalda',
            'trailer': 'youtube/4',
            'year': 1999,
            'rating': 7.8,
            'genre_id': 4,
            'director_id': 4
        }
        movie = self.movie_service.create(movie_d)
        assert movie.id is not None
        assert movie.title == 'Stas'
        assert movie.year == 1895

    def test_delete(self):
        res = self.movie_service.delete(1)
        assert res is None

    def test_update(self):
        movie_d = {
            'id': 2,
            'title': 'Bukin',
            'description': 'Adventures Bukin and family',
            'trailer': 'youtube/5',
            'year': 2004,
            'rating': 8.4,
            'genre_id': 5,
            'director_id': 5
        }
        self.movie_service.update(movie_d)

