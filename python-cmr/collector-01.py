from cmr import CollectionQuery, GranuleQuery
import json

mode="CMR_OPS"

api = GranuleQuery(mode=mode)
# api = GranuleQuery(mode="CMR_UAT")

collections = api.get_all()

with open("{}_collections.json".format(mode), "w") as file:
    json.dump(collections, file)