import requests
import pandas as pd

def check_gdc_status():
    """Check the status of the Genomic Data Commons API."""
    url = "https://api.gdc.cancer.gov/status"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Successfully connected to GDC API!")
            print("Status Info:", response.json()['status'])
        else:
            print(f"Failed to connect. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    check_gdc_status()
