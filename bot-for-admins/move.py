from flask import Flask, jsonify, request
from db import return_cnt

app = Flask(__name__)

@app.route("/kino", methods=['GET'])
def kino_api():
    y = int(request.args.get('page')) 
    return jsonify({
        "page": return_cnt()[0]//10,
        "currentPage": y,
        "data": [
            {
                "id": 1,
                "name": "yulduzlar jangi",
                "description": "lorem30",
                "photo_link": "hfdksfhds",
                "down_link": "jhdskfjhdskf"
            }
        ],
        "status": 200 
    })

if __name__ == "__main__":
    app.run(debug=True)
