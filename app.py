from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Choose Discipline!'

@app.route('/discipline')
def discipline():
    # write a motivational quote
    return 'Discipline is the bridge between goals and accomplishment. - Jim Rohn'

if __name__ == '__main__':
    app.run()
