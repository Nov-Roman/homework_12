from flask import Flask, send_from_directory
from loader.loader import loader_blueprint
from main.main import main_blueprint


app = Flask(__name__)

#  Регистрация блюпринта
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


# route для отдачи загруженных файлов
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == '__name__':
    app.run()
