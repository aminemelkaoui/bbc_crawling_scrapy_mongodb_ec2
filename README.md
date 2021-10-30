# bbc_crawling_scrapy_mongodb_ec2
this is a scraping project using scrapy mongoDb flask and aws ac2
bbccraling file most important files  : scraping file called bbc_crawling.py executing it should scrap and follow the main news link and crawl the most important data from bbc.com/news 
                          the pipeline.py file which erase old data and push the crawled data to MongoDb databse called bbc_crawl 
RestAPI file contains : BBC_newsSearchRestAPI.py which is an API app created using flask framework and published on an AWS EC2 repository 
                          
API ec2 link: http://54.242.186.78/new 'the whole data"
              http://54.242.186.78/headline_report/<key> 'research keywords in article report '
              http://54.242.186.78//headline_text_full/<key> 'research keywords in article title'
thank you for the time you spend reading and examining my project 
  NB:"the data is not all cleaned because it’s a warehousing scraping and i didn't scrap all the data from the website because it’s just a preview challenge and I didn't automate scraping because I'm sure it's recommended to do it using kafka technology"
