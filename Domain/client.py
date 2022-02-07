from datetime import date

from Domain.entitate import Entitate


class Client(Entitate):
    """
    Descrie un client.
    """

    def __init__(self, id_card_client, nume, prenume, cnp, data_inregistrarii):
        super().__init__(id_card_client)
        self.__nume = nume
        self.__prenume = prenume
        self.__cnp = cnp
        year = int('20' + cnp[1] + cnp[2])
        if year > date.today().year:
            year = int('19' + cnp[1] + cnp[2])
        month = int(cnp[3] + cnp[4])
        day = int(cnp[5] + cnp[6])
        self.__data_nasterii = date(year, month, day)
        self.__data_inregistrarii = data_inregistrarii

    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, val):
        self.__nume = val

    @property
    def prenume(self):
        return self.__prenume

    @prenume.setter
    def prenume(self, val):
        self.__prennume = val

    @property
    def full_name(self):
        return self.__nume + ' ' + self.__prenume

    @property
    def cnp(self):
        return self.__cnp

    @cnp.setter
    def cnp(self, val):
        self.__cnp = val

    @property
    def data_nasterii(self):
        return self.__data_nasterii

    @property
    def data_inregistrarii(self):
        return self.__data_inregistrarii

    @data_inregistrarii.setter
    def data_inregistrarii(self, val):
        self.__data_inregistrarii = val

    def __str__(self):
        return f'{self.id_entitate} - nume:{self.nume}, prenume:{self.prenume}, cnp:{self.cnp} ' \
               f'data_nasterii:{self.data_nasterii}; data_inregistrarii: {self.data_inregistrarii}'

    def search(self, string_to_search):
        for prop in [self.full_name, self.cnp, str(self.data_nasterii), str (self.data_inregistrarii)]:
            if string_to_search in prop:
                return True
        return False

    @staticmethod
    def exportClient(client):
        """
        file << "<tr>\n";
        file << "<td>"<<turret.getLocationOfTurret()<<"</td>\n";
        file << "<td>"<<turret.getSizeOfTurret()<<"</td>\n";
        file << "<td>"<<turret.getAuraLevelOfTurret()<<"</td>\n";
        file << "<td>"<<turret.getNumberOfSeparatePartsOfTurret()<<"</td>\n";
        file << "<td>"<<turret.getVisionOfTurret()<<"</td>\n";
        file << "</tr>\n";
        """
        client_html = ""
        client_html += "<tr>\n"
        client_html = client_html + "<td>" + str (client.id_entitate) + "</td>\n"
        client_html = client_html + "<td>" + client.nume + "</td>\n"
        client_html = client_html + "<td>" + client.prenume + "</td>\n"
        client_html = client_html + "<td>" + str (client.cnp) + "</td>\n"
        client_html = client_html + "<td>" + str (client.data_nasterii) + "</td>\n"
        client_html = client_html + "<td>" + str (client.data_inregistrarii) + "</td>\n"
        client_html += "</tr>\n"

        return client_html
