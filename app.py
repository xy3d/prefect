from flask import Flask, request, jsonify
from prefect import flow, task
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://xy3d:XgB8JVGTuWGd50kp@cluster0.20iimjx.mongodb.net/")
db = client["emp"]
collection = db["salary"]

@flow
@app.route('/emp', methods=['GET', 'POST'])
def employees():
    if request.method == 'GET':
        employees_list = list(collection.find({}, {"_id": 0}))
        return jsonify(employees_list)

    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        salary = data.get('salary')

        if name and salary:
            new_employee = {'name': name, 'salary': salary}
            collection.insert_one(new_employee)
            return jsonify({'message': 'Employee added successfully!'}), 201
        else:
            return jsonify({'message': 'Name and salary must be provided.'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)