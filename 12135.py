from ET import *

# issue- 12135 : https://github.com/elastic/elasticsearch/issues/12135
# 1. create an index(cast) and type(type) and post the data given
# 2. create another index (cast2) and type (type) with mappings of data to ip
# 3. post data to index.type in step 2
# 4. implement the search query cast,cast2/_search?search_type=count

#********************************************************
#1
data1 = {
          "ip_str":"0.0.0.0"
        }
post("http://localhost:9200/cast/type/1", data1)

#********************************************************
#2
post("http://localhost:9200/cast2");
mappings = {
             "properties" : {
               "ip_str":{
                 "type":"ip"
                }
              }
           }
post("http://localhost:9200/cast2/type/_mapping", mappings);

#*********************************************************
#3
data2 = {
          "ip_str":"0.0.0.0"
        }
post("http://localhost:9200/cast2/type/1", data2);

#*********************************************************
#4
search = {
           "aggs": {
             "NAME": {
               "terms": {
                 "field": "ip_str",
                 "size": 10
               }
             }
           }
         }
post("http://localhost:9200/cast,cast2/_search?search_type=count", search);
