def get_trph(div_tag, cat):
    
    ret_list = []
    found = False
    
    if (div_tag.contents == ret_list):
        return ret_list
    
    if(cat == "LOC"): #Torneo Liga de 1era
        lookup_string = "Torneos de Primera Division"
    elif (cat=="NAC"): #Copa Nacional
        lookup_string = "Copas Nacionales"
    elif (cat=="INT"):
        lookup_string = "Copas Internacionales Oficiales"
    
    
    for index, tag in enumerate(div_tag.contents):
        if(lookup_string in str(tag)):
            index = index + 4
            found = True
            break
    
    if(found == True):
        trph = div_tag.contents[index].text
        return trph.split(" - ")

    else:
        return ret_list