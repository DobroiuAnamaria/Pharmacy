from Domain.entitate import Entitate
import jsonpickle

from Domain.id_exceptions import IdException


class FileRepository:

    def __init__(self, filename):
        """
        Creeaza un fisier.
        :param filename: fisierul
        """
        self.__storage = {}
        self.__filename = filename

    def __read_file(self):
        try:
            with open(self.__filename, 'r') as f:
                self.__storage = jsonpickle.decode(f.read())

        except:
            self.__storage = {}

    def __write_file(self):
        with open(self.__filename, 'w') as f:
            f.write(jsonpickle.encode(self.__storage))

    def find_by_id(self, id_entitate):
        """
        Gaseste o entitate dupa un id dat.
        :param id_entitate: id-ul entitatii
        :return:
        """
        self.__read_file()
        if str(id_entitate) in self.__storage:
            return self.__storage[str(id_entitate)]
        return None


    def create(self, entitate: Entitate):  # adaugare
        """
        Adauga o entitate.
        :param entitate: entitatea
        :return:
        """
        if self.find_by_id(entitate.id_entitate) is not None:
            raise IdException(f'Entitatea cu id-ul {entitate.id_entitate} exista deja!')
        # if self.find_by_cnp(entitate.cnp) is not None:
        #   raise KeyError(f'Entitatea cnp-ul {entitate.cnp} exista deja!')

        self.__storage[entitate.id_entitate] = entitate
        self.__write_file()

    def update(self, entitate: Entitate):
        """
       Modifica caracteristicile unei entitati.
        :param entitate: entitatea
        :return:
        """
        if self.find_by_id(entitate.id_entitate) is None:
            raise KeyError(f'Nu exista o entitate cu id-ul {entitate.id_entitate} pe care sa o actualizam!')

        self.__storage[entitate.id_entitate] = entitate
        self.__write_file()

    def delete(self, id_entitate):
        """
        Sterge o entitate dupa un id dat
        :param id_entitate: id-ul dat
        :return:
        """
        if self.find_by_id(id_entitate) is None:
            raise KeyError(f'Nu exista o entitate cu id-ul {id_entitate} pe care sa o stergem!')

        del self.__storage[id_entitate]
        self.__write_file()

    def get_all(self):
        """
        Afiseaza toate entitatile.
        :return:
        """
        self.__read_file()
        return list(self.__storage.values())
