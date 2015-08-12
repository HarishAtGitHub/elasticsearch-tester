from ET import *

# issue- 12790 : https://github.com/elastic/elasticsearch/issues/12790
# 1. create an index a_index.
# 2. get the settings of the index.
# 3. use result from above to create new index.
# 4. get settings of the index of step 3

indexone_name = "index1";
indextwo_name = "index2";
#*******************************************************
#1
put("http://localhost:9200/%s" % (indexone_name))

#********************************************************
#2
indexone_settings = get("http://localhost:9200/%s/_settings" % (indexone_name));
settings = indexone_settings.get(indexone_name);

#*********************************************************
#3
put("http://localhost:9200/%s" % (indextwo_name), settings);

#********************************************************
#4
get("http://localhost:9200/%s/_settings" % (indextwo_name));

#NOTE: for repeated test case just change the indexone_name & indextwo_name values above and run
