import json
import PySimpleGUI as psg

# Load data from JSON file
with open('clubs_data.json', 'r', encoding='utf-8') as json_file:
  data = json.load(json_file)


def get_existing_clubs(data):
  club_names = [club_info["club"] for club_info in data]
  return club_names


def get_title_list(title_data):
  """
  This function creates a formatted string listing all titles in the provided data.
  """
  if not title_data:
    return "No hay títulos."
  title_list = ""
  for title in title_data:
    title_list += f"- {title['name']} ({title['year']})\n"
  return title_list.rstrip("\n")  # Remove trailing newline


def get_club_info(club_name):
  """
  This function retrieves and formats all club information, including title lists.
  """
  for club_info in data:
    if club_info["club"] == club_name:
      club_data = f"Club: {club_info['club']}\n\n"
      # Get formatted lists for each title category
      liga_titles = get_title_list(club_info["nac_titles"])
      copa_titles = get_title_list(club_info["loc_titles"])
      int_titles = get_title_list(club_info["int_titles"])
      # Combine title information
      club_data += f"Ligas Nacionales:\n{liga_titles}\n\n"
      club_data += f"Copas Nacionales:\n{copa_titles}\n\n"
      club_data += f"Títulos Internacionales:\n{int_titles}"
      return club_data
  return None  # Return None if club not found


existing_clubs = get_existing_clubs(data)
existing_clubs.sort()

# Define the GUI layout
layout = [[psg.Text('Elegir equipo', size=(20, 1), font='Lucida', justification='left')],
          [psg.Combo(existing_clubs, default_value='Club Atlético San Lorenzo de Almagro', key='equipo')],
          [psg.Button('Mostrar Títulos', font=('Times New Roman', 12))],
          [psg.Multiline(size=(40, 15), key='club_info')],  # Increased size for potentially longer titles
          [psg.Button('SALIR', font=('Times New Roman', 12))]]

# Create the window
win = psg.Window('Customise your Journey', layout)

# Event Loop
while True:
  event, values = win.read()

  if event == psg.WIN_CLOSED or event == 'SALIR':
    break

  if event == 'Mostrar Títulos':  # Button click event
    equipo = values["equipo"]
    club_info = get_club_info(equipo)

    if club_info:
      win['club_info'].update(club_info)  # Update multiline element with all info
    else:
      win['club_info'].update("Equipo no encontrado.")  # Update with error message

win.close()