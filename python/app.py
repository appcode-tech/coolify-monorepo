from flask import Flask

app = Flask(__name__)

@app.route('/.well-known/acme-challenge/challenge')
def acme_challenge():
    return '2b7e39f4343b137f9585676fc4cfac7af4b3d27c8a9a966ab07ea0a60cdbc58c'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')