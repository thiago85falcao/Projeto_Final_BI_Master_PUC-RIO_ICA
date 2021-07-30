def k_cluster_ideal(data, max_k=20):
    """[Ebow method.]

    Args:
        data ([dtype]): [dataframe]
        max_k ([int]): [numero max de clusters]
    """
    import matplotlib.pyplot as plt
    from sklearn.cluster import KMeans
    n_cluster = []
    inertias = []
    
    for k in range(1,max_k+1):
        kmeans_model = KMeans(init="k-means++",n_clusters=k,n_init=20)
        kmeans_model.fit(data)
        n_cluster.append(k)
        inertias.append(kmeans_model.inertia_)
        
    fig = plt.subplots(figsize=(10, 5))
    plt.plot(n_cluster, inertias, 'o-')
    plt.xlabel("Number of Clusters")
    plt.ylabel("Inertia")
    plt.grid(True)
    plt.show()

