import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from emoji import emojize


# Function to get location details
def get_location_details():
    location_name = location_entry.get()

    if not location_name.strip():
        messagebox.showerror("Error", "Please enter a valid location!")
        return

    try:
        # Initialize geolocator
        geolocator = Nominatim(user_agent="location_finder")

        # Get location details
        location = geolocator.geocode(location_name, addressdetails=True)

        if location:
            result_text = (
                f"{emojize(':round_pushpin:')} *Details for*: {location_name}\n\n"
                f"{emojize(':world_map:')} Address: {location.address}\n"
                f"{emojize(':compass:')} Latitude: {location.latitude}\n"
                f"{emojize(':compass:')} Longitude: {location.longitude}\n"
            )

            if location.raw.get("address"):
                address_details = location.raw["address"]
                city = address_details.get("city", "N/A")
                state = address_details.get("state", "N/A")
                country = address_details.get("country", "N/A")
                result_text += (
                    f"{emojize(':cityscape:')} City: {city}\n"
                    f"{emojize(':mountain:')} State: {state}\n"
                    f"{emojize(':globe_with_meridians:')} Country: {country}\n"
                )

            result_label.config(text=result_text, justify="left")
        else:
            messagebox.showinfo("Not Found", "No location found for the given name.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")


# Create the main window
app = tk.Tk()
app.title("Location Finder 🌍")
app.geometry("500x500")
app.resizable(False, False)

# Add a title label
title_label = tk.Label(
    app, text="🌍 Location Finder", font=("Arial", 20, "bold"), fg="green"
)
title_label.pack(pady=10)

# Add an entry for the location
location_entry = tk.Entry(app, font=("Arial", 14), width=30)
location_entry.pack(pady=10)
location_entry.insert(0, "Enter a location here...")

# Add a button to search
search_button = tk.Button(
    app,
    text="🔍 Find Location",
    font=("Arial", 14, "bold"),
    bg="blue",
    fg="white",
    command=get_location_details,
)
search_button.pack(pady=10)

# Add a label to display the results
result_label = tk.Label(
    app,
    text="",
    font=("Arial", 12),
    bg="lightgrey",
    fg="black",
    relief="groove",
    wraplength=450,
    justify="left",
)
result_label.pack(pady=20, fill="both", expand=True)

# Run the application
app.mainloop()
