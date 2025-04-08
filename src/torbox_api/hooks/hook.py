import logging

logging.basicConfig(level=logging.INFO)


class Request:
    def __init__(self, method, url, headers, body=""):
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body

    def __str__(self):
        return f"Request(method={self.method}, url={self.url}, headers={self.headers}, body={self.body})"


class Response:
    def __init__(self, status, headers, body):
        self.status = status
        self.headers = headers
        self.body = body

    def __str__(self):
        return (
            f"Response(status={self.status}, headers={self.headers}, body={self.body})"
        )


class CustomHook:

    def before_request(self, request: Request, **kwargs):
        logging.debug("before_request")
        logging.debug(request)

    def after_response(self, request: Request, response: Response, **kwargs):
        logging.debug("after_response")
        logging.debug(response)

    def on_error(
        self, error: Exception, request: Request, response: Response, **kwargs
    ):
        logging.debug("on_error")
        logging.error(f"Error: {error}")
        logging.debug(request)
        logging.debug(response)
