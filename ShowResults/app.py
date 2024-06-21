from flask import Flask, render_template, request
import json
import sys
import os

current_working_directory = os.getcwd()
parent_working_directory = os.path.abspath(os.path.join(current_working_directory, os.pardir))
misc_dir =  os.path.join(parent_working_directory,"Promiedos")
sys.path.append(misc_dir)
from misc import read_cfg_yaml,set_yaml_file



cfg_params = read_cfg_yaml(set_yaml_file()) # YAML settable params

INPUT_DATA_PATH = cfg_params['INPUT_DATA_PATH']
input_file_folder = os.path.join(parent_working_directory,INPUT_DATA_PATH)
INPUT_DATA_FILENAME = cfg_params['INPUT_DATA_FILENAME']
input_file = os.path.join(input_file_folder, INPUT_DATA_FILENAME)

# Load data from JSON file
with open(input_file, 'r', encoding='utf-8') as json_file:
  data = json.load(json_file)

def get_existing_clubs():
  club_names = [club_info["club"] for club_info in data]
  club_names.sort()
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

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  existing_clubs = get_existing_clubs()
  selected_club = request.form.get('equipo')
  club_info = None
  if selected_club:
    club_info = get_club_info(selected_club)

  return render_template('index.html', existing_clubs=existing_clubs, selected_club=selected_club, club_info=club_info)

if __name__ == '__main__':
  app.run(debug=True)