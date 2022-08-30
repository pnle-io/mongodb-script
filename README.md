# README.md
## MongoDB scripting for example demo purpose

### Note:
- get_collection_stats: Get all statistics data from all collections
      How to execute:
      1. Update file getCollStats.py to define list of connection string
      2. Update file postCollStats.sh to define connection string for MongoDB instance storing statistics data
      3. Use MongoDB Compass or CLI to query and analyse the statistics data


### Directory structure:
/ mongodb-script
    / get_collection_stats
         \/ getCollStats.py - Loop through all defined cluster and database to get collection statistics data
         / postCollStats.sh - Shell script using mongoimport to import JSON output from getCollStats.py to an MongoDB collection for further analysis
         
