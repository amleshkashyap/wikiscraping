import wikiBot
import pywikiBOT
import json
from flask import Flask, request, Response
# import numpy as np

wikiEngines = [wikiBot, pywikiBOT]
wikiEngineNames = ["wikipedia", "pywikibot"]

server = Flask(__name__)


def findEngine(engine):
    global wikiEngines, wikiEngineNames
    count = 0
    for key in wikiEngineNames:
        if engine == key:
            engineModule = wikiEngines[count]
            break
        count = count + 1
    if count == len(wikiEngines):
        raise Exception()
    else:
        return engineModule


@server.route('/wikiSearch', methods=['GET'])
def searchHandler():
    queryReq = request.get_json()
    query = queryReq['query']
    engine = queryReq['engine']
    try:
        engineModule = findEngine(engine)
    except:
        return "Invalid Engine Name"
    search = engineModule.searchQuery(query)
    jsonDict = {}
    jsonDict['search'] = search
    return Response(json.dumps(jsonDict), status=200, mimetype='application/json')


@server.route('/wikiSummary', methods=['GET'])
def summaryHandler():
    queryReq = request.get_json()
    query = queryReq['query']
    engine = queryReq['engine']
    try:
        engineModule = findEngine(engine)
    except:
        return "Invalid Engine Name"
    summary = engineModule.summaryQuery(query)
    jsonDict = {}
    jsonDict['summary'] = summary
    return Response(json.dumps(jsonDict), status=200, mimetype='application/json')


@server.route('/wikiPage', methods=['GET'])
def pageHandler():
    queryReq = request.get_json()
    query = queryReq['query']
    engine = queryReq['engine']
    try:
        engineModule = findEngine(engine)
    except:
        return "Invalid Engine Name"
    page = engineModule.pageQuery(query)
    jsonDict = {}
    jsonDict['page'] = page
    return Response(json.dumps(jsonDict), status=200, mimetype='application/json')


if __name__ == "__main__":
    server.run('localhost', 7000)