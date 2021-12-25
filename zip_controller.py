from zip_model import ZipApp
import math
import logging
import logging.handlers
import zip_view


def eng_handler(lang):
    command = ""
    lang = 'eng'
    while command != 'back':
        command = input("Command ('loc', 'zip', 'dist', 'back') => ")
        # logging.info(f'Received command {command}')
        logger.info(f'Received command {command}')
        command = command.strip().lower()
        if command == 'loc':
            zipcode = input('Enter ZIP code => ')
            print('...' + zipcode)
            location = ZipApp().process_loc(zipcode)
            zip_view.view_process_loc(location, zipcode, lang)
            print()
        elif command == 'zip':
            city = input('Enter a city name to lookup => ')
            print('...' + city)
            state = input('Enter the state name to lookup => ')
            print('...' + state)
            zipcodes = ZipApp().process_zip(city, state)
            zip_view.view_process_zip(city, state, zipcodes, lang)
            print()
        elif command == 'dist':
            zip1 = input('Enter the first ZIP Code => ')
            print(zip1)
            zip2 = input('Enter the second ZIP Code => ')
            print(zip2)
            locations = ZipApp().process_dist(zip1, zip2, )
            zip_view.view_process_dist(locations[0], locations[1], zip1, zip2, lang)
            print()
        elif command != 'back':
            print("Invalid command, ignoring")
    print("...back to root menu")


def ru_handler(lang):
    command = ""
    lang = 'rus'
    while command != 'back':
        command = input("Введите команду ('loc', 'zip', 'dist', 'back') => ")
        # logging.info(f'Received command {command}')
        logger.info(f'Received command {command}')
        command = command.strip().lower()
        if command == 'loc':
            zipcode = input('Введите почтовый индекс => ')
            print('...' + zipcode)
            location = ZipApp().process_loc(zipcode)
            zip_view.view_process_loc(location, zipcode, lang)
            print()
        elif command == 'zip':
            city = input('Введите название города для поиска => ').strip().title()
            print('...' + city)
            state = input('Введите название штата для поиска => ').strip().upper()
            print('...' + state)
            zipcodes = ZipApp().process_zip(city, state)
            zip_view.view_process_zip(city, state, zipcodes, lang)
            print()
        elif command == 'dist':
            zip1 = input('Введите почтовый индекс места отправления => ')
            print(zip1)
            zip2 = input('Введите почтовый индекс места назначения => ')
            print(zip2)
            locations = ZipApp().process_dist(zip1, zip2)
            zip_view.view_process_dist(locations[0], locations[1], zip1, zip2, lang)
            print()
        elif command != 'back':
            print("Каманда не распознана, повторите ввод")
    print("...возвращаемся на предыдущий уровень меню")


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    rfh = logging.handlers.RotatingFileHandler(
        filename='zip_app.log',
        mode='a',
        maxBytes=5*1024*1024,
        backupCount=9,
        encoding=None,
        delay=0
    )
    logging.basicConfig(format='%(asctime)s: %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO, datefmt="%y-%m-%d %H:%M:%S",
                        handlers=[rfh])
    logger = logging.getLogger('main')

    lang = ""
    while lang != 'end':
        lang = input("Выберете язык интерфейса ('rus', 'eng'), либо ('end') для завершения работы => ")
        lang = lang.strip().lower()
        if lang == 'rus':
            print('...выбран русский язык интерфейса')
            ru_handler(lang)
        elif lang == 'eng':
            print('...set Eng as GUI lang')
            eng_handler(lang)
        elif lang != 'end':
            print('...повторите ввод командлета')
        print()
    print("...работа завершена")

    logging.shutdown()

