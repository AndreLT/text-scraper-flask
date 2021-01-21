from flask import Flask, jsonify, request, render_template
from scraper import Scraper
app = Flask(__name__)

@app.route('/')
def home_page():
    example_embed='This is embedded from app.py'
    return render_template('index.html', embed=example_embed)

@app.route('/test', methods=['GET', 'POST'])
def testfn():    # GET request
    if request.method == 'GET':
        return 'Sucesss', 200  # serialize and use JSON headers    # POST request
        
    if request.method == 'POST':
        data = request.json
        ua = data['ua']
        url = data['url']
        try:
            scraper = Scraper(url,ua)
            html = scraper.getter()
            tokens = scraper.cleanner(html)
            return {'tokens': scraper.frequency(tokens)}
        except :
            return {'error': "Something went wrong"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)