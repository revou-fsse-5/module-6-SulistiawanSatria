import unittest
from zoo_management_api.app import app

class TestAnimalAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_animals(self):
        response = self.app.get('/api/animals')
        self.assertEqual(response.status_code, 200)

    def test_add_animal(self):
        animal_data = {
            "species": "Lion",
            "age": 5,
            "gender": "Male"
        }
        response = self.app.post('/api/animals', json=animal_data)
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
