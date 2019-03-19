import falcon
import json

from api.common.errors import InvalidParameterError

class TranslatorMiddleware:
    def process_request(self, request, response):
        if request.content_type == 'application/json':
            try:
                raw_json = request.stream.read()
            except Exception:
                raise Exception('Read Error')
            try:
                request.context['data'] = json.loads(raw_json.decode('utf-8'))
            except ValueError:
                raise InvalidParameterError('No JSON object could be decoded or Malformed JSON')
        else:
            request.context['data'] = None