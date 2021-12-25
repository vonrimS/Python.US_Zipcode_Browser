from zip_model import ZipApp
import logging
import logging.handlers


def view_process_loc(location, zipcode, lang):
    if lang == 'eng':
        if len(location) > 0:
            print(f'ZIP Code {zipcode} is in {location[2]}, {location[3]}, {location[4]} county,'
                  f'\ncoordinates: {ZipApp.format_location((location[0], location[1]))}')
        else:
            print('Invalid or unknown ZIP Code')
    elif lang == 'rus':
        if len(location) > 0:
            print(f'Почтовый индекс {zipcode} в локации {location[2]}, {location[3]}, местность {location[4]},'
                  f'\nкоординаты: {ZipApp.format_location((location[0], location[1]))}')
        else:
            print('Неизвестный почтовый индекс')

def view_process_zip(city, state, zipcodes, lang):
    if lang == 'eng':
        if len(zipcodes) > 0:
            print('The following ZIP Code(s) found for {}, {}: {}'.
                  format(city, state, ", ".join(zipcodes)))
        else:
            print('No ZIP Code found for {}, {}'.format(city, state))
    elif lang == 'rus':
        if len(zipcodes) > 0:
            print('Следующие почтовые индексы были найдены для {}, {}: {}'.
                  format(city, state, ", ".join(zipcodes)))
        else:
            print('Никаких почтовых индексов не обнаружено для {}, {}'.format(city, state))

def view_process_dist(location1, location2, zip1, zip2, lang):
    if lang == 'eng':
        if len(location1) == 0 or len(location2) == 0:
            print('The distance between {} and {} cannot be determined'.
                  format(zip1, zip2))
        else:
            dist = ZipApp.calculate_distance(location1, location2)
            print('The distance between {} and {} is {:.2f} miles'.
                  format(zip1, zip2, dist))
    elif lang == 'rus':
        if len(location1) == 0 or len(location2) == 0:
            print('Расстояние между {} и {} не может быть подсчитано'
                  .format(zip1, zip2))
        else:
            dist = ZipApp.calculate_distance(location1, location2)
            print('Расстояние между {} и {} составляет {:.2f} мили'
                  .format(zip1, zip2, dist))