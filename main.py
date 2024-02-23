# pyinstaller -F -w -n "ayudantia" --add-data "logo.png:." --exclude-module "config.py" main.py

import locale
import sys

import monthly


def main() -> int:
    # options = ["Reportes mensuales (cuadro y parte)",
    #            "Reportes trimestrales (obligatorios y porcentajes)",
    #            "Configuración"]
    # while True:
    #     match gui.menu(options):
    #         case 1:
    #             return generate_monthly()
    #         case 2:
    #             return generate_quarterly()
    #         case 3:
    #             settings()
    #         case _:
    #             return 1
    return generate_monthly()


def generate_monthly() -> int:
    to_return = 0
    to_return += monthly.full_report()

    return to_return


def generate_quarterly():
    # TODO - Generate report with mandatory acts of the quarter
    ...


def settings():
    # TODO - Review and create new types of acts
    # TODO - Select which acts are mandatory
    # TODO - Select last volunteer with 20 years of service
    ...


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, 'es_CL.utf8')
    sys.exit(main())
