from unittest.mock import MagicMock
import pytest
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    dir_1 = Director(id=1, name='Peppa')
    dir_2 = Director(id=2, name='Dambldor')
    dir_3 = Director(id=3, name='Stas')

    director_dao.get_one = MagicMock(return_value=dir_1)
    director_dao.get_all = MagicMock(return_value=[dir_1, dir_2, dir_3])
    director_dao.create = MagicMock(return_value=dir_3)
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    gen_1 = Genre(id=1, name='TraliVali')
    gen_2 = Genre(id=2, name='FireInTheHole')
    gen_3 = Genre(id=3, name='Stas')

    genre_dao.get_one = MagicMock(return_value=gen_1)
    genre_dao.get_all = MagicMock(return_value=[gen_1, gen_2, gen_3])
    genre_dao.create = MagicMock(return_value=gen_3)
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()
    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    mov_1 = Movie(id=1, title='DonniDanko', description='Adventures Donni Danko', trailer='youtube/1', year=1999,
                  rating=6.7, genre_id=1, director_id=1)
    mov_2 = Movie(id=2, title='Karol Lion', description='Adventures Karola Liona', trailer='youtube/2', year=2005,
                  rating=7.6, genre_id=2, director_id=2)
    mov_3 = Movie(id=3, title='Stas', description='Adventures Stas', trailer='youtube/3', year=1895,
                  rating=0.1, genre_id=2, director_id=2)

    movie_dao.get_one = MagicMock(return_value=mov_1)
    movie_dao.get_all = MagicMock(return_value=[mov_1, mov_2, mov_3])
    movie_dao.create = MagicMock(return_value=mov_3)
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


