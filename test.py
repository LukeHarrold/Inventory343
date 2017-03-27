from __init__ import app, db
import unittest
import json
import requests
import random

class apiTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    #Manufacturing api


    #/inventory/{numParts}/{partTypeId} --GET
    def test_send_parts_info(self):
        numParts = random.randint(1,3)
        partTypeId = random.randint(1,3)
        resp = self.app.get('/inventory/get-parts/{}/{}'.format(numParts, partTypeId))
        
        self.assertEqual(resp.status_code, 200)
        

    #/inventory/ --POST
    def test_recieve_completed_phones(self):
        resp = self.app.get('/inventory/mock')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.headers['ContentType'], 'application/json')
    
        '''
    def test_phone_order(self):
        test_json = {"status": "New", "screen": 866, "id": "ordermock", "keyboard": 389, "memory": 989, "model": "f"}
        resp = self.app.get('/inventory/phones/order', data=test_json)
        self.assertEqual(resp.status_code, 200)

    '''
    def test_send_broken_phone(self):
        test_json = '{"status": "New", "screen": 866, "id": "ordermock", "keyboard": 389, "memory": 989, "model": "f"}'
        resp = self.app.get('/inventory/send/{}'.format(test_json))
        self.assertEqual(resp.status_code, 200)

        '''
    def test_recieved_fixed_phone(self):
        test_json = '{"status": "New", "screen": 866, "id": "ordermock", "keyboard": 389, "memory": 989, "model": "f"}'
        resp = self.app.post('/inventory/{}/'.format(test_json))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.headers['ContentType'], 'application/json')
    '''

    def test_all_phone_models(self):
        resp = self.app.get('/inventory/models/all')
        self.assertEqual(resp.status_code, 200)

    def test_holding_sales_hand_through_indexing_lol(self):
        phoneModelId = random.randint(1,10)
        resp = self.app.get('/inventory/models/{}'.format(phoneModelId))
        self.assertEqual(resp.status_code, 200)

    def test_mark_as_return(self):
        phoneId = random.randint(1,10)
        resp = self.app.get('/inventory/phone/return/{}'.format(phoneId))
        self.assertEqual(resp.status_code, 200)

    def test_get_phone_by_id(self):
        phoneId = random.randint(1,10)
        resp = self.app.get('/inventory/phones/{}'.format(phoneId))
        self.assertEqual(resp.status_code, 200)
        
if __name__ == "__main__":
    unittest.main()