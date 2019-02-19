import json
import falcon

class UserResource(object):
    def on_get(self, request, response):
        data = [
            { 'id': 1, 'name': 'Chiem Janssen' },
            { 'id': 2, 'name': 'Uncle Robdog' }
        ]

        response.body = json.dumps(data, ensure_ascii=False)
        response.status = falcon.HTTP_200