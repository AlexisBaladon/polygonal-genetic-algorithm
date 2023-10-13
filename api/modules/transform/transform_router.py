from flask import Blueprint, request

from api.modules.transform import transform_controller

transform_blueprint = Blueprint("transform", __name__)

@transform_blueprint.route("", methods=['POST'])
def transformed_image():
    return transform_controller.transform(request)