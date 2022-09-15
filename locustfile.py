from locust import HttpUser, task


class LoadTesting(HttpUser):
    @task
    def status_test(self):
        self.client.get("/")
    
    @task
    def blip_test(self):
        self.client.get("/blip")
