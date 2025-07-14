import requests
import datetime

print("AI Ops Monitoring App")
print(f"Current time: {datetime.datetime.now()}")

# Simulate a health check by querying a public API
try:
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        print("GitHub API is healthy!")
    else:
        print(f"GitHub API returned status: {response.status_code}")
except Exception as e:
    print(f"Error checking API: {e}")

print("Running inside a Docker container!")