from flask import request, jsonify, Blueprint
from marshmallow import ValidationError

from models import BatchRequestParams
from pickup import query_builder

main_bp = Blueprint('main_blueprint', __name__)


@main_bp.route("/perform_query", methods=['POST'])
def perform_query():
    # получаем ошибки

    data = request.json
    try:
        params = BatchRequestParams().load(data=data)
    except ValidationError as e:
        return jsonify(e.messages), 400

    # возвращаем пользователю сформированный результат
    result = None
    for query in params['queries']:
        result = query_builder(
            cmd=query['cmd'],
            value=query['value'],
            data=result,
        )
    return jsonify(result)
