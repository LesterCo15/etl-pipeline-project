import csv
import pandas as pd
from sqlalchemy import create_engine

def load(data: list, csv_file: str):
  if not data:  # covers [] or None
      print("No data to write. Skipping CSV export.")
      return 
  
  with open(csv_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

  print(f"Saved {len(data)} records to {csv_file}")
  return csv_file



def load_to_db(csv_file: str, user: str, password: str, host: str,
               port: int, db: str):
    df = pd.read_csv(csv_file)

    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}")

    df.to_sql("pokemon_table", engine, if_exists="replace", index=False)
    print("✅ CSV loaded into Postgres via pandas")
