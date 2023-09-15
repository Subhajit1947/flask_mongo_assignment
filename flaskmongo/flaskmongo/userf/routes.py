from flask import Blueprint,render_template,Response,request,jsonify
from flaskmongo.models import User
from flask.views import MethodView

userf=Blueprint('userf',__name__)

class Userroute(MethodView):
    def get(self,id=None):
        if id is not None:
            try: 
                id=int(id)
            except:
                return jsonify({'message':f'id {id} is invalid'}),400
            u=User.objects(uid=id).first()
            if not u:
                return jsonify({'message':f'id {id} not found'}),404
            return jsonify(u)
        u1=User.objects.all()
        if not u1:
            return jsonify({'message':f'user not found'}),404
        return jsonify(u1)
  
    def post(self):
        if request.method=='POST':
            data=request.get_json()
            id=int(data['id'])
            name=data['name']
            email=data['email']
            password=data['password']
            if id and name and email and password:
                u=User.objects(uid=id).first()
                if u:
                    return Response('user already exist')
                nu=User(uid=id,name=name,email=email,password=password)
                nu.save()
                return jsonify(nu),201

    def put(self,id):
        try: 
            id=int(id)
        except:
            return jsonify({'message':f'id {id} is invalid'}),400
        u=User.objects(uid=id).first()
        if not u:
            return jsonify({'message':f'id {id} not found'}),404
        data=request.get_json()
        uid=data['id']
        name=data['name']
        email=data['email']
        password=data['password']
        u.update(uid=uid,name=name,email=email,password=password)
        return jsonify({'message':'update successfuly'})

    def delete(self,id):
        try: 
            id=int(id)
        except:
            return jsonify({'message':f'id {id} is invalid'}),400
        u=User.objects(uid=id).first()
        if not u:
            return jsonify({'message':f'id {id} not found'}),404
        u.delete()
        return jsonify({'message':'delete successfuly'}),204
    


userf.add_url_rule('/user',view_func=Userroute.as_view('usercl'), methods=['GET', 'POST'])
userf.add_url_rule('/user/<int:id>', view_func=Userroute.as_view('userpu'), methods=['GET', 'PUT', 'DELETE'])


