#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for item_weight in range(0, len(weights)):
        hash_table_insert(ht, weights[item_weight], item_weight)

    for item_weight in range(0, len(weights)):
        query = limit - weights[item_weight]
        lookup = hash_table_retrieve(ht, query)
        if lookup is not None:
            tup = (max(item_weight, lookup),
                   min(item_weight, lookup))
            return tup

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
