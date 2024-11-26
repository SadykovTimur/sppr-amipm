import json

import requests


def upload(url: str, token: str, path: str) -> str:
    headers = {"Authorization": token}

    with open(path, 'rb') as file:
        response = requests.post(
            url=url,
            headers=headers,
            files={'file': file},
            timeout=300,
        )

    assert response.status_code == 200, f"Загрузка файла не была произведена. Код ответа {response.status_code}"

    res = json.loads(response.text)

    return res['tempFileId']


def save_file(token: str, temp_file_ids: list, materials_id: str, names: list):
    headers = {"Authorization": token}

    response = requests.patch(
        url=f'https://office.mos.ru/api/new/Document/Many/{materials_id}',
        headers=headers,
        data={
            "models[0].tempId": 0,
            "models[0].name": names[0],
            "models[0].documentType": "File",
            "models[0].parentId": materials_id,
            "models[0].tempFileId": temp_file_ids[0],
            "models[1].tempId": 1,
            "models[1].name": names[1],
            "models[1].documentType": "File",
            "models[1].parentId": materials_id,
            "models[1].tempFileId": temp_file_ids[1],
            "models[2].tempId": 2,
            "models[2].name": names[2],
            "models[2].documentType": "File",
            "models[2].parentId": materials_id,
            "models[2].tempFileId": temp_file_ids[2],
            "models[3].tempId": 3,
            "models[3].name": names[3],
            "models[3].documentType": "File",
            "models[3].parentId": materials_id,
            "models[3].tempFileId": temp_file_ids[3],
            "models[4].tempId": 4,
            "models[4].name": names[4],
            "models[4].documentType": "File",
            "models[4].parentId": materials_id,
            "models[4].tempFileId": temp_file_ids[4],
        },
        timeout=300,
    )

    assert response.status_code == 200, "Файлы не сохранены"


def get_event_materials_id(token: str) -> str:
    headers = {"Authorization": token}

    response = requests.get(url='https://office.mos.ru/api/new/CalendarEvent?', headers=headers, timeout=300)

    result = json.loads(response.text)

    return result['items'][-1]['materialsId']
