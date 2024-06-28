from flask import Flask, jsonify, render_template
from  database.database_connection import  fetch_data
import mysql.connector

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_to_api():
    return render_template('index.html')

@app.route("/history", methods=["GET"])
def history():
    try:
        query = "SELECT user.first_name,user.last_name,user.user_id,appointments.appointment_id,appointments.appointment_status FROM user, appointments"

        myresult = fetch_data(query)
        result_list = [
            {
                "first_name": row[0],
                "last_name": row[1],
                "user_id": row[2],
                "appointment_id": str(row[3]),
                "apppointment_status": str(row[4]),
                # "host_id":str(row[5])
        
               
            } for row in myresult
        ]
        return jsonify(result_list)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

@app.route("/discarded_appointment", methods=["GET"])
def discarded_list():
    try:
        query = "SELECT first_name, last_name, appointment_id, start_ti, appointment_status, host_id FROM practice WHERE appointment_status = 'rejected'"
        myresult = fetch_data(query)
        result_list = [
            {
                "first_name": row[0],
                "last_name": row[1],
                "appointment_number": row[2],
                "start_time": str(row[3]),
                "end_time": str(row[4]),
                "appointment_status": row[5],
                "host_id": row[6]
            } for row in myresult
        ]
        return jsonify(result_list)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

@app.route("/current_appointment", methods=["GET"])
def approved_list():
    try:
        query = "SELECT first_name, last_name, appointment_number, start_time, end_time, appointment_status, host_id FROM practice WHERE first_name = 'ankit'"
        myresult = fetch_data(query)
        result_list = [
            {
                "first_name": row[0],
                "last_name": row[1],
                "appointment_number": row[2],
                "start_time": str(row[3]),
                "end_time": str(row[4]),
                "appointment_status": row[5],
                "host_id": row[6]
            } for row in myresult
        ]
        return jsonify(result_list)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
@app.route("/time_slots", methods=["GET"])
def time_slots():
    try:
        query = "SELECT time_slot FROM timeslots"
        myresult = fetch_data(query)
        result_list = [{"timeslots": row[0]} for row in myresult]
        return jsonify(result_list)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

@app.route("/slots_completed_field", methods=["POST", "GET"])
def slots_completed():
    try:
        query = "SELECT timeslot FROM timeslots"
        myresult = fetch_data(query)
        all_slots_booked = all(slot[0] == 'booked' for slot in myresult)
        message = {
            "status": "success",
            "message": "ALL_SLOTS_BOOKED" if all_slots_booked else "NOT_ALL_SLOTS_BOOKED"
        }
        return jsonify(message)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

if __name__ == "__main__":
    app.run(debug=True)