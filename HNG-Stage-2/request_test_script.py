#!/usr/bin/env python3
import requests

# Define the base URL of your API
base_url = "http://localhost:8000/api/"  # Replace with your API URL

# Helper function to print response content
def print_response(response):
    print(f"Response Status Code: {response.status_code}")
    print("Response Content:")
    print(response.json())

# CREATE: Add a new person
create_data = {
    "name": "Ladi Seth",
    "age": 20,
    "email": "ladiseth@gmail.com"
}
create_response = requests.post(base_url, json=create_data)
print("CREATE:")
print_response(create_response)

# READ: Fetch details of a person by user_id (replace 1 with the actual user_id)
read_response = requests.get(base_url + "1/")
print("READ:")
print_response(read_response)

# UPDATE: Modify details of an existing person by user_id (replace 1 with the actual user_id)
update_data = {
    "name": "ladi kabig seth",
    "age": 20,
    "email": "ladikabigseth@gmail.com"
}
update_response = requests.put(base_url + "1/", json=update_data)
print("UPDATE:")
print_response(update_response)

# DELETE: Remove a person by user_id (replace 1 with the actual user_id)
delete_response = requests.delete(base_url + "1/")
print("DELETE:")
print_response(delete_response)
