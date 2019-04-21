from flask import Flask
from avito import get_html

app = Flask(__name__) 

@app.route('/')
def index():
    html = get_html('Ibanez')
    return html
if __name__ == '__main__':
    app.run()