from flask import Flask , render_template
from data import Articles

app = Flask(__name__)
app.debug=True
@app.route('/')
def index():
    print("Success")
    # return "TEST"
    return render_template('home.html', hello = "GaryKim")

@app.route('/about')
def about():
    print("Success")
    # return "TEST"
    return render_template('about.html', hello = "GaryKim")

@app.route('/articles')       #methods = ['GET','POST'])로 추가 가능
def articles():
    print("Success")
    # return "TEST"
    articles = Articles()
    print(articles)
    return render_template('articles.html', articles = articles)

@app.route('/test')
def show_image():
    return render_template('image.html')

if __name__ =='__main__':
    # app.run(host = '0.0.0.0', port='8080')
    app.run()