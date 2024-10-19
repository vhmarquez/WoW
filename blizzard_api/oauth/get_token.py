from dotenv import load_dotenv
import json
import os

import httpx
from httpx_oauth.oauth2 import OAuth2

def get_token(username: str, password: str) -> str:
    try:
        auth = httpx.BasicAuth(username=username, password=password)
        data = {
            'grant_type': 'client_credentials'
        }
        response = httpx.post('https://oauth.battle.net/token', auth=auth, data=data)
        response.raise_for_status()

        auth_token = response.content
        print(json.dumps(json.loads(auth_token), sort_keys=True, indent=4))
        return auth_token
    except httpx.RequestError as exc:
        print(f"An error occurred while requesting {exc.request.url!r}.")
    except httpx.HTTPStatusError as exc:
        print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")

if __name__ == "__main__":

    load_dotenv()

    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')

    get_token(username=client_id, password=client_secret)