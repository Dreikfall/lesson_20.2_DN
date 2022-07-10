import pytest
from service.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None
        assert isinstance(director.id, int)

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        director_d = {'name': 'Alf'}
        director = self.director_service.create(director_d)
        assert director.id is not None
        assert director.name == 'Stas'

    def test_delete(self):
        res = self.director_service.delete(1)
        assert res is None

    def test_update(self):
        director_d = {'id': 2, 'name': 'Flash'}
        self.director_service.update(director_d)





