import json

import requests

token = "452f24d302caccaddd2ee46f0e685e9b98794b416235f057e44707b00ac68552ef33235582a28cbff1e98"
base_api_url = "https://api.vk.com/method/"


def get_meme(save_json = False):
    payload = {
        'access_token': token,
        'owner_id': "-197700721",
        'album_id': "281940823",
        'extended': True,
        'v': "5.131"
    }
    response = requests.get(base_api_url + "photos.get", params = payload)
    if save_json:
        with open('mem.json', 'w', encoding = "utf-8") as writef:
            json.dump(response.json(), writef)
    return response.json()


def get_user_id_photo(list_memes: list):
    users_id = [str(mem['user_id']) for mem in list_memes]
    payload = {
        'access_token': token,
        'user_ids': ", ".join(users_id),
        'v': "5.131"
    }
    response = requests.get(base_api_url + "users.get", params = payload)
    return response.json()


def print_mem_w_author_and_likes(memes: list, names: list):
    for meme in memes:
        for name in names:
            if meme['user_id'] == name['id']:
                print(f"{name['first_name']} {name['last_name']} {meme['likes']['count']} {meme['id']}")
                continue


def read_mem():
    try:
        with open('mem.json', 'r', encoding = "utf-8") as readf:
            return json.load(readf)
    except Exception:
        return get_meme()


memes = read_mem().get("response").get("items")
names = get_user_id_photo(memes).get("response")
print_mem_w_author_and_likes(memes, names)
