from ET import *
import sys

# issue- 12790 : https://github.com/elastic/elasticsearch/issues/12790
# 1. create an index with settings having creation_date and version
# 2. get settings of the index of step 1 
# Observed: the new index settings has creation_date and version same as settings given
# Expected: the new index settings should have creation_date and version to new updated values

indexone_name = "index1";
if sys.argv[1:]:
  indexone_name = sys.argv[1];
#*******************************************************
#1
settings            = {'settings': {
                                     'index': {
                                                 'number_of_replicas': '1', 
                                                 'version': {'created': '2000001'}, 
                                                 'creation_date': '1439384094544', 
                                                 'uuid': 'ayzHgwB3Sgey-Pk_Okgwyg', 
                                                 'number_of_shards': '5'
                                              }
                                   }
                      }
put("http://localhost:9200/%s" % (indexone_name), settings);

#********************************************************
#2
new_index = get("http://localhost:9200/%s/_settings" % (indexone_name));
print("input settings \n");
print(settings);
print("\n");
print("new index settings \n");
print(new_index.get(indexone_name));

#NOTE: for repeated test case just change the indexone_name value above and run
# or run with command line arguments
