from copy import deepcopy

from Domain.entitate import Entitate


class EntitateRepository(Entitate):

    def __init__(self):
        '''
        TODO
        '''
        self.__storage = {}

    def find_by_id(self, id_entitate ):
        '''
        TODO
        :param id_entitate :
        :return:
        '''
        if id_entitate  in self.__storage:
            return self.__storage[id_entitate ]
        return None



    def create(self, entitate: Entitate ): # adaugare
        '''
        TODO
        :param entitate :
        :return:
        '''
        if self.find_by_id(entitate.id_entitate ) is not None:
            raise KeyError(f'Entitatea cu id-ul {entitate.id_entitate} exista deja!')

        self.__storage[entitate.id_entitate] = entitate

    def update(self, entitate: Entitate):
        '''
        TODO
        :param entitate:
        :return:
        '''
        if self.find_by_id(entitate.id_entitate) is None:
            raise KeyError(f'Nu exista o entitate cu id-ul {entitate.id_entitate} pe care sa o actualizam!')

        self.__storage[entitate.id_entitate] = entitate

    def delete(self, id_entitate):
        '''
        TODO
        :param id_entitate:
        :return:
        '''
        if self.find_by_id(id_entitate) is None:
            raise KeyError(f'Nu exista o entitate cu id-ul {id_entitate} pe care sa o stergem!')

        del self.__storage[id_entitate]

    def get_all(self):
        '''
        TODO
        :return:
        '''
        return deepcopy(list(self.__storage.values()))
