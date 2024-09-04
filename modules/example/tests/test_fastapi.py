import unittest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from database import get_db
from main import app
from ..models import Item

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_example_route(self):
        response = self.client.get('/example')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'This is an example module')

    def test_example_item(self, db: Session = next(get_db())):
        item = db.query(Item).filter_by(id=69).first()
        if not item:
            item = Item(id=69, name='Name', description='Description')
            db.add(item)
            db.commit()

        response = self.client.get('/example/item/69')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'id': item.id, 'name': item.name, 'description': item.description})

    def test_example_item__no_items(self, db: Session = next(get_db())):
        item = db.query(Item).filter_by(id=69).first()
        if item:
            db.delete(item)
            db.commit()

        response = self.client.get('/example/item/69')
        self.assertEqual(response.status_code, 404)

        if item:
            item = Item(id=item.id, name=item.name, description=item.description)
            db.add(item)
            db.commit()
