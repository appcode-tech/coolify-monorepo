from flask import Flask

app = Flask(__name__)

@app.route('/.well-known/acme-challenge')
def acme_challenge():
    return 'Your ACME challenge response here!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')