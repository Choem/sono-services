import falcon
import json

try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict


class BaseResource(object):
    def to_json(self, body_dict):
        return json.dumps(body_dict)

    # TODO: AlchemnySQL object decoder

    def on_error(self, response, error=None):
        orderedDict = OrderedDict()
        orderedDict['code'] = error['code']
        orderedDict['message'] = error['message']

        response.status = error['status']
        response.body = self.to_json(orderedDict)

    def on_success(self, response, message=None, data=None):
        orderedDict = OrderedDict()
        orderedDict['data'] = data
        orderedDict['code'] = 200
        orderedDict['message'] = message or 'OK'

        response.status = falcon.HTTP_200
        response.body = self.to_json(orderedDict)