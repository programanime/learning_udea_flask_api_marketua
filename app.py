from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask import request
from os import environ
from controller import ProductController
from controller import BrandController
from controller import CategoryController
from controller import CarController
from controller import CheckoutController
import sys


app = Flask(__name__)

# cors = CORS(app,  origins=['http://localhost:8080'])
cors = CORS(app)
api = Api(app)
idToken="123"
from flask import jsonify
from flask_restful import Resource,reqparse

parser = reqparse.RequestParser()

@api.resource('/categories')
class CategoriesPrev(Resource):
    def get(self):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        return jsonify({"status":"OK", "data":CategoryController.get_all()})

@api.resource('/categories/')
class Categories(Resource):
    def get(self):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        return jsonify({"status":"OK", "data":CategoryController.get_all()})

@api.resource('/brands')
class BrandsPrev(Resource):
    def get(self):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        return jsonify({"brands":BrandController.get_all()})

@api.resource('/brands/')
class Brands(Resource):
    def get(self):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        return jsonify({"brands":BrandController.get_all()})

@api.resource('/items/category/<category_name>')
class ProductsByCategoryPrev(Resource):
    def get(self,  category_name:str):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        return jsonify({"products":ProductController.get_by_category(category_name)})
        
        # return jsonify({"products":listaItems})
        

@api.resource('/items/category/<category_name>/')
class ProductsByCategory(Resource):
    def get(self,  category_name:str):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        return jsonify({"products":ProductController.get_by_category(category_name)})
        
        # return jsonify({"products":listaItems})

@api.resource('/items/brand/<brand_name>')
class ProductsByBrandPrev(Resource):
    def get(self, brand_name:str):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        items=ProductController.get_by_brand(brand_name)
        return jsonify({"products":items})

@api.resource('/items/brand/<brand_name>/')
class ProductsByBrand(Resource):
    def get(self, brand_name:str):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        items=ProductController.get_by_brand(brand_name)
        return jsonify({"products":items})

@api.resource('/items/<item_id>')
class ProductPrev(Resource):
    def get(self, item_id):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        item = ProductController.get(str(item_id))
        return jsonify(item)        

@api.resource('/items/<item_id>/')
class Product(Resource):
    def get(self, item_id):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        item = ProductController.get(str(item_id))
        return jsonify(item)


@api.resource('/search')
class ProductsPrev(Resource):
    def get(self):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        nombre = request.args.get('q')
        return jsonify({"products":ProductController.get_by_name(nombre)})

@api.resource('/search/')
class Products(Resource):
    def get(self):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        nombre = request.args.get('q')
        return jsonify({"products":ProductController.get_by_name(nombre)})

@api.resource('/checkout')
class CheckoutsPrev(Resource):
    def post(self):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        CheckoutController.save(request.json)
        return jsonify({"ok":True})

@api.resource('/checkout/')
class Checkouts(Resource):
    def post(self):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        CheckoutController.save(request.json)
        return jsonify({"ok":True})

@api.resource('/save-cart')
class CarsPrev(Resource):
    def post(self):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        CarController.save(request.json)
        return jsonify({"ok":True})


@api.resource('/save-cart/')
class Cars(Resource):
    def post(self):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        CarController.save(request.json)
        return jsonify({"ok":True})
        

@api.resource('/user/<user_name>/orders')
class OrderPrev(Resource):
    def get(self, user_name:str):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        items=CheckoutController.get_by_user(user_name)
        return jsonify({"orders":items})

@api.resource('/user/<user_name>/orders/')
class Order(Resource):
    def get(self, user_name:str):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        items=CheckoutController.get_by_user(user_name)
        return jsonify({"orders":items})

@api.resource('/orders/<user_name>')
class OrderUsersPrev(Resource):
    def get(self, user_name:str):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        items=CheckoutController.get_by_user(user_name)
        return jsonify({"status":"OK","orders":items})

@api.resource('/orders/<user_name>/')
class OrderUsers(Resource):
    def get(self, user_name:str):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        items=CheckoutController.get_by_user(user_name)
        return jsonify({"status":"OK","orders":items})
        

@api.resource('/share-cart/<user_name>')
class CarsUserPrev(Resource):
    def get(self, user_name:str):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        items=CarController.get_by_user(user_name)
        return jsonify({"status":"OK","cart":items})

@api.resource('/share-cart/<user_name>/')
class CarsUser(Resource):
    def get(self, user_name:str):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        items=CarController.get_by_user(user_name)
        return jsonify({"status":"OK","cart":items})

@api.resource('/orders/<user_name>')
class OrderUsersSlashPrev(Resource):
    def get(self, user_name:str):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        items=CheckoutController.get_by_user(user_name)
        return jsonify({"status":"OK", "orders":items})

@api.resource('/orders/<user_name>/')
class OrderUsersSlash(Resource):
    def get(self, user_name:str):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        items=CheckoutController.get_by_user(user_name)
        return jsonify({"status":"OK", "orders":items})


        # nombre = request.args.get('q')
        # return jsonify({"products":ProductController.get_by_name(nombre)})

@api.resource("/")
class AllProducts(Resource):
    def get(self):
        if request.headers.get('idToken') and  request.headers.get('idToken') != idToken:return jsonify({"result":"Token no valido", "ok":False})
        items = ProductController.get_all()
        return jsonify(items)

app.run(host= '0.0.0.0', port=environ.get('PORT'))
