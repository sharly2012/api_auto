import unittest
from util.BaseAPI import BaseAPI
from util.MySQL import DB

db = DB()
sql = 'SELECT id, username, email FROM users;'
array = db.execute_sql(sql)


class TestBaiDu(unittest.TestCase):

    def setUp(self):
        pass

    def test_baidu_1(self):
        base = BaseAPI()
        payload = {"username": array[0][0], "email": array[0][1]}
        result = base.test_api("/", payload)
        self.assertTrue(result.status_code == 200)

    def test_baidu_2(self):
        base = BaseAPI()
        payload = {"username": array[1][0], "email": array[1][1]}
        result = base.test_api("/", payload)
        self.assertTrue(result.status_code == 200)

    def test_baidu_3(self):
        base = BaseAPI()
        payload = {"username": array[2][0], "email": array[2][1]}
        result = base.test_api("/", payload)
        self.assertTrue(result.status_code == 200)

    def test_baidu_4(self):
        base = BaseAPI()
        payload = {"username": array[3][0], "email": array[3][1]}
        result = base.test_api("/", payload)
        self.assertTrue(result.status_code == 200)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
