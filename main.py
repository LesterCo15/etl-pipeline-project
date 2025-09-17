from etl import extract, transform, load
from etl.utils import build_url
from dotenv import load_dotenv
import os

load_dotenv()

def main():
  base_url = os.getenv("BASE_URL")
  url = build_url(base_url, 20)
  raw_data = extract.extract(url)
  cleaned_data = transform.transform(raw_data)
  csv = load.load(cleaned_data, "pokemon.csv")
  load.load_to_db(csv, "postgres", "postgres", "localhost", 5433, "postgres_db")

if __name__ == '__main__':
  main()
