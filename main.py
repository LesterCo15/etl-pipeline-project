from etl import extract, transform, load
from etl.utils import get_base_url

def main():
  url = get_base_url()
  raw_data = extract.extract(url, 1)
  print("Extracted:", type(raw_data), len(raw_data))
  cleaned_data = transform.transform(raw_data)
  load.load(cleaned_data, "pokemon.csv")

if __name__ == '__main__':
  main()
