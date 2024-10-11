import random

from locust import HttpUser, task


class SocialUser(HttpUser):
    token: str

    @staticmethod
    def help_func():
        return 42

    def on_start(self):
        # token = self.client.post('/authorization', json={'user': 'admin', 'password': 'uweyrwe'})
        self.token = 'iweriuwyero'

    @task(50)
    def get_publication(self):
        headers = {'Authorization': self.token}
        post_id = random.randrange(1, 102)
        self.client.get(f'/posts/{post_id}', headers=headers)

    @task(10)
    def get_all_posts(self):
        headers = {'Authorization': self.token}
        self.client.get('/posts', headers=headers)

    @task(1)
    def create_a_post(self):
        headers = {'Authorization': self.token}
        data = {
            'title': 'foo',
            'body': 'bar',
            'userId': 1,
        }
        self.client.post('/posts', json=data, headers=headers)
