import requests

def check_credentials(target_url, credentials):
    for credential in credentials:
        username, password = credential.split(":")
        try:
            response = requests.post(target_url, data={"username": username, "password": password}, timeout=5)
            if response.status_code == 200:
                print(f"Valid credential: {username}:{password}")
            else:
                print(f"Invalid credential: {username}:{password} (Status: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"Error during request for {username}: {e}")
