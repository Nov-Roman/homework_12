from flask import Blueprint, render_template, request
import logging
from functions import load_json, search_post_string
from config import POST_PATH
from exceptions import DataJsonError

main_blueprint = Blueprint('main_blueprint', __name__, template_folder="templates")
logging.basicConfig(filename='logs.log', level=logging.INFO)


#  route для вывода главной страницы
@main_blueprint.route('/')
def main_page():
    logging.info('Загрузка главной страницы')
    return render_template('index.html')


# route для вывода, найденных постов
@main_blueprint.route('/search')
def search_page():
    s = request.args.get('s')
    logging.info('Поиск')
    try:
        posts = load_json(POST_PATH)
    except DataJsonError:
        return 'Ошибка загрузки файла json'
    found = search_post_string(posts, s)
    return render_template('post_list.html', posts=found, s=s)
