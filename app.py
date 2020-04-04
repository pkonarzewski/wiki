from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

@app.route('/')
def root():
    # return render_template('index.html')
    return send_from_directory('.', 'index.html')

if __name__ == "__main__":
    app.run()
