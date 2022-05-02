from flask import Blueprint, render_template, request
import logging
from exceptions import InvalidExtension
from functions import load_json, save_new_post, save_picture
from config import POST_PATH

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder="templates")
logging.basicConfig(filename='logs.log', level=logging.INFO)


# route для вывода страницы создания нового поста
@loader_blueprint.route('/post', methods=['GET'])
def new_post_page():
    logging.info("Запуск страницы создания нового поста")
    return render_template('post_form.html')


# route для вывода загруженного поста
@loader_blueprint.route('/post', methods=['POST'])
def create_new_post_page():
    picture = request.files.get('picture')
    content = request.form.get('content')
    if not picture or not content:
        logging.info("Отсутствуют данные")
        return 'Отсутствуют данные'
    posts = load_json(POST_PATH)

    try:
        post_created = {'pic': save_picture(picture), 'content': content}
    except InvalidExtension:
        return 'Неверный формат файла'

    posts.append(post_created)

    save_new_post(POST_PATH, posts)
    return render_template('post_uploaded.html', post_created=post_created)
