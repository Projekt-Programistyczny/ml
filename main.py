import pandas as pd
from sklearn.cluster import KMeans
from database import *
# Wczytaj dane z bazy danych
# Zakładając, że dane są przechowywane w DataFrame o nazwie "df"
# gdzie każda kolumna odpowiada jednej cechy (url, total_price, rent, area, rooms, floor, type, status, region)
# df = pd.read_sql_table('real_estates', 'postgresql://postgres:EtronQ72021!@34.127.125.226/real-estate-analyzer')
df = select_used()
print(vars(df[1]))

data = [{'id':obj.id, 'total_price': obj.total_price, 'rent': obj.rent, 'area': obj.area, 'rooms': obj.rooms} for obj in df]
df = pd.DataFrame(data)#, columns = [ 'id', 'url', 'description', 'total_price', 'price', 'rent', 'currency', 'area', 'rooms', 'deposit', 'floor', 'type', 'status', 'region'])
# Wybierz interesujące cechy do analizy grupowania

features = ['total_price', 'area', 'rooms']
# print(df)
# X = df[features]
df = df[df['rent'] == 0]
df = df[df['total_price'] != -1]
df = df[df['rooms'] != -1]
X = df[features]

# Określ liczbę klastrów (grup) do znalezienia
n_clusters = 3

# Wykonaj grupowanie k-means
kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(X)

# Przypisz etykiety klastrów do danych
labels = kmeans.labels_

# Dodaj etykiety klastrów do DataFrame
df['cluster_label'] = labels
print(labels)
# Wyświetl wyniki grupowania
print(df[['id', 'total_price', 'rent', 'area', 'rooms', 'cluster_label']])




