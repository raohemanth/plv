import random
import datetime
import matplotlib.pyplot as plt
from algorithms_implemented import avl_trees
from algorithms_implemented import rb_trees
from algorithms_implemented import splay_trees

def get_list_of_lists_to_balance():
    size_of_array = 5000
    list_of_list_to_balance = []
    number_of_runs = 100
    count = 0
    max_range_of_random_number=10000000
    while count < number_of_runs:
        list_to_balance = random.sample(range(1,max_range_of_random_number),size_of_array)
        if count < number_of_runs:
            final_list_to_append = sorted(list_to_balance[:count])+list_to_balance[count:size_of_array]
            list_of_list_to_balance.append(final_list_to_append)
            list_of_list_to_balance.append(final_list_to_append[::-1])
        else:
            list_of_list_to_balance.append(list_to_balance)
        count+=1
    return list_of_list_to_balance

def get_dictionary_of_execution_times(lists_of_list_to_balance):
    avl_tree_execution_time_list = []
    rb_tree_execution_time_list = []
    splay_execution_time_list = []

    for indv_list_to_balance in lists_of_list_to_balance:
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
        splay_trees_time_difference = splay_trees_end_time - splay_trees_start_time
        splay_execution_time_list.append(splay_trees_time_difference.microseconds)

    dictionary_of_time_stamps = {
        "AVL Trees": avl_tree_execution_time_list,
        "Red Black Trees": rb_tree_execution_time_list,
        "Splay Trees": splay_execution_time_list,
    }
    return len(lists_of_list_to_balance), dictionary_of_time_stamps

def plot_graphs(size_of_lists_to_balance, dictionary_of_time_executions):
    for algorithm, time_list in dictionary_of_time_executions.items():
        plt.plot([i for i in range(0,size_of_lists_to_balance)], time_list, label = algorithm)
    plt.title('Comparison for time taken to insert into self balancing trees')
    plt.xlabel('Iteration count')
    plt.ylabel('Time taken for insertion in microseconds')
    plt.legend()
    plt.show()

def main():
    lists_of_list_to_balance = get_list_of_lists_to_balance()
    size_of_lists_to_balance, dictionary_of_time_executions = get_dictionary_of_execution_times(lists_of_list_to_balance)
    plot_graphs(size_of_lists_to_balance, dictionary_of_time_executions)

if __name__ == "__main__":
    main()