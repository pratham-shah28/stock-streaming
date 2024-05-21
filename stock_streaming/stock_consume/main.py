# from cassandra.cluster import Cluster
#
#
# cluster = Cluster(['localhost'], port=9042)
# session = cluster.connect('tutorial')
from cassandra.cluster import Cluster

# Connect to the Cassandra cluster
cluster = Cluster(['localhost'], port=9042)
session = cluster.connect('tutorial')

# Define the query to create a table if it does not exist
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    last_traded_price DECIMAL,
    last_traded_time TIMESTAMP
);
"""

# Execute the query
session.execute(create_table_query)
cluster.shutdown()
