from copy import deepcopy
from datetime import date

from Domain.tranzactie import Tranzactie
from Repository.file_repository import FileRepository


class TranzactieService:
    def __init__(self,
                 tranzactii_repository: FileRepository,
                 medicamente_repository: FileRepository,
                 clienti_repository: FileRepository):
        self.__tranzactii_repository = tranzactii_repository
        self.__medicamente_repository = medicamente_repository
        self.__clienti_repository = clienti_repository

    def create(self, id_tranzactie, id_medicament, id_card_client, nr_bucati, data, ora, afisare_reducere = True):
        """
        Adauga o tranzactie in farmacie.
        :param id_tranzactie: id-ul tranzactiei
        :param id_medicament: id-ul medicamentului
        :param id_card_client: id-ul cardului clientului
        :param nr_bucati: numarul de bucati de medicamente
        :param data: data tranzactiei
        :param ora: ora tranzactiei
        :param afisare_reducere: parametrul decide daca se va afisa reducerea efectuata pe ecran
        :return: o tranzactie
        """
        medicament = self.__medicamente_repository.find_by_id(id_medicament)
        client = self.__clienti_repository.find_by_id(id_card_client)
        tranzactie = Tranzactie(id_tranzactie, medicament, client, nr_bucati, data, ora, medicament.pret * nr_bucati)

        med = deepcopy(medicament)
        if id_card_client != '0':
            if med.reteta:
                reducere = (15 * med.pret) / 100

                med.pret = float((med.pret - reducere) * tranzactie.nr_bucati)
                tranzactie.suma_platita = med.pret
                if afisare_reducere == True:
                    print(f'Pretul platit pentru medicament este {med.pret}, iar reducerea acordata este de 15%')
            else:
                reducere = (10 * med.pret) / 100

                med.pret = float((med.pret - reducere) * tranzactie.nr_bucati)
                tranzactie.suma_platita = med.pret
                if afisare_reducere == True:
                    print(f'Pretul platit pentru medicament este {med.pret}, iar reducerea acordata este de 10%')

        if self.__medicamente_repository.find_by_id(id_medicament) is None:
            raise KeyError(f'Nu exista niciun medicament cu id-ul {id_medicament}')
        if self.__clienti_repository.find_by_id(id_card_client) is None:
            raise KeyError(f'Nu exista niciun client cu id-ul {id_card_client}')

        self.__tranzactii_repository.create(tranzactie)
        self.__medicamente_repository.update(med)

    def delete(self, id_tranzactie):
        """
        Sterge o tranzactie din farmacie.
        :param id_tranzactie: id-ul tranzactiei de sters
        :return:
        """
        self.__tranzactii_repository.delete(id_tranzactie)

    def update(self, id_tranzactie, id_medicament, id_card_client, nr_bucati, data, ora):
        """
        Modifica o tranzactie din farmacie.
        :param id_tranzactie: id-ul tranzactiei
        :param id_medicament: id-ul medicamentului
        :param id_card_client: id-ul cardului clientului
        :param nr_bucati: numarul de bucati de medicamente
        :param data: data tranzactiei
        :param ora: ora tramzactiei
        :return:
        """
        medicament = self.__medicamente_repository.find_by_id(id_medicament)
        card_client = self.__clienti_repository.find_by_id(id_card_client)

        tranzactie = self.__tranzactii_repository.find_by_id(id_tranzactie)

        if tranzactie is None:
            raise KeyError(f'Tranzactia cu id-ul {id_tranzactie} nu exista!')

        if id_medicament == '':
            medicament = tranzactie.medicament
        if id_card_client == '':
            card_client = tranzactie.client
        if nr_bucati == '':
            nr_bucati = tranzactie.nr_bucati
        if data == '':
            data = tranzactie.date
        if ora == '':
            ora = tranzactie.time

        suma_platita = medicament.pret * nr_bucati
        updated_tranzactie = Tranzactie(id_tranzactie, medicament, card_client, nr_bucati, data, ora, suma_platita)

        self.__tranzactii_repository.update(updated_tranzactie)

    def get_all(self):
        """
        Afiseaza toate tranzactiile din farmacie.
        :return:
        """
        return self.__tranzactii_repository.get_all()

    def numarare_vanzari(self):
        """
        Sorteaza medicamentele descrescator dupa numarul de vanzari.
        :return:
        """
        medicament_list = self.__medicamente_repository.get_all()
        medicamente_vanzari = {}
        for each_medicament in medicament_list:
            medicamente_vanzari[each_medicament.id_entitate] = 0
        vanzari_list = self.__tranzactii_repository.get_all()
        for vanzare in vanzari_list:
            if vanzare.id_medicament in medicamente_vanzari:
                medicamente_vanzari[vanzare.id_medicament] += 1

        med_sort = {med_id: nr_vanzari for med_id, nr_vanzari in
                    sorted(medicamente_vanzari.items(), key=lambda element: element[1], reverse=True)}
        return med_sort

    def get_tranzactii_by_interval_de_zile(self, start_data, end_data):
        """
        Afiseaza toate tranzactiile dintr-un interval dat.
        :param start_data: prima data a intervalului
        :param end_data: ultima data a intervalului
        :return:
        """
        valid_tranzactii = []

        tranzactii_list = self.__tranzactii_repository.get_all()
        for each_tranzactie in tranzactii_list:
            if start_data <= each_tranzactie.date <= end_data:
                valid_tranzactii.append(each_tranzactie)

        return valid_tranzactii

    def delete_in_interval(self, start_day: date, stop_day: date):
        """
        Sterge toate tranzactiile dintr-un interval dat.
        :param start_day: prima data a intervalului
        :param stop_day: ultima data a intervalului
        :return:
        """
        tranzactie_list = self.__tranzactii_repository.get_all()
        deletions = 0
        for each_tranzactie in tranzactie_list:
            if start_day <= each_tranzactie.date <= stop_day:
                self.delete(str(each_tranzactie.id_entitate))
                deletions += 1
        return deletions

    def sort_dupa_reduceri_desc(self):
        """
        Ordoneaza descrescator cardurile de client dupa reducerile obtinute.
        :return:
        """

        client_list = self.__tranzactii_repository.get_all()
        client_list.sort(key=lambda x: x.reducere, reverse=True)
        return client_list

