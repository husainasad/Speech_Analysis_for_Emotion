from flask import Flask, render_template
# import filename
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('main.html')

if __name__ == '__main__':
   app.run(debug = True)
