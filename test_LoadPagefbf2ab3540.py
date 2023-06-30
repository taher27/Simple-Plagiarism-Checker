# Test generated by RoostGPT for test pythonPlagiarismCheck using AI Model gpt

import unittest
from flask import Flask, render_template
from your_flask_app import loadPage # assuming loadPage is in your_flask_app.py

class TestLoadPage(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_loadPagefbf2ab3540(self):
        with self.app.app_context():
            response = self.client.post('/') # assuming loadPage is mapped to '/'
            self.assertEqual(response.status_code, 200) # check if status code is 200
            self.assertIn(b'index.html', response.data) # check if 'index.html' is in the response

    def test_fail_loadPagefbf2ab3540(self):
        with self.app.app_context():
            response = self.client.post('/wrong_url') # wrong url
            self.assertEqual(response.status_code, 404) # check if status code is 404

if __name__ == '__main__':
    unittest.main()