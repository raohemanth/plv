import random
import datetime
import matplotlib.pyplot as plt
from pip import main

avl_tree_execution_time_list = []
rb_tree_execution_time_list = []
splay_execution_time_list = []

size_of_array = 5000
list_of_lists_to_balance = []
number_of_runs = 20
count = 0
max_range_of_random_number=10000000

while count < number_of_runs:
    list_to_balance = random.sample(range(1,max_range_of_random_number),size_of_array)
    if count < number_of_runs:
        final_list_to_append = sorted(list_to_balance[:count])+list_to_balance[count:size_of_array]
        list_of_lists_to_balance.append(final_list_to_append)
        list_of_lists_to_balance.append(final_list_to_append[::-1])
    else:
        list_of_lists_to_balance.append(list_to_balance)
    count+=1

for indv_list_to_balance in list_of_lists_to_balance:

    avl_trees_start_time = datetime.datetime.now()
    avl_trees.main(indv_list_to_balance)
    avl_trees_end_time = datetime.datetime.now()
    avl_trees_time_difference = avl_trees_end_time - avl_trees_start_time
    avl_tree_execution_time_list.append(avl_trees_time_difference.microseconds)

    rb_trees_start_time = datetime.datetime.now()
    rb_trees.main(indv_list_to_balance)
    rb_trees_end_time = datetime.datetime.now()
    rb_trees_time_difference = rb_trees_end_time - rb_trees_start_time
    rb_tree_execution_time_list.append(rb_trees_time_difference.microseconds)

    splay_trees_start_time = datetime.datetime.now()
    splay_trees.main(indv_list_to_balance)
    splay_trees_end_time = datetime.datetime.now()
    splay_trees_time_difference = avl_trees_end_time - avl_trees_start_time
    splay_execution_time_list.append(splay_trees_time_difference.microseconds)

    dictionary_of_time_stamps = {
        avl_trees_time_difference.microseconds : "AVL Trees",
        rb_trees_time_difference.microseconds : "Red Black Trees",
        splay_trees_time_difference.microseconds : "Splay Trees",
    }

    minimum_time = min(list(dictionary_of_time_stamps.keys()))
    print("List to balance - {}. AVL - {}, RB - {}, Splay - {}, Winner - {}\n".format([], avl_trees_time_difference.microseconds, rb_trees_time_difference.microseconds, splay_trees_time_difference.microseconds,dictionary_of_time_stamps[minimum_time]))

plt.plot([i for i in range(0,len(list_of_lists_to_balance))], avl_tree_execution_time_list, label = "AVL")
plt.plot([i for i in range(0,len(list_of_lists_to_balance))], rb_tree_execution_time_list, label = "RB")
plt.plot([i for i in range(0,len(list_of_lists_to_balance))], splay_execution_time_list, label = "SPLAY")
plt.title('Comparison between number of hash functions and false positives in  Bloom Filter')
plt.xlabel('Number of {} functions'.format(""))
plt.ylabel('Number of false positives')
plt.legend()
plt.show()

if __name__ == "__main__":
    main