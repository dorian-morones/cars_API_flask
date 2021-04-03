from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
print("================DEV================", app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)



@app.route('/')
def hello():
	return {"hello": "world"}


@app.route('/cars', methods=['POST', 'GET'])
def handle_cars():
    from Models.car_models import Cars

    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_car = Cars(
                title=data['title'], 
                model=data['model'], 
                doors=data['doors'],
                make=data['make'], 
                year=data['year'], 
                price=data['price'],
                mileage=data['mileage']
                )

            db.session.add(new_car)
            db.session.commit()

            return {"message": f"car {new_car.title} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        cars = Cars.query.all()
        results = [
            {
                "title": car.title,
                "make": car.make,
                "model": car.model,
                "price": car.price,
            } for car in cars]

        return {"count": len(results), "cars": results, "message": "success"}


@app.route('/cars/<car_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_car(car_id):
    from Models.car_models import Cars

    car = Cars.query.get_or_404(car_id)

    if request.method == 'GET':
        response = {
            "title": car.title,
            "make": car.make,
            "model": car.model,
            "doors": car.doors,
            "price": car.price,
            "year": car.year,
            "mileage": car.mileage
        }
        return {"message": "success", "car": response}

    elif request.method == 'PUT':
        data = request.get_json()
        car.title = data['title']
        car.make = data['make']
        car.model = data['model']
        car.year = data['year']
        car.price = data['price']
        car.doors = data['doors']
        car.mileage = data['mileage']

        db.session.add(car)
        db.session.commit()
        
        return {"message": f"car {car.title} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(car)
        db.session.commit()
        
        return {"message": f"Car {car.title} successfully deleted."}


if __name__ == '__main__':
    app.run(debug=True)