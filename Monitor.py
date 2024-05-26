import requests
import time
from tabulate import tabulate

# Function to check the status of a subdomain
def check_status(subdomain):
    try:
        return "Up" if requests.get(f"http://{subdomain}.yourdomain.com").status_code == 200 else "Down"
    except requests.ConnectionError:
        return "Down"

# List of subdomains to monitor
subdomains_to_monitor = ["service1", "service2", "service3"]

# Continuously monitor subdomains status
while True:
    statuses = []
    for subdomain in subdomains_to_monitor:
        print(tabulate(statuses, headers=["Subdomain", "Status"], tablefmt="grid"))
    time.sleep(60)  # Wait for 1 minute before checking again