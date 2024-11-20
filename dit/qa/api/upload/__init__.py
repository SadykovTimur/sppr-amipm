import requests


def upload(url: str, token: str, path: str) -> int:
    headers = {
        "Authorization": token
    }

    with open(path, 'rb') as file:
        response = requests.post(
            url=url,
            headers=headers,
            files={'file': file},
            timeout=300,
        )

    return response.status_code
