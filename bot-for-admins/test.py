from flask import Flask, jsonify, request
from bot import get_data,cnt_vd
app = Flask(__name__)

@app.route("/kino", methods=['GET'])
def kino_api():
    y = int(request.args.get('page'))
    print("-----------")
    print(y)
    print(cnt_vd())
    print(get_data(y))
    print("-----------")
    return jsonify({
        "page": cnt_vd()/10,
        "currentPage": y,
        "data":get_data(y),
        "status": 200 
    })

if __name__ == "__main__":
    app.run(debug=True)
