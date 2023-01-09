from pymongo import MongoClient
import json

conn_str_0 = "<connection-string-cluster-1>"
conn_str_1 = "<connection-string-cluster-2>"
conn_str_2 = "<connection-string-cluster-3>"

conn_pool = [conn_str_0, conn_str_1, conn_str_2]
output = []

for conn in conn_pool:
    client = MongoClient(conn)
    for db in client.list_database_names():
        if db not in ["admin", "config", "local"]:
            for coll in client[db].list_collections():            
                if (coll["name"] not in [ "system.views" ]) and ( coll["type"] != "view" ):
                    coll_stat = {
                        "db_name": db,
                        "coll_name": coll["name"],
                        "coll_size_MB": client[db].command("collStats", coll["name"], scale = 1024*1024 )["size"],
                        "avg_obj_size_MB": client[db].command("collStats", coll["name"], scale = 1024*1024 )["avgObjSize"],
                        "num_doc": client[db].command("collStats", coll["name"])["count"],
                        "storage_size_MB": client[db].command("collStats", coll["name"], scale = 1024*1024 )["storageSize"],
                        "num_idx": client[db].command("collStats", coll["name"])["nindexes"],
                        "idx_size_MB": client[db].command("collStats", coll["name"], scale = 1024*1024 )["totalIndexSize"],
                        "total_size_MB": client[db].command("collStats", coll["name"], scale = 1024*1024 )["totalSize"],
                    }
                    output.append(coll_stat)
    client.close()
print(json.dumps(output))

