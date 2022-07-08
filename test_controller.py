import unittest
from controller import ProductController
from controller import BrandController
from controller import CategoryController

class TestProductController(unittest.TestCase):
    def test_get_all(self):
        result = ProductController.get_all()
        self.assertTrue(len(result)>0)

    def test_get(self):
        result = ProductController.get("5")
        self.assertTrue(result!=None)

    def test_get_by_category(self):
        result = ProductController.get_by_category("cellphone")
        self.assertTrue(len(result)>0)
    
    def test_get_by_brand(self):
        result = ProductController.get_by_brand("asus")
        self.assertTrue(len(result)>0)
    
    def test_get_by_name(self):
        result = ProductController.get_by_name("xiaomi")
        self.assertTrue(len(result)>0)

class TestCategoryController(unittest.TestCase):
    def test_get_all(self):
        result = CategoryController.get_all()
        self.assertTrue(len(result)>0)

class TestBrandController(unittest.TestCase):
    def test_get_all(self):
        result = BrandController.get_all()
        self.assertTrue(len(result)>0)


class TestCartController(unittest.TestCase):
    def test_get_all(self):
        result = CarController.get_all()
        self.assertTrue(len(result)>0)
        