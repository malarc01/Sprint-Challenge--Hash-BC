#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    if length == 1:
        # print('***')
        return None

    for index, item in enumerate(weights):
        hash_table_insert(ht, item, index)
        # print('added to hashtable, item, index)

    for item_in_list in range(len(weights)):
        result = limit-weights[item_in_list]
        value = hash_table_retrieve(ht, result)
        if value != None:
            output = (max(item_in_list, value),
                      min(item_in_list, value))
            return output


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
