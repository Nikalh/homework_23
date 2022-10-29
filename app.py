# from flask import request, jsonify, Blueprint, Response
# from marshmallow import ValidationError
#
# from models import BatchRequestParams
# from pickup import query_pickuper
#
# main_bp = Blueprint('main_blueprint', __name__)
#
#
# @main_bp.route("/perform_query", methods=['POST'])
# def perform_query() -> Response:
#     # получить на ошибки
#     try:
#         params = BatchRequestParams().load(data=request.json)
#     except ValidationError as e:
#         return jsonify(e.messages), 400
#
#     # вернозвращаем пользователю сформированный результат
#     result = None
#     for query in params['quereies']:
#         result = query_pickuper(
#             cmd=query['cmd'],
#             value=query['value'],
#             data=result,
#         )
#     return jsonify(result)
from flask import Flask

from view import main_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    return app
