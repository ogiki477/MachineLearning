import requests
import csv

def get_species_list(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "recordings" in data:
            species_list = list({recording["sp"] for recording in data["recordings"]})
            return species_list
    else:
        print("Error: Unable to fetch data from the API.")
        return []

def save_to_csv(species_list, csv_file_path):
    with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Species"])  # Write header row
        writer.writerows([[species] for species in species_list])  # Write species names row by row

if __name__ == "__main__":
    url = "https://xeno-canto.org/api/2/recordings?query=sp&field=species"
    species_list = get_species_list(url)

    if species_list:
        print("This will give a list without duplicates:")
        print(species_list)

        csv_file_path = "birds.csv"
        save_to_csv(species_list, csv_file_path)

        print("Data saved to CSV file successfully.")
