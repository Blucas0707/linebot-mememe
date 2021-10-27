from .schema import responseSchema
from .type import ErrorMessage, StatusCode
from flask import Response as flaskResponse
import json
class response:
    def __init__(self):
        pass
    def writeErrorResponse(data, err):
        responseSchema["ResponseStatusCode"] = StatusCode[err]
        responseSchema["Message"] = ErrorMessage[err]
        responseSchema["Data"] = None
        resp = json.dumps(responseSchema, indent=4, ensure_ascii=False)
        return flaskResponse(resp, status = StatusCode[err], mimetype='application/json')

    def writeSuccessResponse(data, statuscode):
        responseSchema["ResponseStatusCode"] = statuscode
        responseSchema["Message"] = "Success"
        responseSchema["Data"] = data
        resp = json.dumps(responseSchema, indent=4, ensure_ascii=False)
        return flaskResponse(resp, status = statuscode, mimetype='application/json')
        
    def writeDataResponse(data, statuscode):
        responseSchema["ResponseStatusCode"] = statuscode
        responseSchema["Message"] = "Success"
        responseSchema["Data"] = data
        resp = json.dumps(responseSchema, indent=4, ensure_ascii=False)
        return flaskResponse(resp, status = statuscode, mimetype='application/json')