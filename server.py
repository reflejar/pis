from flask import Flask

server = Flask(__name__)
@server.route('/k8s/readiness/')
def readiness(): return "OK", 200 
@server.route('/k8s/liveness/') 
def liveness(): return "OK", 200  