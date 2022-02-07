from Repository.client_repository import *

class ClientHTMLRepository:
    def __init__(self, filename):
        self.__filename = filename

    def export_clients(self, clienti):
        with open(self.__filename, "w") as file:
            '''
            file << "<!DOCTYPE html>\n";
            file << "<html>\n";
            file << "<head>\n";
            file << "<title>NorvenTurret</title>\n";
            file << "</head>\n";
            file << "<body>\n";
            file << "<table border=\"1\">\n";
            file << "<tr>\n";
            file << "<td>Location</td>\n";
            file << "<td>Size</td>\n";
            file << "<td>Aura Level</td>\n";
            file << "<td>Number of separate parts</td>\n";
            file << "<td>Vision</td>\n";
            file << "</tr>\n";
            '''
            file.write("<!DOCTYPE html>\n")
            file.write("<html>\n")
            file.write("<head>\n")
            file.write("<title>Clienti</title>\n")
            file.write("</head>\n")
            file.write("<body>\n")
            file.write("<table border=\"1\">\n")
            file.write("<tr>\n")
            file.write("<td>Id client</td>\n")
            file.write("<td>Nume</td>\n")
            file.write("<td>Prenume</td>\n")
            file.write("<td>CNP</td>\n")
            file.write("<td>Data nasterii</td>\n")
            file.write("<td>Data inregistrare</td>\n")
            file.write("</tr>\n")

            for client in clienti:
                file.write(Client.exportClient(client))

            file.write("</table>\n")
            file.write("</body>\n")
            file.write("</html>\n")
