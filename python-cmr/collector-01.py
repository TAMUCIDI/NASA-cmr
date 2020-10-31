from cmr import CollectionQuery, GranuleQuery
import json

api = GranuleQuery(mode="CMR_OPS")
# api = GranuleQuery(mode="CMR_UAT")

collections = api.get_all()

with open("CMR_UAT_collections.json", "w") as file:
    json.dump(collections, file)