from flask import Flask, render_template, request
import random
import math

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("interface.html")

@app.route("/simulate", methods=["POST"])
def simulate():
    try:
        num_passengers = int(request.form['passengers'])
        processing_time_per_passenger = float(request.form['processing_time'])
        num_resources = int(request.form['num_resources'])

        if num_passengers <= 0 or processing_time_per_passenger <= 0 or num_resources <= 0:
            return render_template("interface.html", error="Veuillez saisir des valeurs valides pour les paramètres.")

        # Calculate time per resource (time cycle)
        time_per_resource = processing_time_per_passenger / num_resources

        # Get the position of the passenger in the queue
        queue_position = int(request.form['queue_position'])

        # Calculate the waiting time for the passenger (first in queue has no waiting time)
        waiting_time = max(0, (queue_position - 1) * time_per_resource)

        # Calculate the processing time for the passenger
        processing_time = random.expovariate(1 / processing_time_per_passenger)

        # Calculate the total time (waiting time + processing time)
        total_time = waiting_time + processing_time

        # Calculate the processing time for the first passenger (no waiting time)
        first_passenger_processing_time = random.expovariate(1 / time_per_resource)

        # Calculate the processing time for the last passenger (total number of passengers * time per resource)
        last_passenger_processing_time = num_passengers * time_per_resource
        # Calculate the position of the person in the middle of the queue
        middle_position = math.ceil(num_passengers / 2)

        # Calculate the waiting time for the person in the middle of the queue
        middle_waiting_time = max(0, (middle_position - 1) * time_per_resource)

        # Calculate the processing time for the person in the middle of the queue
        middle_processing_time = random.expovariate(1 / processing_time_per_passenger)

        # Calculate the total time for the person in the middle of the queue
        middle_total_time = middle_waiting_time + middle_processing_time

        return render_template("Result.html", results=True, 
                               waiting_time=waiting_time, 
                               processing_time=processing_time, 
                               total_time=total_time, 
                               first_passenger_processing_time=first_passenger_processing_time,
                               last_passenger_processing_time=last_passenger_processing_time,
                               middle_waiting_time=middle_waiting_time,
                               middle_processing_time=middle_processing_time,
                               middle_total_time=middle_total_time)


    except ValueError:
        return render_template("interface.html", error="Veuillez saisir des valeurs numériques valides pour les paramètres.")

if __name__ == "__main__":
    app.run(debug=True)
