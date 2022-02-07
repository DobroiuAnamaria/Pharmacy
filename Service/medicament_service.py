import xlsxwriter

from Domain.medicament import Medicament
from Domain.medicament_validator import MedicamentValidator
from Domain.random import RandomMed
from Repository.file_repository import FileRepository


class MedicamentService:

    def __init__(self, medicamente_repository: FileRepository, medicament_validator: MedicamentValidator,
                 tranzactie_repository: FileRepository):
        self.__medicamente_repository = medicamente_repository
        self.__tranzactie_repository = tranzactie_repository
        self.__medicament_validator = medicament_validator

    def create(self, id_medicament, nume, producator, pret, reteta):
        """
        Adauga un medicament.

        :param id_medicament: id-ul medicamentului
        :param nume: numele medicamentului
        :param producator: producatorul medicamentului
        :param pret: pretul medicamentului
        :param reteta: True, daca necesita  reteta si False altfel
        :raises ValueError: daca ...
        :raises KeyError: daca id-ul exista deja
        :return: -
        """
        medicament = Medicament(id_medicament, nume, producator, pret, reteta)
        self.__medicament_validator.validate(medicament)

        if reteta == 'da':
            medicament.reteta = True
        else:
            medicament.reteta = False

        self.__medicamente_repository.create(medicament)

    def delete(self, id_med):
        """
        Sterge un medicament dupa un id dat.
        :param id_med: id-ul medicamentului de sters
        :return:
        """
        medicament = self.__medicamente_repository.find_by_id(id_med)
        if self.numar_tranzactii(medicament) != 0:
            raise KeyError(f'Exista tranzactii pentru medicamentul cu id {id_med}! Acesta nu poate fi sters!')
        self.__medicamente_repository.delete(id_med)

    def numar_tranzactii(self, medicament):
        """
        Calculeaza nr de vanzari ale medicamentelor din tranzactii.
        :param medicament: medicamentul din tranzactie
        :return:
        """
        tranzactii = self.__tranzactie_repository.get_all()
        numar = 0
        for tranzactie in tranzactii:
            if tranzactie.id_medicament == medicament.id_entitate:
                numar = numar + 1
        return numar

    def update(self, id_medicament, nume, producator, pret, reteta):
        medicament = self.__medicamente_repository.find_by_id(id_medicament)
        if medicament is None:
            raise KeyError(f'Medicamentul cu id-ul {id_medicament} nu exista!')

        if nume != '':
            medicament.nume = nume
        if producator != '':
            medicament.producator = producator
        if pret != '':
            medicament.pret = pret
        else:
            medicament.pret = float(medicament.pret)
        if reteta != '':
            medicament.reteta = reteta

        self.__medicament_validator.validate(medicament)

        if reteta == 'da' or reteta == '':
            medicament.reteta = True
        else:
            medicament.reteta = False

        self.__medicamente_repository.update(medicament)

    def read_by_id(self, id_dat):
        """
        Gaseste un medicament dupa id-ul dat.
        :param id_dat: id-ul medicamentului de gasit
        :return:
        """
        return self.__medicamente_repository.find_by_id(id_dat)

    def generate_medicamente(self, number_of_medicamente):
        """
        Genereaza un numar de medicamente cu date aleatorii valide
        :param number_of_medicamente: numarul de medicamente de generat, int
        :return: None
        """

        generated_list = []
        for i in range(number_of_medicamente):
            rand_id = RandomMed.random_int()
            rand_nume = RandomMed.random_string()
            rand_producator = RandomMed.random_int(1888, 2025)
            rand_pret = RandomMed.random_int(1, 200)
            rand_reteta = RandomMed.random_bool()
            generated_medicamente = Medicament(rand_id, rand_nume, rand_producator, rand_pret, rand_reteta)
            self.__medicament_validator.validate(generated_medicamente)
            self.__medicamente_repository.create(generated_medicamente)
            generated_list.append(generated_medicamente)
        return generated_list

    def get_all(self):
        """
        Afiseaza toate medicamentele din farmacie.
        :return:
        """
        return self.__medicamente_repository.get_all()

    def full_search(self, string_to_search):
        """
        Cauta medicamente dupa nume, producator etc.
        Cautare full text.
        :param string_to_search: string-ul de cautat
        :return:
        """

        search_results = []
        medicamente_list = self.__medicamente_repository.get_all()
        for each_medicament in medicamente_list:
            if each_medicament.search(string_to_search):
                search_results.append(each_medicament)
        return search_results

    def apply_scumpire_med(self, read_pret, pret_increase):
        """
        Aplica o scumpire data medicamentelor cu pretul mai mic decat o valoare data.
        :param read_pret: pretul dat dupa care se compara
        :param pret_increase: procentul cu care se scumpeste
        :return:
        """

        errors = ''
        if pret_increase < 0:
            errors += '\nScumpirea nu poate sa reduca pretul medicamentului.'
        if pret_increase == 0:
            errors += '\nScumpirea nu poate fi zero.'
        if len(errors):
            raise ValueError(errors)

        preturi = 0
        medicamente_list = self.__medicamente_repository.get_all()
        for medicament in medicamente_list:
            if medicament.pret <= read_pret:
                preturi += 1
                medicament.pret = medicament.pret + pret_increase
                self.__medicamente_repository.update(medicament)
        return preturi

    def excel_tabel(self):

        workbook = xlsxwriter.Workbook('medicament.xlsx')
        worksheet = workbook.add_worksheet()
        row = 0
        col = 0
        worksheet.write(row, col, "id_medicament")
        worksheet.write(row, col + 1, "producator")
        worksheet.write(row, col + 2, "nume")
        worksheet.write(row, col + 3, "pret")
        worksheet.write(row, col + 4, "reteta")
        row += 1
        col = 0
        for medicament in self.__medicamente_repository.get_all():
            worksheet.write(row, col, medicament.id_entitate)
            worksheet.write(row, col + 1, medicament.producator)
            worksheet.write(row, col + 2, medicament.nume)
            worksheet.write(row, col + 3, medicament.pret)
            worksheet.write(row, col + 4, medicament.reteta)
            row += 1
            col = 0

        workbook.close()
