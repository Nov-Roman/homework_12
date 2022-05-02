import json

from config import UPLOAD_FOLDER
from exceptions import DataJsonError, InvalidExtension


def load_json(file_name: json) -> list:
    """
    Возвращает список кандидатов
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError


def search_post_string(posts: list, string: str) -> list:
    """
    Возвращает список постов по запросу
    """
    posts_founded = []
    for post in posts:
        if string.lower() in post['content'].lower():
            posts_founded.append(post)
    return posts_founded


def save_new_post(file_name: str, posts: list) -> json:
    """
    Записывает изменения в файл json
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        return json.dump(posts, file, ensure_ascii=False)


def save_picture(picture) -> str:
    """
    Возвращает изображение если расширение файла соответствует
    """
    extension = picture.filename.split('.')[-1]
    if extension not in ['jpeg', 'png', 'gif', 'jpg']:
        raise InvalidExtension('Неверный формат файла')
    loaded_picture = f'{UPLOAD_FOLDER}/{picture.filename}'
    picture.save(loaded_picture)
    return loaded_picture
