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
        match gui.show_menu(options):
            case 0:
                return monthly.generate()
            case 1:
                return quarterly.generate()
            case 2:
                settings()
            case _:
                return 1


def settings():
    # TODO - Review and create new types of acts
    ...

    # TODO - Select which acts are mandatory
    ...

    # TODO - Select last volunteer with 20 years of service
    ...


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, 'es_CL.utf8')
    sys.exit(main())
