import sys
import dep_util
import dep_zip_app


def check_expected(cmd, result, expected):
    if type(result) != type(expected):
        print('The return value of {} is of type {}, not of type {}'.
              format(cmd, type(result), type(expected)))
    if result != expected:
        print('The return value of {} is {}, expected {}'.
              format(cmd, result, expected))


zip_codes = util.read_zip_all()


if sys.argv[1] == 'zip_by_location':
    try:
        result = zip_app.zip_by_location(zip_codes, ('trOy', 'nY'))
        check_expected('zip_app.zip_by_location(zip_codes, ('trOy', 'nY'))',
                       result, ['12179', '12180', '12181', '12182', '12183'])
        result = zip_app.zip_by_location(zip_codes, ('Mechanicsburg', 'pa'))
        check_expected('zip_app.zip_by_location(zip_codes, ('Mechanicsburg', 'pa'))',result, ['17055'])
        result = zip_app.zip_by_location(zip_codes, ('Helsinki', 'FI'))
        check_expected('zip_app.zip_by_location(zip_codes, ('Helsinki', 'FI'))', result, [])
    except Exception as e:
        print(e)
elif sys.argv[1] == 'location_by_zip':
    try:
        result = zip_app.location_by_zip(zip_codes, '17055')
        check_expected('zip_app.location_by_zip(zip_codes, '17055')',
                       result, (40.180953, -77.177086, 'Mechanicsburg', 'PA',
                                'Cumberland'))
        result = zip_app.location_by_zip(zip_codes, '96201')
        check_expected('zip_app.location_by_zip(zip_codes, '96201')',
                       result, ())
    except Exception as e:
        print(e)
