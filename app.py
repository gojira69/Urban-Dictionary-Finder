from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

APIKey = '6bb4804c0bmshab33739dd5d1524p1457f5jsna74cb460920a'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/define',methods=['GET'])
def define():
    term = request.args.get('term')
    url = f'https://mashape-community-urban-dictionary.p.rapidapi.com/define?term={term}'
    headers = {
        'X-RapidAPI-Key': APIKey,
        'X-RapidAPI-Host': 'mashape-community-urban-dictionary.p.rapidapi.com',
    }

    try:
        response = requests.get(url,headers=headers)
        data = response.json()
        return jsonify(data)
    except Exception as error:
        return jsonify({'error': 'Error fetching data!'})
    
if __name__ == '__main__':
    app.run(debug=True)