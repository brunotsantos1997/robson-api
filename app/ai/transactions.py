from typing import List

import numpy as np
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer

from app.data.model import UserTransactions


def generate_clusters(users_transactions_list: List[UserTransactions], k):
    list_of_transactions = []
    for i, user_transactions in enumerate(users_transactions_list):
        transactions = ''
        for transaction in user_transactions.transactions:
            transactions += ' ' + transaction.description

        list_of_transactions.append(transactions)

    vec = CountVectorizer()
    df = np.array(vec.fit_transform(list_of_transactions).toarray())
    kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=10)
    kmeans.fit(df)
    y_pred = kmeans.predict(df)
    print(y_pred)
    return y_pred
