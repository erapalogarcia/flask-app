from flask import Flask, request
from flask_restful import Resource,Api,reqparse

app= Flask(__name__)
api=Api(app)

items=[{"name":"Erick","precio":12.5}]
#Hereda todo lo que esta en la clase Resource
class Student(Resource):
    #se declara un metodo get
    def get(self,name):
        res={}
        for item in items:
           if(item['name']==name):
              res=item

        #esto es similar a usar un for
        #res=next(filter(lambda x: x['name']==name,items))
        return {"res":res},402


    def post(self,name):
        parse=reqparse.RequestParser()
        parse.add_argument('price',
        type=float,
        help='El precio no puede estar en blanco')
       
        #data=request.get_json()
        data=parse.parse_args()
        item={"name":name,"price":data['price']}
        items.append(item)
        return item,201

class ItemList(Resource):
    def get(self):
      return items

api.add_resource(Student,'/student/<string:name>')
api.add_resource(ItemList,'/items')

app.run(port=5000)
