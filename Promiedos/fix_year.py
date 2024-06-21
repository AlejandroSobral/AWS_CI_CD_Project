
import json

def set_category_based_on_year(data):
    for club_info in data:
        for title_type in ["nac_titles", "int_titles", "loc_titles"]:
            for title in club_info[title_type]:
                title_year = int(title["year"])
                if title_year <= 1934:
                    title["category"] = "Amateur"
                else:
                    title["category"] = "Profesional"

# Calling the function to set categories

input_file = "clubs_data.json"
with open(input_file, "r", encoding="utf-8") as json_file:
    data = json.load(json_file)
set_category_based_on_year(data)

output_file = "clubs_data_fix1.json"
with open(output_file, "w") as json_file:
    json.dump(data, json_file, indent=4)