from views.view import app

if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True, port=80,host='127.0.0.1')
