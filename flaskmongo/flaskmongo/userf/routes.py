from flask import Blueprint,render_template,Response,request,jsonify
from flaskmongo.models import User
userf=Blueprint('userf',__name__)

@userf.route('/')
def abc():
    return 'hello'


@userf.route('/user',methods=['GET'])
def home():
    u=User.objects.all()
    if not u:
        return jsonify({'message':f'user not found'}),404
    return jsonify(u)

@userf.route('/user/<id>',methods=['GET'])
def getuser(id):
    try: 
        id=int(id)
    except:
        return jsonify({'message':f'id {id} is invalid'}),400
    u=User.objects(uid=id).first()
    if not u:
        return jsonify({'message':f'id {id} not found'}),404
    return jsonify(u)
    


@userf.route('/user',methods=['POST'])
def create_user():
    if request.method=='POST':
        data=request.get_json()
        id=data['id']
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

@userf.route('/user/<id>',methods=['PUT'])
def update_user(id):
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

@userf.route('/user/<id>',methods=['DELETE'])
def delete_user(id):
    try: 
        id=int(id)
    except:
        return jsonify({'message':f'id {id} is invalid'}),400
    u=User.objects(uid=id).first()
    if not u:
        return jsonify({'message':f'id {id} not found'}),404
    u.delete()
    return jsonify({'message':'delete successfuly'}),204


