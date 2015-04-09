import csv
import math

# train 是map格式 map.key 是user_id, map.values是set，应当为购买的物品集合
#输入数据应当保证物品集合是同一个category

def item_similarity(train):
    C = dict()
    N = dict()
    for u, items in train.items():
        for i in items:
            N[i] += 1
            for j in items:
                if i == j:
                    continue
                if i not in C:
                    C[i] = dict()
                    C[i][j] = 1
                else:
                    C[i][j] += 1

    W = dict()
    for i, related_items in C.items():
        for j, cij in related_items.items():
            if i not in W:
                W[i] = dict()
            W[i][j] = cij / math.sqrt(N[i] * N[j])
    return W


def recommend(train, user_id, W, K):
    rank = dict()
    ru = train[user_id]
    for i in ru.items():
        for j, wj in sorted(W[i].items(), key=lambda x, y: y, reverse=True)[0:K]:
            rank[j].weight +=  wj

    rank = sorted(rank.items(), key=lambda x, y: y.weight, reverse=True)
    return rank









