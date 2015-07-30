from E import *

#create index named 
post("http://localhost:9200/i1");

#create type and its mappings
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

#create an entry in the above type
data = {
  "name" : "harish",
  "@timestamp":1438142633505
};
post("http://localhost:9200/i1/i1_typeone/1", data);

#match query - search
search = {
  "query": {
    "match": { 
      "@timestamp": "1438142633505"
    }
  }
};

post("http://localhost:9200/i1/_search", search);
