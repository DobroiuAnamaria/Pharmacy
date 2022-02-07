from datetime import date, time
from Domain.tranzactie import Tranzactie


class TranzactieValidator:

    def validate(self, tranzactie: Tranzactie):
        errors = []
        if tranzactie.nr_bucati <=  0:
            errors.append('Numarul de bucati trebuie sa fie mai mare decat 0!')

        if type(tranzactie.date) is not date:
            errors.append('Data tranzactiei are un format invalid')

        if type(tranzactie.time) is not time:
            errors.append('Ora tranzactiei are un format invalid')

        if errors != []:
            raise ValueError(errors)

