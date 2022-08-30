echo "Collect stats from all collections in all database..."
python3 getCollectionStatsByAllDb.py > outputCollStats.json
echo "Import to MongoDB collection..."
mongoimport --uri mongodb+srv://<user-name>:<password>@<mongodb-srv-uri>/<db-name> --collection <collection-name> --type JSON --file outputCollStats.json --jsonArray --drop
echo "Import completed!"
