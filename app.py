from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def string_reverse():
    if request.method == 'POST':
        text = request.json['text']
    else:
        text = request.values.get('text')
    if text:
        reversed_string = text[::-1]
        return jsonify({'success' : True, 'data' : { 'original_string' : text, 'reversed_string': reversed_string} }), 200
    return jsonify({'success' : False, 'error': 'string not provided'}), 404

if __name__ == '__main__':
    app.run(debug=True)
