from convert_year import convert_year
from replace_name_abbreviations import replace_name_abbreviations
from determine_category import determine_category
import re

def category_string(category):
    if(category == "LOC"):
        name = "Liga Nacional"
    if(category =="NAC"):
        name = "Copa Nacional"
    if(category =="INT"):
        name = "Copa Internacional"
    return name
        

def split_name_year(name_year_list, in_category):
    empty_list = []
    if(name_year_list == empty_list):
        return empty_list
    
    result = []
    try:
        for item in name_year_list:
            
            if len(item)== 4: #Titulo
                year = item
                result.append({'name': category_string(in_category), 'year': item, 'category': determine_category(year)})
                continue
            
            match = re.search(r'(\d{2}/\d{2}|\d{4})\s*(.+)', item)
            if match:
                year = convert_year(match.group(1))
                name = replace_name_abbreviations(match.group(2).strip())
                if (re.search(r"/", name)):
                 name = "Liga Nacional"
                category = determine_category(year)
                result.append({'name': name, 'year': year, 'category': category})
            else:
                match = re.search(r'(.+)\s*(\d{2}/\d{2}|\d{4})', item)
                if match:
                    name = replace_name_abbreviations(match.group(1).strip())
                    if (re.search(r"/", name)):
                        name = "Liga Nacional"
                    year = convert_year(match.group(2))
                    category = determine_category(year)
                    result.append({'name': name, 'year': year, 'category': category})
                else:
                    if (len(re.findall(r'\d+', item)[0]) == len(item)):
                        category = determine_category(year)
                        result.append({'name': "Liga Nacional", 'year': item, 'category': category})
        return result
    except:
        print(Exception)
        return result