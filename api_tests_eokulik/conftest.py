import pytest

from api_tests_eokulik.endpoints.get_posts import GetPosts
from api_tests_eokulik.endpoints.get_posts_id import GetPostsId
from api_tests_eokulik.endpoints.put_posts import PutPosts
from api_tests_eokulik.endpoints.post_post import PostPost
from api_tests_eokulik.endpoints.delete_post import DeletePost
from api_tests_eokulik.data import test_data


@pytest.fixture()
def publication_id(post_post_endpoint, delete_post_endpoint):
    post_post_endpoint.create_publication(test_data.DEFAULT_PAYLOAD)
    # pub_id = post_post_endpoint.response_json['id']  # = 101
    pub_id = 42
    yield pub_id
    delete_post_endpoint.delete_post(pub_id)


@pytest.fixture()
def get_posts_endpoint():
    return GetPosts()


@pytest.fixture()
def get_post_by_id_endpoint():
    return GetPostsId()


@pytest.fixture()
def put_pub_endpoint():
    return PutPosts()


@pytest.fixture()
def post_post_endpoint():
    return PostPost()


@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()
