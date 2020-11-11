from cmr import CollectionQuery, GranuleQuery
import json

mode="CMR_OPS"

api = CollectionQuery(mode=mode)
# api = GranuleQuery(mode=mode)

collections = api.format("umm_json").concept_id(["C1214305813-AU_AADC"]).get(1)

# granule = api.format("json").short_name("OMTO3e").get(1)
# with open("{}_collections.json".format(mode), "w") as file:
#     json.dump(collections, file)

for c in collections:
    print(c)