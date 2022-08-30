# README.md
Query all collection in all database, excepting views collection and system, local, config databases

## Notes:
- getCollStats.py: Loop through all defined cluster connection, query all collection at all databases in the cluster to get the statistics
- postCollStats.py: Shell script which uses mongoimport to load statistics data to another MongoDB collection for further analysis

## Execution:
1. Update the file getCollStats.py to define the list of connection string to query the collection stats
2. Update the file postCollStats.sh to use mongoimport to import data to an MongoDB collection for further analysis
3. Use MongoDB Compass or CLI to query statistics data