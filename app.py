from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route('/main', methods=['POST', 'OPTIONS'])
def main():

    file = request.files['file']
    print(file)

    return { "ok": True }

if __name__ == '__main__':
    app.run(host = 'localhost', port = 8000)


# from fileinput import filename
# from flask import Flask
# from flask_restful import Resource, reqparse, Api
# import socket
# import werkzeug
# import librosa
# from io import BytesIO
# from urllib.request import urlopen

# from run_detection import Model

# app = Flask(__name__)
# api = Api(app)

# ALLOWED_PROFILE_EXTENSIONS = {'.wav', 'mp4'}

# model = Model()

# def allowed_file(filename):
#     file_type = filename.split(".")[1]
#     if file_type in ALLOWED_PROFILE_EXTENSIONS:
#         return True
#     return False


# class ScreamDetect(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files', help="No 'file' header found")
#     parser.add_argument('url', type=str)

#     def post(self):
#         data = self.parser.parse_args()
        
#         file = data['file']
#         print(file)

#         if file is None or file.filename == '':
#             return {"errorCode": 3, "errorMessage": "Incorrect File Format"}, 400

#         if not allowed_file(file.filename):
#             return {"errorCode": 3, "errorMessage": "Incorrect File Format"}, 400

#         try:
#             file_ = file.read()
#             print(file_)
#             clip, sample_rate = librosa.load(file_, sr=None) 
#             rs = model.predict(clip, sample_rate)

#         except:
#             return {"errorCode": 1, "errorMessage": "Unreadable"}, 400
#         return {"errorCode": 0, "errorMessage": "Success", "label": rs[0], "class": rs[1]}, 200

# api.add_resource(ScreamDetect, "/screamdetect")

# def get_ip():
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     try:
#         s.connect(('10.255.255.255', 1))
#         IP = s.getsockname()[0]
#     except:
#         IP = '127.0.0.1'
#     finally:
#         s.close()
#     return IP


# if __name__ == '__main__':
#     app.run(host=get_ip(), port=5000, debug=True)