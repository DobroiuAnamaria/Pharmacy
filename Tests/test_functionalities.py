from Domain.client_validator import ClientValidator
from Domain.medicament_validator import MedicamentValidator

from Repository.client_html import ClientHTMLRepository
from Repository.file_repository import FileRepository
from Service.client_service import ClientService
from Service.medicament_service import MedicamentService
from Service.tranzactie_service import TranzactieService
from Tests.common import clear_file
from datetime import date, time


def test_delete_tranzactii_din_interval():
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
    clear_file('client_html_test.txt')
    client_repository = FileRepository(filename)
    client_validator = ClientValidator()
    client_html = ClientHTMLRepository('client_html_test.txt')
    client_service = ClientService(client_repository, client_validator, tranzactie_repository, client_html)
    client_service.create('100', 'Sima', 'Felix', '5010116010389', '2020-10-10')

    service = TranzactieService(tranzactie_repository, medicament_repository, client_repository)

    service.create('100', '100', '100', 3, date(2020, 9, 10), time(10, 10), afisare_reducere=False)
    service.create('101', '101', '100', 3, date(2020, 10, 8), time(10, 10), afisare_reducere=False)
    service.create('102', '100', '100', 3, date(2020, 10, 9), time(10, 10), afisare_reducere=False)
    service.create('103', '101', '100', 3, date(2020, 10, 10), time(10, 10), afisare_reducere=False)
    service.create('104', '100', '100', 3, date(2020, 11, 10), time(10, 10), afisare_reducere=False)
    service.delete_in_interval(date(2020, 10, 7), date(2020, 10, 11))
    lista_tranzactii = service.get_all()
    assert len(lista_tranzactii) == 2
    assert lista_tranzactii[0].id_entitate == '100'
    assert lista_tranzactii[1].id_entitate == '104'

def test_afisare_tranzactii_din_interval():
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
    clear_file('client_html_test.txt')
    client_repository = FileRepository(filename)
    client_validator = ClientValidator()
    client_html = ClientHTMLRepository('client_html_test.txt')
    client_service = ClientService(client_repository, client_validator, tranzactie_repository, client_html)
    client_service.create('100', 'Sima', 'Felix', '5010116010389', '2020-10-10')

    service = TranzactieService(tranzactie_repository, medicament_repository, client_repository)

    service.create('100', '100', '100', 3, date(2020, 9, 10), time(10, 10), afisare_reducere=False)
    service.create('101', '101', '100', 3, date(2020, 10, 8), time(10, 10), afisare_reducere=False)
    service.create('102', '100', '100', 3, date(2020, 10, 9), time(10, 10), afisare_reducere=False)
    service.create('103', '101', '100', 3, date(2020, 10, 10), time(10, 10), afisare_reducere=False)
    service.create('104', '100', '100', 3, date(2020, 11, 10), time(10, 10), afisare_reducere=False)
    service.get_tranzactii_by_interval_de_zile(date(2020, 10, 7), date(2020, 10, 11))
    lista_tranzactii = service.get_tranzactii_by_interval_de_zile(date(2020, 10, 7), date(2020, 10, 11))
    assert len(lista_tranzactii) == 3

def test_carduri_ordonate():
    clear_file('client_test.txt')
    clear_file('test_tranzactii.txt')
    clear_file('test_client_html.txt')
    clear_file('test_medicament.txt')
    medicament_repository = FileRepository('test_medicament.txt')
    medicament_validator = MedicamentValidator()
    tranzactie_repository = FileRepository('test_tranzactii.txt')
    medicament_service = MedicamentService(medicament_repository, medicament_validator, tranzactie_repository)
    medicament_service.create('100', 'Parasinus', 'Nu stiu', 10, 'da')
    medicament_service.create('101', 'Paduden', 'Nu mai stiu', 15, 'nu')

    client_repository = FileRepository('client_test.txt')

    client_html = ClientHTMLRepository('test_client_html.txt')
    client_validator = ClientValidator()
    client_service = ClientService(client_repository, client_validator, tranzactie_repository, client_html)
    tranzactie_service = TranzactieService(tranzactie_repository, medicament_repository, client_repository)

    client_service.create('15', 'Dona', 'Alba', '6010113410234', date(2020, 9, 11))
    client_service.create('16', 'Sheperd', 'Derek', '5010113410234', date(2020, 10, 10))
    client_service.create('17', 'Grey', 'Meredith', '6040113410257', date(2020, 8, 14))

    tranzactie_service.create('100', '100', '15', 3, date(2020, 9, 10), time(10, 10), afisare_reducere=False)
    tranzactie_service.create('101', '101', '16', 10, date(2020, 10, 8), time(10, 10), afisare_reducere=False)
    tranzactie_service.create('102', '100', '17', 1, date(2020, 10, 9), time(10, 10), afisare_reducere=False)

    lista_ordonata = tranzactie_service.sort_dupa_reduceri_desc()
    assert lista_ordonata[0].id_entitate == '101'
    assert lista_ordonata[1].id_entitate == '100'
    assert lista_ordonata[2].id_entitate == '102'


