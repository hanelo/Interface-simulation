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

        if num_passengers <= 0 or processing_time_per_passenger <= 0 or num_resources <= 0 :
            return render_template("interface.html", error="Veuillez saisir des valeurs valides pour les paramètres.")

        # Calculate time per resource (time cycle)
        time_per_resource = processing_time_per_passenger / num_resources

        # Calculate the waiting time for the passenger (first in queue has no waiting time)
        waiting_time = 0  # Updated for the first passenger

        # Calculate the processing time for the passenger (from the form input)
        processing_time = processing_time_per_passenger

        # Calculate the total time (waiting time + processing time)
        total_time = waiting_time + processing_time

        # Calculate the processing time for the first passenger (no waiting time)
        first_passenger_processing_time = processing_time_per_passenger  # Updated for the first passenger


        # Additional calculations for the chosen position
        chosen_position = int(request.form['chosen_position'])
        chosen_position_waiting_time = 0

        if chosen_position == 1:
            chosen_position_waiting_time = 0
        else:
            chosen_position_waiting_time = (processing_time_per_passenger / num_passengers) * (chosen_position - 1)

        chosen_position_processing_time = processing_time_per_passenger
        chosen_position_total_time = chosen_position_waiting_time + chosen_position_processing_time
         # Calculate the total time (waiting time + processing time)
        total_time_last_passenger =  (num_passengers*processing_time)/num_resources
        # Calculate the waiting time for the passenger (last in queue )
        last_passenger_waiting_time = total_time_last_passenger-processing_time
        # Calculate the waiting time for the passenger in the middle
        passenger_middle_waiting_time = last_passenger_waiting_time/2
        # Calculate the total time (waiting time + processing time)
        total_time_middle_passenger = passenger_middle_waiting_time  + processing_time
        # Calculate the waiting time for the passenger (chosen position in queue )
        passenger_chosenposition_waiting_time = (processing_time_per_passenger / num_resources) * (chosen_position - 1)
        passenger_chosenposition_total_time =  passenger_chosenposition_waiting_time + processing_time
        # Calculate capacity
        capacity = (num_resources *60)/(processing_time)



        return render_template("Result.html", results=True,
                               waiting_time=waiting_time,
                               processing_time=processing_time,
                               total_time=total_time,
                               first_passenger_processing_time=first_passenger_processing_time,
                               chosen_position_waiting_time=chosen_position_waiting_time,
                               chosen_position_processing_time=chosen_position_processing_time,
                               chosen_position_total_time=chosen_position_total_time,
                               last_passenger_waiting_time=last_passenger_waiting_time,
                               total_time_last_passenger=total_time_last_passenger,
                               passenger_middle_waiting_time=passenger_middle_waiting_time,
                               total_time_middle_passenger=total_time_middle_passenger,
                               passenger_chosenposition_waiting_time=passenger_chosenposition_waiting_time,
                               passenger_chosenposition_total_time=passenger_chosenposition_total_time,
                               capacity=capacity
                               )

    except ValueError:
        return render_template("interface.html", error="Veuillez saisir des valeurs numériques valides pour les paramètres.")

if __name__ == "__main__":
    app.run(debug=True)
