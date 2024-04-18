from flask import Flask, jsonify, request
from db import return_cnt,get_data

app = Flask(__name__)

@app.route("/kino", methods=['GET'])
def kino_api():
    y = int(request.args.get('page')) 
    return jsonify({
        "page": return_cnt()[0],
        "currentPage": y,
        "data":get_data(y),
        "status": 200 
    })

if __name__ == "__main__":
    app.run(debug=True)
