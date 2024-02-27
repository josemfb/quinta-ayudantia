# pyinstaller -F -w -n "ayudantia" --add-data "logo.png:." --exclude-module "config.py" main.py

import locale
import sys

import gui
import quarterly
import monthly


def main() -> int:
    options = ["Cuadro mensual y parte de asistencias",
               "Cuadro de obligatorios trimestrales y porcentajes",
               "Configuración"]
    while True:
        match gui.show_menu(options, title="Automatizador de la Ayudantía"):
            case 0:
                return monthly.generate()
            case 1:
                return quarterly.generate()
            case 2:
                return settings()
            case _:
                return 1


def settings():
    options = ["Revisar listado de actos obligatorios",
               "Modificar último voluntario con premio de 20",
               "Acerca de este programa", ]
                # "Crear nuevo tipo de acto"]

    while True:
        match gui.show_menu(options, title="Configuración"):
            case 0:
                # TODO - Select which acts are mandatory
                ...
            case 1:
                # TODO - Select last volunteer with 20 years of service
                ...
            # case 2:
                # TODO - Review and create new types of acts
                ...
            case 2:  # case 3:
                msg = ("Automatizador de tareas de la ayudantía.                                                     \n"
                       "Creado por José Fernández B. (jose.fernandez@5.cbs.cl)")
                gui.show_message(title="Acerca de", message=msg)
                return 0
            case _:
                return 1


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, 'es_CL.utf8')
    sys.exit(main())
