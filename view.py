from flask import request, jsonify, Blueprint, Response
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest

from models import RequestParams, BatchRequestParams  # BatchRequestParams
from pickup import query_builder

main_bp = Blueprint('main_blueprint', __name__)


@main_bp.route("/perform_query", methods=['POST'])
def perform_query():
    # получить на ошибки

    data = request.json
    try:
        params = BatchRequestParams().load(data=data)
    except ValidationError as e:
        return jsonify(e.messages), 400

    #веозвращаем пользователю сформированный результат
    result = None
    for query in params['queries']:
        result = query_builder(
            cmd=query['cmd'],
            value=query['value'],
            data=result,
        )
    return jsonify(result)
    #return jsonify(query_builder(params, None))