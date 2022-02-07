from Tests.test_client_service import test_create_client, test_update_client, test_delete_client
from Tests.test_domain import test_medicament, test_client, test_tranzactie
from Tests.test_file_repository import test_file_repository
from Tests.test_functionalities import test_delete_tranzactii_din_interval, test_afisare_tranzactii_din_interval, \
    test_carduri_ordonate, test_full_search_medicamente, test_full_search_clienti, test_medicamente_ordonate, \
    test_apply_scumpire
from Tests.test_medicament_service import test_create_medicament, test_update_medicament, test_delete_medicament
from Tests.test_tranzactie_service import test_create_tranzactie, test_update_tranzactie, test_delete_tranzactie


def run_all_tests():
    #test domain:
    test_medicament()
    test_client()
    #test_tranzactie()
    #test_tranzactie()

    #test file_repository:
    test_file_repository()

    #test service medicament:
    test_create_medicament()
    test_update_medicament()
    test_delete_medicament()

    #test service client:
    test_create_client()
    test_update_client()
    test_delete_client()

    #test service tranzactie:
    test_create_tranzactie()
    test_delete_tranzactie()
    test_update_tranzactie()

    #test functionalities:
    test_afisare_tranzactii_din_interval()
    test_delete_tranzactii_din_interval()
    test_carduri_ordonate()
    test_full_search_medicamente()
    test_full_search_clienti()
    #test_medicamente_ordonate()
    test_apply_scumpire()

