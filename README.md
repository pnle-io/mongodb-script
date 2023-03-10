## MongoDB Altas 🌏 - Enviroment Assessment 

### Get Colletion Stats

Get all statistics data from all collections.  

-  <a href="/get_collection_stats/getCollStats.py">getCollStats.py</a>  - Loop through all defined clusters and databases to get collection statistics data.  
    Please run this on the shell 
    ```shell 
    python3 getCollStats.py
    ```
    The output for this script is **cluster-result.json**
-  postCollStats.sh - Shell script using mongoimport to import JSON output from getCollStats.py to an MongoDB collection for further analysis.  

How to run the script:  
1.  Update the connection string from  
2.  Update file postCollStats.sh to define connection string for MongoDB instance storing statistics data.  
3.  Use MongoDB Compass or CLI to query and analyse the statistics data.  


         
