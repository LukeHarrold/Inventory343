from __init__ import app, db
import unittest
import requests

class apiTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    #Manufacturing api

    def test(self):
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.headers["Content-Type"], "text/html; charset=utf-8")

    #/inventory/{numParts}/{partTypeId} --GET
    def test_send_parts_info(self):
        resp = self.app.get('/')

        self.assertEqual(resp.status_code, 200)

    #/inventory/ --POST
    def test_recieve_completed_phones(self):
        
        pass

    #/inventory/send --POST
    def test_send_phone_to_be_refurbished(self):
        pass

    #/inventory/ --POST
    def test_recieve_refurbished_phone(self):
        pass


    #Sales api

    #/inventory/phones/order --POST
    def test_phone_orders(self):
        pass

    #/inventory/models/all --GET
    def test_get_all_models(self):
        pass

    #/inventory/models/{phoneModelId} --GET
    def test_get_specific_model(self):
        pass

    #/inventory/phone/return?phoneid={phoneId} --POST
    def test_mark_as_return(self):
        pass

    #/inventory/phones/{phoneId} --GET
    def test_get_phone(self):
        pass


if __name__ == "__main__":
    unittest.main()