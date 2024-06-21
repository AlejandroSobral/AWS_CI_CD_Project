import json
import tkinter as tk
from tkinter import ttk

def calculate_total_titles_in_range(club_info, start_year, end_year):
    total_titles = {"Amateur": 0, "Profesional": 0}
    fetched_titles = []
    for title_type in ["nac_titles", "int_titles", "loc_titles"]:
        for title in club_info[title_type]:
            title_year = int(title["year"])
            if start_year <= title_year <= end_year:
                total_titles[title["category"]] += 1
                title_type_name = "Copa Nacional" if title_type == "nac_titles" else (
                    "Título Internacional" if title_type == "int_titles" else "Liga Nacional"
                )
                title_info = {
                    "type": title_type_name,
                    "name": title["name"],
                    "year": title["year"],
                    "category": title["category"]
                }
                fetched_titles.append(title_info)
    total_titles["Total"] = sum(total_titles.values())
    return total_titles, fetched_titles

def sort_clubs_by_total_titles_in_range(data, start_year, end_year):
    sorted_clubs = sorted(data, key=lambda club_info: calculate_total_titles_in_range(club_info, start_year, end_year)[0]["Total"], reverse=True)
    return sorted_clubs

def show_results():
    start_year = int(start_year_entry.get())
    end_year = int(end_year_entry.get())

    sorted_clubs = sort_clubs_by_total_titles_in_range(data, start_year, end_year)

    result_text.delete(1.0, tk.END)

    result_text.insert(tk.END, f"{'Club':<40} {'Amateur':<10} {'Profesional':<10} {'Total':<10}\n")
    result_text.insert(tk.END, "-" * 70 + "\n")
    
    for club_info in sorted_clubs:
        total_titles, fetched_titles = calculate_total_titles_in_range(club_info, start_year, end_year)
        total_titles_count = total_titles["Total"]
        if total_titles_count > 0:
            club_name = club_info["club"]
            result_text.insert(tk.END, f"{club_name:<40} {total_titles['Amateur']:<10} {total_titles['Profesional']:<10} {total_titles_count:<10}\n")
            if print_titles_var.get():
                for title in fetched_titles:
                    result_text.insert(tk.END, f"    {title['type']} - {title['name']} ({title['year']})\n")
                result_text.insert(tk.END, "\n")
                
                

input_file = "clubs_data.json"

with open(input_file, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Football Titles Analyzer")

# Create a style for the labels and entries
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))

# Create and pack the starting year widgets
start_year_label = ttk.Label(root, text="Enter the starting year:")
start_year_label.pack(fill="both", padx=10, pady=5)

start_year_entry = ttk.Entry(root)
start_year_entry.pack(fill="both", padx=10, pady=5)

# Create and pack the ending year widgets
end_year_label = ttk.Label(root, text="Enter the ending year:")
end_year_label.pack(fill="both", padx=10, pady=5)

end_year_entry = ttk.Entry(root)
end_year_entry.pack(fill="both", padx=10, pady=5)

# Create and pack the checkbox widget
print_titles_var = tk.BooleanVar()
print_titles_checkbox = ttk.Checkbutton(root, text="Print individual titles", variable=print_titles_var)
print_titles_checkbox.pack(fill="both", padx=10, pady=5)

# Create and pack the Show Results button
show_results_button = ttk.Button(root, text="Show Results", command=show_results)
show_results_button.pack(fill="both", padx=10, pady=10)

# Create and pack the result text widget
result_text = tk.Text(root, height=20, width=80)
result_text.pack(fill="both", padx=10, pady=10)

root.mainloop()