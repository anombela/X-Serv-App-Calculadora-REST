#!/usr/bin/python

import webapp
import socket


class calcres(webapp.webApp):

    def parse(self, request):

        orden = request.split()[0]
        cuerpo = request.split()[-1]
        return(orden, cuerpo)

    def process(self, parsedRequest):
        (orden,  body) = parsedRequest

        resultado = 0
        if (orden == "PUT"):
            self.operacion = body
            return ("200 OK", "<html><body>Operacion: "
                    + body + "</body></html>")
        elif (orden == "GET"):
            try:
                if (len(self.operacion.split('+')) == 2):
                    resultado = (float(self.operacion.split("+")[0]) +
                                 float(self.operacion.split("+")[1]))
                elif (len(self.operacion.split('-')) == 2):
                    resultado = (float(self.operacion.split("-")[0]) -
                                 float(self.operacion.split("-")[1]))
                elif (len(self.operacion.split('*')) == 2):
                    resultado = (float(self.operacion.split("*")[0]) *
                                 float(self.operacion.split("*")[1]))
                elif (len(self.operacion.split('/')) == 2):
                    resultado = (float(self.operacion.split("/")[0]) /
                                 float(self.operacion.split("/")[1]))
                return ("200 OK",
                        "<html><body>El resultado es: " +
                        str(resultado) + "</body></html>")
            except ValueError:
                return ("404 Not Found",
                        "<html><body>Error: ValueError</body></html>")
            except AttributeError:
                return ("404 Not Found",
                        "<html><body>Error: AttributeError</body></html>")

        else:
            return ("404 Non Found",
                    "<html><body>Operacion incorrecta</body></html>")

if __name__ == "__main__":
    serv = calcres(socket.gethostname(), 1234)
