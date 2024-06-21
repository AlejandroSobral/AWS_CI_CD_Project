def convert_year(year):
    if len(year) == 5 and year[2] == '/':
        first_year = int('19' + year[:2])
        second_year = int('19' + year[3:])
        return f"{first_year}/{second_year}"
    return year