from datetime import date

from Domain.client import Client
from Domain.medicament import Medicament
from Repository.file_repository import FileRepository
from Tests.common import clear_file


def test_file_repository():
    filename = 'test_medicament.txt'
    clear_file(filename)
    medicament_repository = FileRepository(filename)
    assert medicament_repository.get_all() == []

    m = Medicament('2', 'Brufen', 'Catena', 15, 'Da')
    medicament_repository.create(m)

    assert medicament_repository.get_all() == [m]

    filename = 'test_client.txt'
    clear_file(filename)
    client_repository = FileRepository(filename)
    assert client_repository.get_all() == []

    c = Client('2', 'Banea', 'Carmen', '6010116010379', date(2020, 10, 10))
    client_repository.create(c)

    assert client_repository.get_all() == [c]
