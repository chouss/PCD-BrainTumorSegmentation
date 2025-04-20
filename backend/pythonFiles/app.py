from flask import Flask, request,jsonify
from flask_cors import CORS
import uploadIMG

app = Flask(__name__)
@app.route('/')
def app():
    print("")
@app.route('/uploadIMG', methods=['GET','POST'])
def doUploadIMG():
    uploadIMG()


@app.route('/Segmentation', methods=['GET','POST'])
def doSegmentation():
    ()
if __name__ == '__main__':
    CORS(app)
    app.run()