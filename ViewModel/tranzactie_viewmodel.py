
from datetime import date, time

from Domain.client import Client
from Domain.medicament import Medicament


class TranzactieViewModel:

    def __init__(self, id_tranzactie, medicament: Medicament, client: Client, nr_bucati, data: date, ora: time):
        self.id_tranzactie = id_tranzactie
        self.medicament = medicament
        self.client = client
        self.nr_bucati = nr_bucati
        self.data = data
        self.ora = ora

    def __str__(self):
        return f'Tranzactia cu id-ul {self.id_tranzactie}, medicamentul: {self.medicament}, ' \
               f'clientul: {self.client}, nr_bucati: {self.nr_bucati}, data: {self.data.strftime("%A %#d %b %Y")} ' \
               f'ora: {self.ora.strftime("%H:%M")}'