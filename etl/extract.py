import requests
import time

def extract(url):
  try:
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    print(f"Successfully accessed: {url}")
    raw_data_list = []
    for p in response['results']:
      raw_data = requests.get(p['url']).json()
      raw_data_list.append(raw_data)
      time.sleep(0.6)
    return raw_data_list  
  except requests.exceptions.ConnectionError as e:
    print(f"Error: Could not connect to {url}. Reason: {e}")
  except requests.exceptions.HTTPError as e:
      print(f"Error: HTTP error occurred for {url}. Status code: {e.response.status_code}")
  except requests.exceptions.RequestException as e:
      print(f"An unexpected error occurred during the request to {url}: {e}")

  return []