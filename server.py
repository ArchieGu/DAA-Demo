import json 
from flask import Flask, request, jsonify 
import argparse

from BackEnd.Path.Map.utils import calculate_path

app = Flask(__name__)

@app.route('/cal_path', methods=['POST'])
def cal_path():
    try:
        data = request.get_data()
        data = json.loads(data)
    except Exception as e:
        print('get data error: {}'.format(e))
        return jsonify({
            'code': 400,
            'msg': '发送数据错误',
            'data': []
        }), 400

    path = calculate_path(data)
    return jsonify({
        'code': 0,
        'data': path 
    })
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port',  type=int,
                    help='an integer for the port')
    # 解析参数步骤  
    args = parser.parse_args()

    host = 'localhost'
    port = args.port 
    print('calculte node run: {}:{}'.format(host, port))
    app.run(debug=True, host=host, port=port)