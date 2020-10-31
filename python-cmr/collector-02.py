from cmr import CollectionQuery, GranuleQuery
import json
import os

def load_collection(p):
    with open(p, "r") as f:
        collection = json.load(f)
    return collection

def get_providor():
    with open("providor.txt", "r") as f:
        p = [x.strip() for x in f.readlines()]
    return p

# ops_collection = load_collection("CMR_OPS_collections.json")
# ops_collection_id = [x["id"] for x in ops_collection]

providor = get_providor()

def get_p(api, p, start_page):
    export_file_path = os.path.join(export_path, "{}.json".format(p))
    print("Writing", export_file_path)
    g = api.provider(p).get_all(start_page)
    # granules[p] = g
    with open(export_file_path, "w") as f:
        json.dump(g, f)

def get_all(api):
    for p in providor:
        get_p(api, p)

export_path = "/h/diya.li/cidi/cmr-spider/data/GES_DISC"
api = GranuleQuery(mode="CMR_OPS", export_path=export_path)
# get_all(api)
get_p(api, "GES_DISC", 1)
