from datetime import date, time
from Domain.client_validator import ClientValidator
from Domain.medicament_validator import MedicamentValidator
from Repository.client_html import ClientHTMLRepository
from Repository.file_repository import FileRepository
from Service.client_service import ClientService
from Service.medicament_service import MedicamentService
from Service.tranzactie_service import TranzactieService
from Tests.common import clear_file


def test_create_tranzactie():

    clear_file('test_medicament.txt')
    clear_file('test_client.txt')
    clear_file('test_tranzactii.txt')
    clear_file('test_client_html.txt')

    medicament_repository = FileRepository('test_medicament.txt')
    medicament_validator = MedicamentValidator()
    client_repository = FileRepository('test_client.txt')
    client_validator = ClientValidator()
    client_html = ClientHTMLRepository('test_client_html.txt')

    tranzactie_repository = FileRepository('test_tranzactii.txt')
    medicament_service = MedicamentService(medicament_repository, medicament_validator, tranzactie_repository)
    medicament_service.create('11', 'Nurofen', 'Catena', 10, 'da')
    assert len(medicament_service.get_all()) == 1

    client_service = ClientService(client_repository, client_validator, tranzactie_repository, client_html)
    client_service.create('11', 'Sima', 'Felix', '5010116010379', date(2020, 10, 10))
    assert len(client_service.get_all()) == 1

    tranzactie_service = TranzactieService(tranzactie_repository, medicament_repository, client_repository)
    tranzactie_service.create('11', '11', '11', 3, date(2020, 11, 11), time(12, 10), afisare_reducere=False)
    assert len(tranzactie_service.get_all()) == 1

    added = tranzactie_repository.find_by_id('11')
    assert added is not None
    assert added.id_entitate == '11'
    assert added.id_medicament == '11'
    assert added.id_card_client == '11'
    assert added.nr_bucati == 3
    assert added.date == date(2020, 11, 11)
    assert added.time == time(12, 10)

def test_update_tranzactie():

    clear_file('test_medicament.txt')
    clear_file('test_client.txt')
    clear_file('test_tranzactii.txt')
    clear_file('test_client_html.txt')

    medicament_repository = FileRepository('test_medicament.txt')
    medicament_validator = MedicamentValidator()
    client_repository = FileRepository('test_client.txt')
    client_validator = ClientValidator()
    client_html = ClientHTMLRepository('test_client_html.txt')
    tranzactie_repository = FileRepository('test_tranzactii.txt')
    medicament_service = MedicamentService(medicament_repository, medicament_validator, tranzactie_repository)
    medicament_service.create('11', 'Nurofen', 'Catena', 10, 'da')
    assert len(medicament_service.get_all()) == 1

    client_service = ClientService(client_repository, client_validator, tranzactie_repository, client_html)
    client_service.create('11', 'Sima', 'Felix', '5010116010379', date(2020, 10, 10))
    assert len(client_service.get_all()) == 1

    tranzactie_service = TranzactieService(tranzactie_repository, medicament_repository, client_repository)
    tranzactie_service.create('11', '11', '11', 3, date(2020, 11, 11), time(12, 10), afisare_reducere=False)
    tranzactie_service.update('11', '11', '11', 5, date (2020, 11, 11), time (10, 10))
    assert len(tranzactie_service.get_all()) == 1

    added = tranzactie_repository.find_by_id('11')
    assert added is not None
    assert added.id_entitate == '11'
    assert added.id_medicament == '11'
    assert added.id_card_client == '11'
    assert added.nr_bucati == 5
    assert added.date == date(2020, 11, 11)
    assert added.time == time(10, 10)


def test_delete_tranzactie():
        filename = 'test_tranzactii.txt'
        clear_file(filename)
        tranzactie_repository = FileRepository(filename)

        filename = 'test_medicament.txt'
        clear_file(filename)
        medicament_repository = FileRepository(filename)
        medicament_validator = MedicamentValidator()
        medicament_service = MedicamentService(medicament_repository, medicament_validator, tranzactie_repository)
        medicament_service.create('100', 'Parasinus', 'Nu stiu', 10, 'da')
        medicament_service.create('101', 'Paduden', 'Nu mai stiu', 15, 'da')

        filename = 'test_client.txt'
        clear_file(filename)
        clear_file('test_client_html.txt')
        client_repository = FileRepository(filename)
        client_validator = ClientValidator()
        client_html = ClientHTMLRepository('test_client_html.txt')
        client_service = ClientService (client_repository, client_validator, tranzactie_repository, client_html)
        client_service.create('100', 'Sima', 'Felix', '5010116010389', '2020-10-10')

        service = TranzactieService(tranzactie_repository, medicament_repository, client_repository)

        service.create('100', '100', '100', 3, date (2020, 9, 10), time (10, 10), afisare_reducere=False)
        service.create('101', '101', '100', 3, date (2020, 10, 8), time (10, 10), afisare_reducere=False)
        service.create('102', '100', '100', 3, date (2020, 10, 9), time (10, 10), afisare_reducere=False)
        service.create('103', '101', '100', 3, date (2020, 10, 10), time (10, 10), afisare_reducere=False)
        service.create('104', '100', '100', 3, date (2020, 11, 10), time (10, 10), afisare_reducere=False)
        service.delete('100')
        lista_tranzactii = service.get_all()
        assert len(lista_tranzactii) == 4



