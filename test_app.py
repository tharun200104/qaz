import unittest
import threading
from urllib.request import urlopen
from app import Handler, HTTPServer


class TestApplication(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 8081), Handler)
        cls.thread = threading.Thread(
            target=cls.server.serve_forever,
            daemon=True
        )
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def test_health_endpoint(self):
        response = urlopen("http://127.0.0.1:8081/health")

        self.assertEqual(response.status, 200)
        self.assertEqual(response.read(), b"OK")


if __name__ == "__main__":
    unittest.main()
