
import unittest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

class TestAPI(unittest.TestCase):
    def test_get_posts(self):
        response = requests.get(f"{BASE_URL}/posts")
        self.assertEqual(response.status_code, 200, "GET /posts failed")
        self.assertIsInstance(response.json(), list, "Response is not a list")

    def test_create_post(self):
        payload = {"title": "foo", "body": "bar", "userId": 1}
        response = requests.post(f"{BASE_URL}/posts", json=payload)
        self.assertEqual(response.status_code, 201, "POST /posts failed")
        data = response.json()
        self.assertEqual(data["title"], payload["title"], "Title mismatch")
        self.assertEqual(data["body"], payload["body"], "Body mismatch")
        self.assertEqual(data["userId"], payload["userId"], "User ID mismatch")

    def test_update_post(self):
        post_id = 1
        payload = {"title": "updated title", "body": "updated body", "userId": 1}
        response = requests.put(f"{BASE_URL}/posts/{post_id}", json=payload)
        self.assertEqual(response.status_code, 200, "PUT /posts/{id} failed")
        data = response.json()
        self.assertEqual(data["title"], payload["title"], "Title mismatch")
        self.assertEqual(data["body"], payload["body"], "Body mismatch")

    def test_delete_post(self):
        post_id = 1
        response = requests.delete(f"{BASE_URL}/posts/{post_id}")
        self.assertEqual(response.status_code, 200, "DELETE /posts/{id} failed")

if __name__ == "__main__":
    unittest.main()
