from datetime import date, time

from Domain.client import Client
from Domain.medicament import Medicament
from Domain.tranzactie import Tranzactie


def test_medicament():

    m = Medicament('1', 'Algocalmin', 'Habar nu am', 10, 'Da')
    assert m.id_entitate == '1'
    assert m.nume == 'Algocalmin'
    assert m.producator == 'Habar nu am'
    assert m.pret == 10
    assert m.reteta == 'Da'


def test_client():

    c = Client('1', 'Popa', 'Dorel', '5010116010379', date(2020, 10, 10))
    assert c.id_entitate == '1'
    assert c.nume == 'Popa'
    assert c.prenume == 'Dorel'
    assert c.cnp == '5010116010379'
    assert c.data_inregistrarii == date(2020, 10, 10)

def test_tranzactie():
    t = Tranzactie('11', '11', '11', 3, date(2020, 11, 11), time(12, 10))
    assert t.id_entitate == '11'
    assert t.id_medicament == '11'
    assert t.id_card_client == '11'
    assert t.nr_bucati == 3
    assert t.date == date(2020, 11, 11)
    assert t.time == time(12, 10)
