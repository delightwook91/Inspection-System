from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, abort
import api_handler
import json

app = Flask(__name__)
api=Api(app)

@app.route('/api_gate/Bottleneck/<ip1>/<ip2>/<mod1>/<mod2>/<test>',methods=['POST','PUT'])
def api_bottleneck(ip1,ip2,mod1,mod2,test):
    return api_handler.start_bottleneck('Bottleneck',ip1,ip2,mod1,mod2,test)

@app.route('/api_gate/Monitoring/<tool>/<ip>/<port>/<pas>/<user>/<name>/<type>/<vm_ip>/<vm_id>',methods=['POST','PUT'])
def api_monitoring(tool,ip,port,pas,user,name,type,vm_ip,vm_id):
    return api_handler.start_monitoring(tool,ip,port,pas,user,name,type,vm_ip,vm_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000,
            debug=True,)

# data = [['192.168.11.3', '192.168.11.31'],['root', 'root'],'netstat -nap | grep ESTAB | wc -l']
# call_case('Bottleneck',data)
# { "ip1" : "192.168.11.3", "ip2" : "192.168.11.31"

    # print("############################################")
    # print("###################### GET data : ",msg)
    # print("############################################")
    # print("############################################")
    # print("###################### GET data : ", ip1)
    # print("############################################")
    # print("############################################")
    # print("###################### GET data : ", ip2)
    # print("############################################")
    # print("############################################")
    # print("###################### GET data : ", mod1)
    # print("############################################")
    # print("############################################")
    # print("###################### GET data : ", mod2)
    # print("############################################")
    # print("############################################")
    # print("###################### GET data : ", test)
    # print("############################################")