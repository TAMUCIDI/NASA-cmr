from cmr import CollectionQuery, GranuleQuery
import json

mode="CMR_OPS"

api = CollectionQuery(mode=mode)
# api = GranuleQuery(mode="CMR_UAT")

collections = api.format("native").concept_id(["C1214614210-SCIOPS"]).get_all()

# with open("{}_collections.json".format(mode), "w") as file:
#     json.dump(collections, file)

for c in collections:
    print(c)