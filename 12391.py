from ET import *

# issue - https://github.com/elastic/elasticsearch/issues/12391
# issue id - 12391
# 1. create content with a spelling mistake
# 2. make a get request to _search with content as the body

# actual o/p : crytic message Unexpected token START_OBJECT in [per_ring].
# expected o/p : user friendly and understandable message

content = {
   "aggs": {
      "nested_geodistance": {
         "nested": {
            "path": "addresses"
         },
         "aggs": {
           "per_ring": {
             "geo_distance": {
               "field": "addresses.location",
               "unit": "km",
               "orgin": {
                 "lat": 56.78,
                 "lon": 12.34
               },
               "ranges": [
                 {
                   "from": 100,
                   "to": 200
                 }
               ]
             }
           }
         }
      }
   }
}

post("http://localhost:9200/_search", content);
