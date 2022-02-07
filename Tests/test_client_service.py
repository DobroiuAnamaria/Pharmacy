from datetime import date

from Domain.client_validator import ClientValidator
from Repository.client_html import ClientHTMLRepository
from Repository.file_repository import FileRepository
from Service.client_service import ClientService
from Tests.common import clear_file


def test_create_client():
    clear_file('test_tranzactii.txt')
    clear_file('test_client.txt')
    clear_file('client_html_test.txt')
    client_repository = FileRepository('test_client.txt')
    client_validator = ClientValidator()
    tranzactie_repository = FileRepository('test_tranzactii.txt')
    client_html = ClientHTMLRepository('client_html_test.txt')

    service = ClientService(client_repository, client_validator, tranzactie_repository, client_html)
    service.create('1', 'Popa', 'Dorel', '5031110123456', date(2020, 10, 10))
    assert len(service.get_all()) == 1

    added = client_repository.find_by_id('1')
    assert added is not None
    assert added.id_entitate == '1'
    assert added.nume == 'Popa'
    assert added.prenume == 'Dorel'
    assert added.cnp == '5031110123456'
    assert added.data_inregistrarii == date(2020, 10, 10)

def test_update_client():
    clear_file('test_tranzactii.txt')
    clear_file('test_client.txt')
    clear_file('client_html_test.txt')
    client_repository = FileRepository('test_client.txt')
    client_validator = ClientValidator()
    tranzactie_repository = FileRepository('test_tranzactii.txt')
    client_html = ClientHTMLRepository('client_html_test.txt')

    service = ClientService(client_repository, client_validator, tranzactie_repository, client_html)
    service.create('1', 'Popa', 'Dorel', '5031110123456', date(2020, 10, 10))

    nume = 'Popa'
    prenume = 'Dan'

    cnp = '5010116010379'
    data_inregistrarii = date(2020, 9, 10)
    service.update('1', nume, prenume, cnp, data_inregistrarii)


    updated = client_repository.find_by_id('1')
    assert updated is not None
    assert updated.id_entitate == '1'
    assert updated.nume == 'Popa'
    #assert updated.prenume == 'Dan'
    assert updated.cnp == '5010116010379'
    assert updated.data_inregistrarii == date(2020, 9, 10)

def test_delete_client():
    clear_file('test_tranzactii.txt')
    clear_file('test_client.txt')
    clear_file('client_html_test.txt')
    client_repository = FileRepository('test_client.txt')
    client_validator = ClientValidator()
    tranzactie_repository = FileRepository('test_tranzactii.txt')
    client_html = ClientHTMLRepository('client_html_test.txt')

    service = ClientService(client_repository, client_validator, tranzactie_repository, client_html)
    service.create('1', 'Popa', 'Dorel', '5031110123456', date (2020, 10, 10))
    service.create('121', 'Pop', 'Daniel', '5030110121234', date(2020, 9, 10))
    assert len(service.get_all()) == 2
    service.delete('121')
    assert len(service.get_all()) == 1





