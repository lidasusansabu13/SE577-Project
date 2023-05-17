import os
import requests
from dotenv import load_dotenv

load_dotenv()


class GithubProxy:
    def __init__(self) -> None:
        self.base_url = os.getenv('GH_API_URL')
        self.access_token = os.getenv('GH_ACCESS_TOKEN')
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28'
        }

    def get_data(self, path):
        url = f'{self.base_url}{path}'
        try:
            response = requests.get(url, headers=self.headers, timeout=5)
            response.raise_for_status()  # Raise an exception if response status is not 2xx
            return response.json()
        except requests.exceptions.RequestException as error:
            print(f"Error occurred: {error}")
            return None
