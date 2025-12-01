from flask import Flask, render_template
from pathlib import Path
import os

app = Flask(__name__)

# Get absolute paths for Vercel
base_path = Path(__file__).parent.parent  # Go up to root directory

# Set template and static folders
app.template_folder = str(base_path / 'templates')
app.static_folder = str(base_path / 'public')  # Use 'public' folder instead
app.static_url_path = '/public'

# Define all available pages (can extend up to 100)
AVAILABLE_PAGES = {
    'page_001': '001.html',
    'page_002': '002.html',
    'page_003': '003.html',
    'page_004': '004.html',
    'page_005': '005.html',
    'page_006': '006.html',
    'page_007': '007.html',
    'page_008': '008.html',
    'page_009': '009.html',
    'page_010': '010.html',
}

def get_available_pages():
    """Check which HTML files actually exist in templates folder"""
    available = {}
    template_dir = Path('templates')

    for page_id, filename in AVAILABLE_PAGES.items():
        filepath = template_dir / filename
        if filepath.exists():
            available[page_id] = filename

    return available

@app.route('/')
def index():
    # Get only available pages to pass to template
    available_pages = get_available_pages()
    return render_template('index.html', available_pages=available_pages)

@app.route('/page_001')
def page_001():
    return render_template('001.html')

@app.route('/page_002')
def page_002():
    return render_template('002.html')

@app.route('/page_003')
def page_003():
    return render_template('003.html')

@app.route('/page_004')
def page_004():
    return render_template('004.html')

@app.route('/page_005')
def page_005():
    return render_template('005.html')

@app.route('/page_006')
def page_006():
    return render_template('006.html')

@app.route('/page_007')
def page_007():
    return render_template('007.html')

@app.route('/page_008')
def page_008():
    return render_template('008.html')

@app.route('/page_009')
def page_009():
    return render_template('009.html')

@app.route('/page_010')
def page_010():
    return render_template('010.html')

if __name__ == '__main__':

    app.run(debug=True)
