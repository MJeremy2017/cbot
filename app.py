from flask import Flask, request

app = Flask(__name__)


@app.route('/api/v1/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    return 'Data received: {}'.format(data)


if __name__ == '__main__':
    app.run(port=3000)
