from config import app 

# start the flask app and run app on 5000 port number
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")