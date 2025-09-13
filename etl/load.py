import csv

def load(data: list, csv_file: str):
  with open(csv_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)