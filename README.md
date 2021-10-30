# bbc_crawling_scrapy_mongodb_ec2
this is a scraping project using scrapy mongoDb flask and aws ac2
bbccraling file contains : crawler file called bbc_crawling.py executing it should scrap news from bbc.com/news 
                          the pieline.py file which push the crawled data to MongoDb databse called bbc_crawl 
RestAPI file contains : BBC_newsSearchRestAPI.py which is an API app created using flask framework and published on an AWS EC2 repository 
                          
API ec2 link: http://54.242.186.78/new
              http://54.242.186.78/headline_report/<key>
              http://54.242.186.78//headline_text_full/<key>
thank you for the time you spend reading and examining my project 
