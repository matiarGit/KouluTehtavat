from flask import Flask
import requests
app = Flask(__name__)
@app.route('/alkuluku/<Number>')
def alkuluku_laskin(Number):
    Number = int(Number)
    x = 0
    for i in range(2, Number):
        if Number % i == 0:
            x = 1

    if x == 0:
        isPrime = True
    else:
        isPrime = False

    vastaus = {

    "Number" : Number,
    "isPrime"  : isPrime

    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)