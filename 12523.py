from ET import *

# issue- 12523 : https://github.com/elastic/elasticsearch/issues/12523
# procedure
# 1. create index
# 2. create type and its mappings with @timestamp field mapped to date
# 3. put values in the field mapped as date
# 4. search for unix epoch time stamp by giving the value given in step 3

#***************************************************************************
#1. create index named i1 
post("http://localhost:9200/i1");

#***************************************************************************
#2. create type and its mappings
mappings = {
       "properties" : { 
           "@timestamp" : {
            "type" :   "date"
           },
           "name" : {
            "type" :   "string"
           }
        }
}

post("http://localhost:9200/i1/i1_typeone/_mapping", mappings);

#***************************************************************************
#3. create an entry in the above type
data = {
  "name" : "harish",
  "@timestamp":1438142633505
};
post("http://localhost:9200/i1/i1_typeone/1", data);

#*************************************************************************
#4. match query - search
search = {
  "query": {
    "match": { 
      "@timestamp": "1438142633505"
    }
  }
};

post("http://localhost:9200/i1/_search", search);
