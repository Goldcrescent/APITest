from flask import *
import requests

app = Flask(__name__)
@app.route('/api', methods=['POST'])

def api():
    data = request.get_json()
    url = data['url']
    method = data['method']
    headers = data.get('headers', {})
    body = data.get('body', {})

    try:
        if method == 'GET':
            response = requests.get(url, headers=headers, params=body)
        elif method == 'POST':
            response = requests.post(url, headers=headers, json=body)
        elif method == 'PUT':
            response = requests.put(url, headers=headers, json=body)
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers, json=body)
        else:
            return jsonify({'error': 'Unsupported HTTP method'}), 400
        return jsonify({
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'body': response.json() if response.content else None
        })
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500
    if __name__ == '__main__':
        app.run(debug=True)