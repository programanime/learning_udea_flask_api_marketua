# Api marketua Flask :

## Para iniciar la API ejecute
##### pip install -r requirements.txt
##### python app.py

## para correr las pruebas unitarias ejecute
##### python -m unittest test_controller.py

## Las URLs son:

## Lista de categorías:
https://marketuaflask.herokuapp.com/categories

## Búsqueda por nombre
https://marketuaflask.herokuapp.com/search?q={param}

### Ejemplo
https://marketuaflask.herokuapp.com/search?q=portatil

## Búsqueda por categoría
https://marketuaflask.herokuapp.com/items/category/{categoryName}

### Ejemplo
https://marketuaflask.herokuapp.com/items/category/cellphone

## Marcas existentes
https://marketuaflask.herokuapp.com/brands

## Búsqueda por marca
https://marketuaflask.herokuapp.com/items/brand/{brandName}

### Ejemplo
https://marketuaflask.herokuapp.com/items/brand/ASUS

## Detalles de un producto
https://marketuaflask.herokuapp.com/items/{item_id}

### Ejemplo
https://marketuaflask.herokuapp.com/items/4 


