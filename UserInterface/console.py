from datetime import date, time

from Service.medicament_service import MedicamentService
from Service.client_service import ClientService
from Service.tranzactie_service import TranzactieService


class Console:

    def __init__(self,
                 medicament_service: MedicamentService,
                 client_service: ClientService,
                 tranzactie_service: TranzactieService):
        self.__medicament_service = medicament_service
        self.__client_service = client_service
        self.__tranzactie_service = tranzactie_service

    def print_menu(self):
        """
        Permite utilizatorului sa vada optiunile gestionarii farmaciei online.
        :return:
        """
        print('\n--------------------------------------------------------------------')
        print('1-->CRUD Medicamente')
        print('2-->CRUD Card client')
        print('3-->CRUD Tranzactie')
        print('4-->Operatiuni')
        print('x-->Iesire')
        print('--------------------------------------------------------------------\n')

    def run_console(self):

        while True:
            self.print_menu()
            option = input('Alegeti optiunea: ')
            if option == '1':
                self.run_crud_medicamente()
            elif option == '2':
                self.run_crud_clienti()
            elif option == '3':
                self.run_crud_tranzactii()
            elif option == '4':
                self.run_operatiuni()
            elif option == 'x':
                break
            else:
                print('Comanda invalida!')

    def run_crud_medicamente(self):
        while True:
            print('\n--------------------------------------------------------------------')
            print('1-->Create medicament.')
            print('2-->Delete medicament.')
            print('3-->Update medicament.')
            print('a-->Show all medicamente.')
            print('b. Back')
            print('--------------------------------------------------------------------\n')
            option = input('Alegeti optiunea: ')
            if option == '1':
                self.handle_create_medicament()
            elif option == '2':
                self.handle_delete_medicament()
            elif option == '3':
                self.handle_update_medicament()
            elif option == 'a':
                self.handle_show_all_medicament()
            elif option == 'b':
                break
            else:
                print('Optiune invalida.')

    def handle_create_medicament(self):
        """
        Permite utilizatorului sa adauge un medicament in farmacie.
        :return:
        """
        try:
            id_medicament = input('ID-ul medicamentului: ').strip()
            nume = input('Numele medicamentului: ').strip()
            producator = input('Producatorul medicamentului: ').strip()
            pret = float(input('Pretul medicamentului: '))
            reteta = input('Necesita reteta: ')

            self.__medicament_service.create(id_medicament, nume, producator, pret, reteta)

            print('Medicamentul a fost adaugat cu succes!')
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def handle_show_all_medicament(self):
        """
        Permite utilizatorului sa afiseze toate medicamentele din farmacie.
        :return:
        """
        for medicament in self.__medicament_service.get_all():
            print(medicament)

    def handle_delete_medicament(self):
        """
        Permite utilizatorului sa stearga un medicament din farmacie.
        :return:
        """
        try:
            id_medicament = input('ID-ul medicamentului care se va sterge: ')
            self.__medicament_service.delete(id_medicament)
            print('Medicamentul a fost sters!')
        except KeyError as ke:
            print(ke)

    def handle_update_medicament(self):
        """
        Permite utilizatorului sa modifice caracteristicile unui medicament din farmacie.
        :return:
        """
        try:
            id_medicament = input('ID-ul medicamentului: ').strip()
            nume = input('Numele medicamentului (gol pt a nu schimba): ').strip()
            producator = input('Producatorul medicamentului (gol pt a nu schimba): ').strip()
            pret = float(input('Pretul medicamentului (gol pt a nu schimba): '))
            reteta = input('Necesita reteta (gol pt a nu schimba): ')

            self.__medicament_service.update(id_medicament, nume, producator, pret, reteta)

            print('Medicamentul a fost modificat cu succes!')
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def handle_generari_random(self):
        """
        Permite utilizatorului sa adauge/genereze un numar dat de medicamente random in farmacie.
        :return:
        """
        try:
            medicamente_number = int(input('Dati numarul de medicamente spre generare: ').strip())
            generated_list = self.__medicament_service.generate_medicamente(medicamente_number)
            for each_medicament in generated_list:
                print(each_medicament)
            print(f'\nBaza de date a fost populata cu {len(generated_list)} medicamente aleatorii!')
        except KeyError as ke:
            print(f'\nEroare: \n{ke}\n --> reincearca!\n')

    def __run_excel_tabel(self):

        try:
            self.__medicament_service.excel_tabel()
            print('Medicamentele au fost exportate')

        except:
            print('Eroare!Reincearca!')

    def run_crud_clienti(self):
        while True:
            print('\n--------------------------------------------------------------------')
            print('1-->Create client.')
            print('2-->Delete client.')
            print('3-->Update client.')
            print('a-->Show all clienti.')
            print('b-->Back')
            print('--------------------------------------------------------------------\n')
            option = input('Alegeti optiunea: ')
            if option == '1':
                self.handle_create_client()
            elif option == '2':
                self.handle_delete_client()
            elif option == '3':
                self.handle_update_client()
            elif option == 'a':
                self.handle_show_all_client()
            elif option == 'b':
                break
            else:
                print('Optiune invalida.')

    def handle_create_client(self):
        """
        Permite utilizatorului sa adauge un client in farmacie.
        :return:
        """
        try:
            id_card_client = input('ID-ul cardului clientului: ').strip()
            nume = input('Numele clientului: ').strip()
            prenume = input('Prenumele clientului: ').strip()
            cnp = input('CNP-ul clientului: ').strip()
            read_date = input('Dati data inregistrarii (zz.ll.aaaa): ').strip()

            read_date = read_date.split('.')
            data_inregistrarii = date(int(read_date[2]), int(read_date[1]), int(read_date[0]))

            self.__client_service.create(id_card_client, nume, prenume, cnp, data_inregistrarii)

            print('Clientul a fost adaugat cu succes!')
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def handle_show_all_client(self):
        """
        Permite utilizatorului sa afiseze toti clientii din farmacie.
        :return:
        """
        for client in self.__client_service.get_all():
            print(client)

    def handle_delete_client(self):
        """
        Permite utilizatorului sa stearga un client din farmacie.
        :return:
        """
        try:
            id_card_client = input('ID-ul clientului care se va sterge: ')
            self.__client_service.delete(id_card_client)
            print('Clientul a fost sters!')
        except KeyError as ke:
            print(ke)

    def handle_update_client(self):
        """
        Permite utilizatorului sa modifice caracteristicile unui client din farmacie.
        :return:
        """
        try:
            id_card_client = input('ID-ul cardului client: ').strip()
            nume = input('Numele clientului (gol pt a nu schimba): ').strip()
            prenume = input('Prenumele clientului (gol pt a nu schimba): ').strip()
            cnp = input('CNP-ul clientului : ').strip()
            data_inregistrarii = input('Data inregistrarii clientului zz.ll.aaaa : ').strip()

            self.__client_service.update(id_card_client, nume, prenume, cnp, data_inregistrarii)

            print('Clientul a fost modificat cu succes!')
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def run_crud_tranzactii(self):
        while True:
            print('\n--------------------------------------------------------------------')
            print('1-->Create tranzactie.')
            print('2-->Delete tranzactie.')
            print('3-->Update tranzactie.')
            print('a-->Show all tranzactii.')
            print('b-->Back')
            print('--------------------------------------------------------------------\n')
            option = input('Alegeti optiunea: ')
            if option == '1':
                self.handle_create_tranzactie()
            elif option == '2':
                self.handle_delete_tranzactie()
            elif option == '3':
                self.handle_update_tranzactie()
            elif option == 'a':
                self.handle_show_all_tranzactii()
            elif option == 'b':
                break
            else:
                print('Optiune invalida.')

    def handle_create_tranzactie(self):
        """
        Permite utilizatorului sa creeze o tranzactie in farmacie.
        :return:
        """
        try:
            id_tranzactie = input('ID-ul tranzactiei clientului: ').strip()
            id_medicament = input('ID-ul medicamentului: ').strip()
            id_card_client = input('ID-ul clientului: ').strip()
            nr_bucati = int((input('Numarul de bucati: ')).strip())
            read_date = input('Data tranzactiei zz.ll.aaaa: ').strip().split('.')
            data = date(int(read_date[2]), int(read_date[1]), int(read_date[0]))
            read_ora = input('Ora tranzactiei ora:min: ').strip().split(':')
            ora = time(int(read_ora[0]), int(read_ora[1]))

            self.__tranzactie_service.create(id_tranzactie, id_medicament, id_card_client, nr_bucati, data, ora)

            print('Tranzactia a fost adaugata cu succes!')
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def handle_show_all_tranzactii(self):
        """
        Permite utilizatorului sa afiseze toate tranzactiile din farmacie.
        :return:
        """
        for tranzactie in self.__tranzactie_service.get_all():
            print(tranzactie)

    def handle_delete_tranzactie(self):
        """
        Permite utilizatorului sa stearga o tranzactie din farmacie.
        :return:
        """
        try:
            id_tranzactie = input('ID-ul tranzactiei care se va sterge: ')
            self.__tranzactie_service.delete(id_tranzactie)
            print('Tranzactia a fost stearsa!')
        except KeyError as ke:
            print(ke)

    def handle_update_tranzactie(self):
        """
        Permite utilizatorului sa modifice o tranzactie din farmacie.
        :return:
        """
        try:
            id_tranzactie = input('ID-ul tranzactiei clientului: ').strip()
            id_medicament = input('ID-ul medicamentului: ').strip()
            id_card_client = input('ID-ul clientului: ').strip()
            nr_bucati = input('Numarul de bucati (gol pt a nu schimba): ')
            read_data = input('Data zz.ll.aaaa (gol pt a nu schimba): ')
            read_ora = input('Ora hh:mm (gol pt a nu schimba): ')

            if read_data != '':
                read_data = read_data.split('.')
                data = date(int(read_data[2]), int(read_data[1]), int(read_data[0]))
            else:
                data = ''

            if read_ora != '':
                read_ora = read_ora.split(':')
                ora = time(int(read_ora[0]), int(read_ora[1]))
            else:
                ora = ''

            self.__tranzactie_service.update(id_tranzactie, id_medicament, id_card_client, nr_bucati, data, ora)

            print('Tranzactia a fost modificata cu succes!')
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def __handle_numarare_vanzari(self):
        """
        Permite utilizatorului sa sorteze descrescator medicamentele dupa numarul de vanzari.
        :return:
        """
        med_sorted = self.__tranzactie_service.numarare_vanzari()
        for each_id_med in med_sorted:
            print(f'Vanzari:{med_sorted[each_id_med]}/', end='')
            print(self.__medicament_service.read_by_id(each_id_med))

    def __handle_full_text_search(self):
        """
        Permite utilizatorului sa caute medicamente si clienti dupa nume, prenume, producator, CNP etc.
        Cautare full text.
        :return:
        """
        try:
            string_to_search = input('Introduceti ce cautati: ').strip()
            if string_to_search == '':
                raise KeyError('\nSecventa de cautat este goala.')

            search_results = self.__medicament_service.full_search(
                string_to_search) + self.__client_service.full_search(string_to_search)
            if len(search_results) == 0:
                print('\nNu au fost gasite rezultate!\n')
            else:
                print(f'\nRezultatele cautarii: ({len(search_results)} matches)\n')
                for result in search_results:
                    print(result)
                print()
        except Exception as ex:
            print(f'\nEroare: \n{ex}\n --> reincearca!\n')

    def __handle_afisare_tranzactii_interval_dat(self):
        """
        Permite utilizatorului sa afiseze tranzactiile dintr-un interval dat.
        :return:
        """
        try:
            read_start = input('Dati data de inceput (zz.ll.aaaa): ').strip().split('.')
            start_data = date(int(read_start[2]), int(read_start[1]), int(read_start[0]))
            read_end = input('Dati data de sfarsit (zz.ll.aaaa): ').strip().split('.')
            end_data = date(int(read_end[2]), int(read_end[1]), int(read_start[0]))

            tranzactii_list = self.__tranzactie_service.get_tranzactii_by_interval_de_zile(start_data, end_data)
            print()
            if len(tranzactii_list) == 0:
                print(
                    f'\nNu exista tranzactii intre zilele {start_data.strftime("%Z.%L")}-{end_data.strftime("%Z.%L")}.')
            else:
                for each_tranzactie in tranzactii_list:
                    print(each_tranzactie)
            print()
        except Exception as ex:
            print(f'\nEroare: \n{ex}\nProblema posibila: datele introduse sunt invalide\n --> reincearca!\n')

    def __handle_scumpire_medicament(self):
        """
        Permite utilizatorului sa scumpeasca pretul unui medicament mai mic decat un pret dat.
        :return:
        """
        try:
            read_pret = float(input('Dati pretul dupa care se compara : '))
            pret_increase = float(input('Dati scumpirea aplicata: '))

            scumpire = self.__medicament_service.apply_scumpire_med(read_pret, pret_increase)
            print()
            if scumpire == 0:
                print('Nu au fost gasite medicamente cu pretul mai mic decat pretul precizat.')
            else:
                print(f'Au fost acordate {scumpire} de scumpiri!')
            print()
        except Exception as ex:
            print(f'\nEroare: \n{ex}\n --> reincearca!\n')

    def __handle_delete_tranzactii_in_interval(self):
        """
        Permite utilizatorului sa stearga tranzactiile dintr-un interval dat.
        :return:
        """
        try:
            read_start = input('Dati data de inceput (zz.ll.aaaa): ').strip().split('.')
            start_day = date(int(read_start[2]), int(read_start[1]), int(read_start[0]))
            read_stop = input('Dati data de final (zz.ll.aaaa): ').strip().split('.')
            stop_day = date(int(read_stop[2]), int(read_stop[1]), int(read_stop[0]))

            deletions = self.__tranzactie_service.delete_in_interval(start_day, stop_day)
            print()
            if deletions == 0:
                print('Nu au fost gasite tranzactii in perioada precizata.')
            else:
                print(f'Au fost sterse {deletions} tranzactii cu succes!')
            print()
        except Exception as ex:
            print(f'\nEroare: \n{ex}\n --> reincearca!\n')

    def __handle_client_desc_dupa_reducere(self):
        sorted_clienti = self.__tranzactie_service.sort_dupa_reduceri_desc()
        print()
        if len(sorted_clienti) == 0:
            print('Nu exista carduri ale clientilor in memorie.')
        else:
            for each_client in sorted_clienti:
                print(each_client)
        print()

    def __handle_export_clienti(self):
        try:
            self.__client_service.export_clienti()
            print("Clientii au fost exportati cu succes")
        except Exception as e:
            print(f'Eroare: {e}')

    def run_operatiuni(self):
        while True:
            print('\n--------------------------------------------------------------------')
            print('1-->Cautare medicamente si clienti dupa nume, producdator, prenume, cnp etc.')
            print('2-->Afisarea tuturor tranzactiilor dintr-un interval de zile dat.')
            print('3-->Afisarea medicamentelor ordonate descrescator dupa numarul de vanzari.')
            print('4-->Afisarea cardurilor client ordonate descrescator dupa valoarea reducerilor obtinute.')
            print('5-->Stergerea tuturor tranzactiilor dintr-un anumit interval de zile.')
            print('6-->Scumpirea cu un procentaj dat a tuturor medicamentelor cu pretul mai mic decat o valoare data.')
            print('7-->Generare medicamente random.')
            print('8-->Exporta clientii in fisier html')
            print('9-->Exporta medicamentele in tabel excel')
            print('b-->Back')
            print('--------------------------------------------------------------------\n')
            option = input('Alegeti optiunea: ')
            if option == '1':
                self.__handle_full_text_search()
            if option == '2':
                self.__handle_afisare_tranzactii_interval_dat()
            elif option == '3':
                self.__handle_numarare_vanzari()
            elif option == '4':
                self.__handle_client_desc_dupa_reducere()
            elif option == '5':
                self.__handle_delete_tranzactii_in_interval()
            elif option == '6':
                self.__handle_scumpire_medicament()
            elif option == '7':
                self.handle_generari_random()
            elif option == '8':
                self.__handle_export_clienti()
            elif option == '9':
                self.__run_excel_tabel()
            elif option == 'b':
                break
            else:
                print('Optiune invalida.')
