from Domain.medicament_validator import MedicamentValidator
from Repository.file_repository import FileRepository
from Service.medicament_service import MedicamentService
from Tests.common import clear_file


def test_create_medicament():
    clear_file('test_medicament.txt')
    clear_file('test_tranzactii.txt')
    medicament_repository = FileRepository('test_medicament.txt')
    medicament_validator = MedicamentValidator()
    tranzactie_repository = FileRepository('test_tranzactii.txt')

    service = MedicamentService(medicament_repository, medicament_validator, tranzactie_repository)
    service.create('1', 'Nurofen', 'Catena', 10, 'da')
    assert len(service.get_all()) == 1

    added = medicament_repository.find_by_id('1')
    assert added is not None
    assert added.id_entitate == '1'
    assert added.nume == 'Nurofen'
    assert added.producator == 'Catena'
    assert added.pret == 10
    assert added.reteta == True

def test_update_medicament():
    clear_file('test_medicament.txt')
    clear_file('test_tranzactii.txt')
    medicament_repository = FileRepository('test_medicament.txt')
    medicament_validator = MedicamentValidator()
    tranzactie_repository = FileRepository('test_tranzactii.txt')

    service = MedicamentService(medicament_repository, medicament_validator, tranzactie_repository)
    service.create('1', 'Nurofen', 'Catena', 10, 'da')
    assert len(service.get_all()) == 1
    service.update('1', 'Nurofen', 'Catena', 12, 'da')

    updated = medicament_repository.find_by_id('1')
    assert updated is not None
    assert updated.id_entitate == '1'
    assert updated.nume == 'Nurofen'
    assert updated.producator == 'Catena'
    assert updated.pret == 12
    assert updated.reteta == True

def test_delete_medicament():
    clear_file('test_medicament.txt')
    clear_file('test_tranzactii.txt')
    medicament_repository = FileRepository ('test_medicament.txt')
    medicament_validator = MedicamentValidator ()
    tranzactie_repository = FileRepository ('test_tranzactii.txt')

    service = MedicamentService (medicament_repository, medicament_validator, tranzactie_repository)
    service.create('1', 'Nurofen', 'Catena', 10, 'da')
    service.create('2', 'Fasconal', 'Catena', 17, 'nu')
    service.delete('1')
    assert len(service.get_all()) == 1

