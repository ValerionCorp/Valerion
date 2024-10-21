from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_nvidia_price():
    url = "https://stockanalysis.com/stocks/nvda/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        price = soup.select_one('.text-4xl')
        if price:
            return price.text.strip()
        else:
            return "No se encontró el precio."
    except requests.exceptions.RequestException as e:
        return f"Error al acceder al sitio: {e}"

@app.route('/')
def index():
    nvidia_price = get_nvidia_price()
    return render_template('index.html', price=nvidia_price)

if __name__ == "__main__":
    app.run(debug=True)
    