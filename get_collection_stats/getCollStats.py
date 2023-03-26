from pymongo import MongoClient
from urllib.parse import urlparse
import json

#example of connection string mongodb+srv://<<YOUR_USERNAME>>:<<YOUR_PASSWORD>>@fastanalytic.zqqqy.mongodb.net/?retryWrites=true&w=majority
conn_str_0 = "<connection-string-cluster-1>"
conn_str_1 = "<connection-string-cluster-2>"
conn_str_2 = "<connection-string-cluster-3>"

conn_pool = [conn_str_0, conn_str_1, conn_str_2]
output = []

for conn in conn_pool:
    parsed_uri = urlparse(conn)
    cluster_name = parsed_uri.hostname.split('.')[0]
    client = MongoClient(conn)
    for db in client.list_database_names():
        if db not in ["admin", "config", "local"]:
            for coll in client[db].list_collections():            
                if (coll["name"] not in [ "system.views" ]) and ( coll["type"] != "view" ):
                    try:
                        avgObjSize = client[db].command("collStats", coll["name"], scale = 1024*1024 )["avgObjSize"]
                    except KeyError:
                        avgObjSize = "N/A"
                    try:
                        num_doc = client[db].command("collStats", coll["name"])["count"]
                    except KeyError:
                        num_doc = "N/A"                    
                    coll_stat = {
                        "cluster_name": cluster_name,
                        "db_name": db,
                        "coll_name": coll["name"],
                        "coll_size_MB": client[db].command("collStats", coll["name"], scale = 1024*1024 )["size"],
                        "avg_obj_size_Bytes": avgObjSize,
                        "num_doc": num_doc,
                        "storage_size_MB": client[db].command("collStats", coll["name"], scale = 1024*1024 )["storageSize"],
                        "num_idx": client[db].command("collStats", coll["name"])["nindexes"],
                        "idx_size_MB": client[db].command("collStats", coll["name"], scale = 1024*1024 )["totalIndexSize"],
                        "total_size_MB": client[db].command("collStats", coll["name"], scale = 1024*1024 )["totalSize"],
                    }
                    output.append(coll_stat)
    client.close()

output_file = 'cluster-result.json'
with open(output_file, "w") as f:
    f.write(json.dumps(output, indent=4))
