from Domain.client_validator import ClientValidator
from Domain.medicament_validator import MedicamentValidator
from Repository.client_html import ClientHTMLRepository
from Repository.file_repository import FileRepository
from Service.client_service import ClientService
from Service.medicament_service import MedicamentService
from Service.tranzactie_service import TranzactieService
from Tests.run_all_tests import run_all_tests
from UserInterface.console import Console


def main():

    medicament_repository = FileRepository('medicamente.txt')
    medicament_validator = MedicamentValidator()

    client_repository = FileRepository('clienti.txt')
    client_validator = ClientValidator()

    tranzactie_repository = FileRepository('tranzactii.txt')
    clienti_html = ClientHTMLRepository("clienti.html")

    medicament_service = MedicamentService(medicament_repository, medicament_validator, tranzactie_repository)
    client_service = ClientService(client_repository, client_validator, tranzactie_repository, clienti_html)
    tranzactie_service = TranzactieService(tranzactie_repository, medicament_repository, client_repository)

    user_interface = Console(medicament_service, client_service, tranzactie_service)
    user_interface.run_console()


run_all_tests()
main()
