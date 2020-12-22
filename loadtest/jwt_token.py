from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    #def on_start(self):
    #    self.client.post("/login", {
    #        "username": "bob",
    #        "password": "tables123"
    #    })
    
    @task
    def get_jwt_token(self):
        self.client.post("/api/token/", {
            "username": "bob",
            "password": "tables123"
        })
