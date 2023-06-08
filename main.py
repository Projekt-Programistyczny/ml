import pandas as pd
from sklearn.cluster import KMeans
from database import *
import matplotlib.pyplot as plt


df = select_joined_tables()

data = [{'url': real_estate.url, 'total_price': real_estate.total_price, 'area': real_estate.area, 'type_of_estate': 1 if link.type_of_estate == 'dom' else 2} for real_estate, link in df]
df = pd.DataFrame(data)

features = ['total_price', 'area']

df = df[df['total_price'] != -1]
df = df[df['area'] != -1]
X = df[features]

# Określ liczbę klastrów (grup) do znalezienia
n_clusters = 3

# Wykonaj grupowanie k-means
kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(X)

centroids = kmeans.cluster_centers_

# Wyświetlanie centroid
for i, centroid in enumerate(centroids):
    print(f"Centroid {i+1}: {centroid}")

# Przypisz etykiety klastrów do danych
labels = kmeans.labels_

# Dodaj etykiety klastrów do DataFrame
df['cluster_label'] = labels
print(labels)
# Wyświetl wyniki grupowania
# print(df[['url', 'total_price', 'area', 'type_of_estate', 'cluster_label']])


for index, estate in df.iterrows():
    add_category(estate.url, estate.cluster_label)
    print(index)


