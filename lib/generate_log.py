from datetime import datetime
import requests
import os

def generate_log(data):
    # TODO: Implement log generation logic

    # STEP 1: Validate input
    # Hint: Check if data is a list

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")

    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename

    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Input data must be a list.")

    # STEP 2: Generate a filename with today's date
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    try:
        with open(filename, "w") as file:
            for entry in data:
                file.write(f"{entry}\n")
    except Exception as e:
        print(f"Error writing to file: {e}")
        return None

    # STEP 4: Print a confirmation message with the filename
    print(f"Log successfully generated: {filename}")
    return filename

def fetch_data():
    """Fetches a sample post from a public API."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))