def test_full_search_medicamente():
    clear_file('test_medicament.txt')
    clear_file('test_tranzactii.txt')
    medicament_repository = FileRepository('test_medicament.txt')
    medicament_validator = MedicamentValidator()
    tranzactie_repository = FileRepository('test_tranzactii.txt')
    medicament_service = MedicamentService(medicament_repository, medicament_validator, tranzactie_repository)
    medicament_service.create('100', 'Parasinus', 'Nu stiu', 10, 'da')
    medicament_service.create('101', 'Paduden', 'Nu mai stiu', 15, 'nu')
    assert len(medicament_service.full_search('Nu')) == 2

def test_full_search_clienti():
    clear_file('test_client.txt')
    clear_file('test_tranzactii.txt')
    clear_file('test_client_html.txt')
    client_repository = FileRepository('test_client.txt')
    client_validator = ClientValidator()
    client_html = ClientHTMLRepository('test_client_html.txt')
    tranzactie_repository = FileRepository('test_tranzactii.txt')
    client_service = ClientService(client_repository, client_validator, tranzactie_repository, client_html)
    client_service.create('15', 'Dona', 'Alba', '6010113410234', date(2020, 9, 11))
    client_service.create('16', 'Sheperd', 'Derek', '5010113410234', date(2020, 10, 10))
    client_service.create('17', 'Grey', 'Meredith', '6040113410257', date(2020, 8, 14))
    assert len(client_service.full_search('Derek')) == 1


def test_medicamente_ordonate():
    clear_file('client_test.txt')
    clear_file('test_tranzactii.txt')
    clear_file('test_client_html.txt')
    clear_file('test_medicament.txt')
    medicament_repository = FileRepository('test_medicament.txt')
    medicament_validator = MedicamentValidator()
    tranzactie_repository = FileRepository('test_tranzactii.txt')
    medicament_service = MedicamentService(medicament_repository, medicament_validator, tranzactie_repository)
    medicament_service.create('100', 'Parasinus', 'Nu stiu', 10, 'da')
    medicament_service.create('101', 'Paduden', 'Nu mai stiu', 15, 'nu')

    client_repository = FileRepository('client_test.txt')

    client_html = ClientHTMLRepository('test_client_html.txt')
    client_validator = ClientValidator()
    client_service = ClientService(client_repository, client_validator, tranzactie_repository, client_html)
    tranzactie_service = TranzactieService(tranzactie_repository, medicament_repository, client_repository)

    client_service.create('15', 'Dona', 'Alba', '6010113410234', date(2020, 9, 11))
    client_service.create('16', 'Sheperd', 'Derek', '5010113410234', date(2020, 10, 10))
    client_service.create('17', 'Grey', 'Meredith', '6040113410257', date(2020, 8, 14))

    tranzactie_service.create('100', '100', '15', 3, date(2020, 9, 10), time(10, 10), afisare_reducere=False)
    tranzactie_service.create('101', '101', '16', 10, date(2020, 10, 8), time(10, 10), afisare_reducere=False)
    tranzactie_service.create('102', '100', '17', 1, date(2020, 10, 9), time(10, 10), afisare_reducere=False)

    lista_ordonata = tranzactie_service.numarare_vanzari()
    assert lista_ordonata[0].id_medicament == '2'
    assert lista_ordonata[1].id_medicament == '1'



def test_apply_scumpire():
    clear_file('test_tranzactii.txt')
    clear_file('test_medicament.txt')
    medicament_repository = FileRepository('test_medicament.txt')
    medicament_validator = MedicamentValidator()
    tranzactie_repository = FileRepository('test_tranzactii.txt')
    medicament_service = MedicamentService(medicament_repository, medicament_validator, tranzactie_repository)
    medicament_service.create('100', 'Parasinus', 'Nu stiu', 30, 'da')
    medicament_service.create('101', 'Paduden', 'Nu mai stiu', 15, 'nu')
    medicament_service.create('102', 'Augumentin', 'Tot nu stiu', 45, 'da')
    medicament_service.create('103', 'Faringosept', 'Nici asta', 10, 'da')

    read_pret = 15
    pret_increase = 10
    medicament_service.apply_scumpire_med(read_pret, pret_increase)
    medicament_service.update('103', 'Faringosept', 'Nici asta', 11, 'da')

    updated = medicament_repository.find_by_id('103')
    assert updated is not None
    assert updated.id_entitate == '103'
    assert updated.nume == 'Faringosept'
    assert updated.producator == 'Nici asta'
    assert updated.pret == 11
    assert updated.reteta == True



