import math

class ZipApp:

    def __init__(self):
        self.data = self.get_all_zip()

    def get_all_zip(self):
        i = 0
        header = []
        zip_codes = []
        zip_data = []
        skip_line = False
        # http://notebook.gaslampmedia.com/wp-content/uploads/2013/08/zip_codes_states.csv
        for line in open('DAL/zip_codes_states.csv').read().split("\n"):
            skip_line = False
            m = line.strip().replace('"', '').split(",")
            i += 1
            if i == 1:
                for val in m:
                    header.append(val)
            else:
                zip_data = []
                for idx in range(0, len(m)):
                    if m[idx] == '':
                        skip_line = True
                        break
                    if header[idx] == "latitude" or header[idx] == "longitude":
                        val = float(m[idx])
                    else:
                        val = m[idx]
                    zip_data.append(val)
                if not skip_line:
                    zip_codes.append(zip_data)
        return zip_codes

    def calculate_distance(location1, location2):
        lat1 = math.radians(location1[0])
        lat2 = math.radians(location2[0])
        long1 = math.radians(location1[1])
        long2 = math.radians(location2[1])
        del_lat = (lat1 - lat2) / 2
        del_long = (long1 - long2) / 2
        angle = math.sin(del_lat) ** 2 + math.cos(lat1) * math.cos(lat2) * \
                math.sin(del_long) ** 2
        distance = 2 * 3959.191 * math.asin(math.sqrt(angle))
        return distance

    def degree_minutes_seconds(location):
        minutes, degrees = math.modf(location)
        degrees = int(degrees)
        minutes *= 60
        seconds, minutes = math.modf(minutes)
        minutes = int(minutes)
        seconds = 60 * seconds
        return degrees, minutes, seconds

    def format_location(location):
        ns = ""
        if location[0] < 0:
            ns = 'S'
        elif location[0] > 0:
            ns = 'N'

        ew = ""
        if location[1] < 0:
            ew = 'W'
        elif location[0] > 0:
            ew = 'E'

        format_string = '{:03d}\xb0{:0d}\'{:.2f}"'
        latdegree, latmin, latsecs = ZipApp.degree_minutes_seconds(abs(location[0]))
        latitude = format_string.format(latdegree, latmin, latsecs)
        longdegree, longmin, longsecs = ZipApp.degree_minutes_seconds(abs(location[1]))
        longitude = format_string.format(longdegree, longmin, longsecs)
        return '(' + latitude + ns + ',' + longitude + ew + ')'

    def zip_by_location(self, codes, location):
        zips = []
        # codes = self.get_src_data()
        for code in codes:
            if location[0].lower() == code[3].lower() and \
                    location[1].lower() == code[4].lower():
                zips.append(code[0])
        return zips

    def location_by_zip(self, codes, zipcode):
        for code in codes:
            if code[0] == zipcode:
                return tuple(code[1:])
        return ()

    def process_loc(self, zipcode):
        codes = self.data
        location = self.location_by_zip(codes, zipcode)
        return location

    def process_zip(self, city, state):
        codes = self.data
        city = city.strip().title()
        state = state.strip().upper()
        zipcodes = self.zip_by_location(codes, (city, state))
        return zipcodes


    def process_dist(self, zip1, zip2):
        codes = self.data
        locations = []
        location1 = self.location_by_zip(codes, zip1)
        locations.append(location1)
        location2 = self.location_by_zip(codes, zip2)
        locations.append(location2)
        return locations