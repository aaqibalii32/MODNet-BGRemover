from api import app as APPLICATION

if __name__ == '__main__':
    APPLICATION.run(host="0.0.0.0", port=80, debug=True)
