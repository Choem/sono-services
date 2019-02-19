# Router class that helps us register routes
class Router:
    @staticmethod
    def register_routes(routes, app):
        for module in routes:
            for route in module:
                app.add_route(route[0], route[1])