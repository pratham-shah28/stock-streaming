from cassandra.cluster import Cluster


cluster = Cluster(['localhost'], port=9042)
session = cluster.connect('tutorial')
# contact_points = ['localhost']
# port = 9042
# cluster = Cluster(contact_points, port=port)
# session = cluster.connect()