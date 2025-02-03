from flask import Blueprint, render_template, request, redirect
from services.medication_service import get_all_medications, add_new_medication, update_medication_by_id
from models.medication_model import fetch_medication_by_id
from utils.time_formatter import format_time_input

# Define the Blueprint
medication_bp = Blueprint("medication", __name__)

@medication_bp.route("/")
def index():
    medications = get_all_medications()
    return render_template("homepage.html", medications=medications)


@medication_bp.route("/add", methods=["GET", "POST"])
def add_medication():
    if request.method == "POST":
        medication_info = {
            "Username": request.form["Username"],
            "name": request.form["name"],
            "dose": request.form["dose"],
            "frequency": request.form["frequency"],
            "time": request.form["time"]
        }

        # Format time and handle errors
        formatted_time = format_time_input(medication_info["time"])
        if not formatted_time:
            return "Invalid time format. Please enter time in 'HH:MM' format."

        medication_info["time"] = formatted_time
        add_new_medication(medication_info)
        return redirect("/")
    return render_template("add_medication.html")


@medication_bp.route("/edit/<int:medicine_id>", methods=["GET", "POST"])
def edit_medications(medicine_id):
    if request.method == "GET":
        medication = fetch_medication_by_id(medicine_id)
        if not medication:
            return "Medication not found", 404
        return render_template("edit_medication.html", post=medication)

    if request.method == "POST":
        medication_info = {
            "Username": request.form["Username"],
            "name": request.form["name"],
            "dose": request.form["dose"],
            "frequency": request.form["frequency"],
            "time": format_time_input(request.form["time"]),
        }

        update_medication_by_id(medicine_id, medication_info)
        return redirect("/")
