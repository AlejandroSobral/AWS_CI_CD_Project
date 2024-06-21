import json

def titles_accumulation(data):
    club_accumulation = {}
    all_years = set()

    for club_info in data:
        club_name = club_info["club"]
        nac_titles = club_info["nac_titles"]
        int_titles = club_info["int_titles"]
        loc_titles = club_info["loc_titles"]

        all_titles = nac_titles + int_titles + loc_titles
        all_titles.sort(key=lambda title: int(title["year"]))

        accumulation = 0
        for title in all_titles:
            year = title["year"]
            all_years.add(year)
            accumulation += 1
            if year not in club_accumulation:
                club_accumulation[year] = {}
            if club_name not in club_accumulation[year]:
                club_accumulation[year][club_name] = accumulation

    return club_accumulation

# Load data from the JSON file
with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Get the titles accumulation per club and year
accumulation_by_year = titles_accumulation(data)

# Prepare the final result in the desired format
final_result = []
for year in sorted(accumulation_by_year.keys()):
    year_data = {
        "year": year,
        "accumulation": accumulation_by_year[year]
    }
    final_result.append(year_data)

# Print the final result in JSON format
print(json.dumps(final_result, indent=4))
