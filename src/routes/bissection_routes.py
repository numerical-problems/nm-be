from flask_restx import Resource
from flask import request
from src.utils.dto import BissectionDto
from src.controllers.bissection_controller import BissectionController


api = BissectionDto.api
_body_bissection = BissectionDto.body


@api.route('/', strict_slashes=False)
class Bissection(Resource, BissectionController):
    def post(self):
        return self.bissection_expression(body=request.json)
