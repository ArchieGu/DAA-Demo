import json 
from flask import Flask, request, jsonify 

app = Flask(__name__)

@app.route('/cal_path', methods=['POST'])
def cal_path():
    try:
        data = request.get_data()
        data = json.loads(data)
    except Exception as e:
        print('get data error')
        return jsonify({
            'code': 400,
            'msg': '发送数据错误',
            'data': []
        }), 400

    return jsonify({
        'code': 0,
        'data': []
    })
    
if __name__ == '__main__':
    app.run(debug=True, port=9099)