import random
from locust import HttpUser, task


class SocialUser(HttpUser):
    # пример создания токена авторизации
    # он старт означает выполнение в самом начале
    def on_start(self) -> None:
        self.client.post('/authorization', json={'user': 'admin', 'password': 'qwerty'})
    @task(50)
    # пометили, что это основная функция для юзера
    def get_publication(self):
        post_id = random.randrange(1, 101)
        self.client.get(f'/posts/{post_id}')
    @task(10)
    # в скобках указали вес задачи
    def get_all_posts(self):
        self.client.get('/posts')
    @task(1)
    def create_post(self):
        data = {
            'title': 'qaaa',
            'body': 'no body',
            'userId': 1
        }
        self.client.post('/posts', json=data)
