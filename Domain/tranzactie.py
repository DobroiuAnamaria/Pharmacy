from Domain.client import Client
from Domain.entitate import Entitate
from Domain.medicament import Medicament
from ViewModel.tranzactie_viewmodel import TranzactieViewModel
from datetime import datetime


class Tranzactie(Entitate):
    """

    """

    def __init__(self, id_tranzactie, medicament: Medicament, client: Client, nr_bucati, data, ora, suma_platita):
        """

        """
        super(Tranzactie, self).__init__(id_tranzactie)
        self.__medicament = medicament
        self.__client = client
        self.__nr_bucati = nr_bucati
        self.__datetime = datetime.combine(data, ora)
        self.__suma_platita = suma_platita

    @property
    def medicament(self):
        return self.__medicament

    @property
    def client(self):
        return self.__client

    @property
    def id_medicament(self):
        return self.__medicament.id_entitate

    @property
    def id_card_client(self):
        return self.__client.id_entitate

    @property
    def nr_bucati(self):
        return self.__nr_bucati

    @nr_bucati.setter
    def nr_bucati(self, value):
        self.__nr_bucati = value

    @property
    def date(self):
        return self.__datetime.date()

    @date.setter
    def date(self, value: date):
        self.__datetime = datetime.combine(value, self.__datetime.time())

    @property
    def time(self):
        return self.__datetime.time()

    @time.setter
    def time(self, value: time):
        self.__datetime = datetime.combine(self.__datetime.date(), value)

    @property
    def datetime(self):
        return self.__datetime

    @datetime.setter
    def datetime(self, value: datetime):
        self.__datetime = value

    @property
    def reducere(self):
        return self.__medicament.pret*self.nr_bucati-self.__suma_platita

    @property
    def suma_platita(self):
        return self.__suma_platita

    @suma_platita.setter
    def suma_platita(self, value):
        self.__suma_platita = value

    def __str__(self):
        return str(TranzactieViewModel(self.id_entitate, self.medicament, self.client, self.nr_bucati, self.date, self.time))
