from flask import Flask, render_template, url_for, send_file, request, flash

app = Flask(__name__)

@app.route('/')
def index():
    about_img = url_for('static', filename='images/about.jpg')
    bg_img = url_for('static', filename='images/bg_1.jpg')
    return render_template('index.html', about_img = about_img, bg_img = bg_img)

@app.route('/contact')
def contact():
    return render_template('form.html')


@app.route('/download_file')
def download_file():
    path="RESUME.pdf"
    return send_file(path,as_attachment=True)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
