
from Domain.client import Client



class ClientValidator:

    def validate(self, client: Client):

        errors = []

        if len(client.cnp) != 13 :
            errors.append('CNP-ul trebuie sa contina 13 cifre!')

        if errors != []:
            raise ValueError(errors)