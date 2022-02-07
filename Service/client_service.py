from datetime import date

from Domain.client import Client
from Domain.client_validator import ClientValidator
from Domain.cnp_exceptions import CnpException
from Repository.client_html import ClientHTMLRepository
from Repository.file_repository import FileRepository


class ClientService:
    def __init__(self, clienti_repository: FileRepository, client_validator: ClientValidator,
                 tranzactie_repository: FileRepository,  client_html: ClientHTMLRepository):
        self.__clienti_repository = clienti_repository
        self.__tranzactie_repository = tranzactie_repository
        self.__client_validator = client_validator
        self.__client_html_repository = client_html

    def create(self, id_card_client, nume, prenume, cnp, data_inregistrarii):
        """
        Adauga un client.

        :param id_card_client: id-ul cardului clientului
        :param nume: numele clientului
        :param prenume: prenumele clientului
        :param cnp: cnp-ul clientului
        :param data_inregistrarii: data inregistrarii cardului clientului
        :raises ValueError: daca ...
        :raises KeyError: daca id-ul exista deja
        :return: -
        """
        client = Client(id_card_client, nume, prenume, cnp, data_inregistrarii)

        if self.get_by_cnp(client.cnp) is not None:
            raise CnpException(f'Clientul cu cnp-ul {client.cnp} exista deja!')

        self.__client_validator.validate(client)

        self.__clienti_repository.create(client)

    def delete(self, id_client):
        """
        Sterge un client din farmacie dupa un id dat
        :param id_client: id-ul clientului de sters
        :return:
        """
        card = self.__clienti_repository.find_by_id(id_client)
        if self.numar_tranzactii(card) != 0:
            raise KeyError(f'Exista tranzactii pentru cardul cu id {id_client}! Acesta nu poate fi sters!')
        self.__clienti_repository.delete(id_client)

    def numar_tranzactii(self, client):
        """
        Calculeaza numarul de clienti din tranzactii.
        :param client: clientul cu caracteristicile.
        :return:
        """
        tranzactii = self.__tranzactie_repository.get_all()
        numar = 0
        for tranzactie in tranzactii:
            if tranzactie.id_card_client == client.id_entitate:
                numar = numar + 1
        return numar

    def update(self, id_card_client, nume, prenume, cnp, data_inregistrarii):
        """
        Modificica caracteristicile unui client din farmacie.
        :param id_card_client: id-ul cardului clientului
        :param nume: numele clientului
        :param prenume: prenumele clientului
        :param cnp: cnp-ul clientului
        :param data_inregistrarii: data inregistrarii cardului clientului
        :return:
        """
        client = self.__clienti_repository.find_by_id(id_card_client)
        if client is None:
            raise KeyError(f'Clientul cu id-ul {id_card_client} nu exista!')

        if nume != '':
            client.nume = nume
        if prenume != '':
            client.prenume = prenume
        if cnp != '':
            client.cnp = cnp
        if data_inregistrarii != '':
            client.data_inregistrarii = data_inregistrarii
        else:
            read_date = data_inregistrarii.split('-')
            client.data_inregistrarii = date(int(read_date[2]), int(read_date[1]), int(read_date[0]))

        self.__client_validator.validate(client)

        self.__clienti_repository.update(client)

    def get_by_cnp(self, cnp):
        """
        Gaseste un client cu cnp-ul dat.
        :param cnp: cnp-ul clientului de gasit
        :return:
        """
        clienti = self.get_all()
        for client in clienti:
            if cnp == client.cnp:
                return client
        return None

    def get_all(self):
        """
        Afiseaza toti clientii din farmacie.
        :return:
        """
        return self.__clienti_repository.get_all()

    def full_search(self, string_to_search):
        """
        Cauta medicamente dupa nume, prenume, cnp etc.
        Cautare full text.
        :param string_to_search: string-ul de cautat
        :return:
        """

        search_results = []
        clienti_list = self.__clienti_repository.get_all()
        for each_client in clienti_list:
            if each_client.search(string_to_search):
                search_results.append(each_client)
        return search_results


    def export_clienti(self):
        self.__client_html_repository.export_clients(self.__clienti_repository.get_all())
