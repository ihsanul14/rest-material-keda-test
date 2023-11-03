from odoo.tests.common import TransactionCase

class TestMaterialController(TransactionCase):
    def test_get_material(self):
        response = self.url_open('/api/material')
        self.assertEqual(response.status_code, 200)
    
    def test_create_material(self):
        payload = {
            "code": "M01",
            "name": "Jeans 1",
            "type": "jeans",
            "buy_price": 100,
            "related_supplier": "supplier 1"
        }
        response = self.url_post('/api/material', json=payload)
        self.assertEqual(response.status_code, 200) 
    
    def test_update_material(self):
        payload = {
            "name": "Jeans 1",
            "type": "jeans",
            "buy_price": 100,
            "related_supplier": "supplier 1"
        }
        response = self.url_put('/api/material/M01', json=payload)
        self.assertEqual(response.status_code, 200) 
    
    def test_delete_material(self):
        response = self.url_delete('/api/material/M01')
        self.assertEqual(response.status_code, 200) 