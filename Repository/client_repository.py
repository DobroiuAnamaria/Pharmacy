
from Repository.file_repository import FileRepository
from Domain.client import Client



class ClientRepository(FileRepository):

    def __init__(self, filename):
        super(ClientRepository, self).__init__(filename)



    def get_lista_de_CNP(self):
        CNPs = []
        for client in self.get_all():
            CNPs.append(client.cnp)
        return CNPs

    def create(self, other: Client):
        '''if self.find_by_id(other.id_entitate) is not None:
            raise KeyError(f'Exista deja o entitate cu id-ul {other.id_entitate}!')
        if self.__valid_CNP(other) is False:
            raise KeyError(f'Exista deja un card cu CNP-ul {other.CNP}')
        self.storage[other.id] = other
        new_CNP = CNP(other)
        self.__CNP_repository.create(new_CNP)
        self.write_file()'''
        if other.cnp in self.get_lista_de_CNP():
            raise KeyError("CNP-ul exista deja")
        super(ClientRepository, self).create(other)


    def update(self, other: Client):
        super(ClientRepository, self).update(other)


    def delete(self, id_card_client):
        '''del_card = self.find_by_id(id_card_client)
        if del_card is not None:
            CNP_for_delete = CNP(del_card)
            self.__CNP_repository.delete(CNP_for_delete.id)'''
        super(ClientRepository, self).delete(id_card_client)