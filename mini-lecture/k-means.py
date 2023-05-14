import numpy as np
import random
 
def cluster_points(X, mu):
    clusters = {}
    for x in X:
        best_mu = min([(i[0], np.linalg.norm(x-mu[i[0]])) for i in enumerate(mu)], key=lambda t:t[1])[0]
        try:
            clusters[best_mu].append(x)
        except KeyError:
            clusters[best_mu] = [x]
    return clusters
 
def reevaluate_centers(mu, clusters):
    new_mu = []
    keys = sorted(clusters.keys())
    for k in keys:
        new_mu.append(np.mean(clusters[k], axis = 0))
    return new_mu
 
def has_converged(mu, old_mu):
    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in old_mu]))
 
def find_centers(X, k):
    # Initialize to k random centers
    old_mu = random.sample(list(X), k)
    mu = random.sample(list(X), k)
    while not has_converged(mu, old_mu):
        old_mu = mu
        # Assign all points in X to clusters
        clusters = cluster_points(X, mu)
        # Reevaluate centers
        mu = reevaluate_centers(old_mu, clusters)
    return(mu, clusters)