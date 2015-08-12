from ET import *

# issue- 12790 : https://github.com/elastic/elasticsearch/issues/12790
# 1. create an index a_index.
# 2. get the settings of the index.
# 3. use result from above to create new index.
# 4. get settings of the index of step 3

#********************************************************
#1
put("http://localhost:9200/indextry1")

#********************************************************
#2
indexone_settings = get("http://localhost:9200/indextry1/_settings");
settings = indexone_settings.get("indextry1");

#*********************************************************
#3
put("http://localhost:9200/indextry2", settings);

#********************************************************
#4
get("http://localhost:9200/indextry2/_settings");
