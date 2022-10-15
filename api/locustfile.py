from locust import HttpUser, between, task


class APIUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def assistance_list(self):
        self.client.get("api/assistance/")

    @task(2)
    def assistance_detail(self):
        self.client.get("api/assistance/1/")
