class Middleware:
    def __init__(self):
        self.logs = []

    def handle_request(self, request):
        self.logs.append(request)
        return f"Request {request} received and logged."
    
middleware = Middleware()
print(middleware.handle_request("GET /home"))
print(middleware.handle_request("POST /data"))
print(middleware.logs)