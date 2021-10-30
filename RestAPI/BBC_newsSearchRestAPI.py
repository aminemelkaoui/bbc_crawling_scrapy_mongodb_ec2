# BBC News Search Rest API

from   flask import Flask
from   flask_restful import Resource, Api
from   flask_pymongo import PyMongo
from   bson import json_util
import json

# Connecting to MongoDB containing the crawled BBC News Articles.
app    = Flask(__name__)
app.config['MONGO_DBNAME'] = 'bbc_crawler'
app.config['MONGO_URI']    = 'mongodb+srv://melkaoui:1986@cluster0.1yk9u.mongodb.net/bbc_crawl?retryWrites=true&w=majority'
api                        = Api(app)
mongo                      = PyMongo(app)

def MDBtoJson(data):
    """Convert Mongo to JSON"""
    return json.dumps(data, default=json_util.default)

class BBC_News(Resource):
    def get(self):
        # extract the entire dataset from mongoDb repository 
        results = mongo.db.bbc_crawler.find()
        json_results = []
        for result in results:
            json_results.append(result)
        return MDBtoJson(json_results)

class SearchNewsTextKeyword(Resource):
    def get(self, keyword):
        # getting news headlines titles by keywords 
        results = mongo.db.bbc_crawler.find({'headline_text_full': {'$regex': '.*' + keyword + '.*'}})
        json_results = []
        for result in results:
            json_results.append(result)
        return MDBtoJson(json_results)

class SearchNewsHeadlineKeyword(Resource):
    def get(self, keyword):
        # getting news headlines full report by keywords 
        results = mongo.db.bbc_crawler.find({'headline_report': {'$regex': '.*' + keyword + '.*'}})
        json_results = []
        for result in results:
            json_results.append(result)
        return MDBtoJson(json_results)

api.add_resource(SearchNewsHeadlineKeyword, '/headline_report/<string:keyword>') # display the  headlines full report that conatine's keyword 'must to be string'
api.add_resource(SearchNewsTextKeyword, '/headline_text_full/<string:keyword>') #  display the headlines titles that conatine's keyword 'must to be string'
api.add_resource(BBC_News, '/new') # display the entire database 

if __name__ == '__main__':
    app.run()