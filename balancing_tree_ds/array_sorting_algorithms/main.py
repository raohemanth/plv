import random
import datetime
import matplotlib.pyplot as plt
from algorithms_implemented import bubblesort
from algorithms_implemented import insertionsort
from algorithms_implemented import mergesort
from algorithms_implemented import quicksort
from algorithms_implemented import selectionsort
from algorithms_implemented import shellsort

def get_list_of_lists_to_balance():
    size_of_array = 50
    list_of_list_to_balance = []
    number_of_runs = 100
    count = 0
    max_range_of_random_number=1000
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
    bubblesort_execution_time_list = []
    insertionsort_execution_time_list = []
    mergesort_execution_time_list = []
    quicksort_execution_time_list = []
    selectionsort_execution_time_list = []
    shellsort_execution_time_list = []

    for indv_list_to_balance in lists_of_list_to_balance:
        bubblesort_start_time = datetime.datetime.now()
        bubblesort.bubblesort(indv_list_to_balance)
        bubblesort_end_time = datetime.datetime.now()
        bubblesort_time_difference = bubblesort_end_time - bubblesort_start_time
        bubblesort_execution_time_list.append(bubblesort_time_difference.microseconds)

        insertionsort_start_time = datetime.datetime.now()
        insertionsort.insertion_sort(indv_list_to_balance)
        insertionsort_end_time = datetime.datetime.now()
        insertionsort_time_difference = insertionsort_end_time - insertionsort_start_time
        insertionsort_execution_time_list.append(insertionsort_time_difference.microseconds)

        mergesort_start_time = datetime.datetime.now()
        mergesort.merge_sort(indv_list_to_balance)
        mergesort_end_time = datetime.datetime.now()
        mergesort_time_difference = mergesort_end_time - mergesort_start_time
        mergesort_execution_time_list.append(mergesort_time_difference.microseconds)

        quicksort_start_time = datetime.datetime.now()
        quicksort.quicksort(indv_list_to_balance)
        quicksort_end_time = datetime.datetime.now()
        quicksort_time_difference = quicksort_end_time - quicksort_start_time
        quicksort_execution_time_list.append(quicksort_time_difference.microseconds)

        selectionsort_start_time = datetime.datetime.now()
        selectionsort.selection_sort(indv_list_to_balance)
        selectionsort_end_time = datetime.datetime.now()
        selectionsort_time_difference = selectionsort_end_time - selectionsort_start_time
        selectionsort_execution_time_list.append(selectionsort_time_difference.microseconds)
        
        shellsort_start_time = datetime.datetime.now()
        shellsort.shellSort(indv_list_to_balance)
        shellsort_end_time = datetime.datetime.now()
        shellsort_time_difference = shellsort_end_time - shellsort_start_time
        shellsort_execution_time_list.append(shellsort_time_difference.microseconds)

    dictionary_of_time_stamps = {
        "Bubble Sort": bubblesort_execution_time_list,
        "Insertion Sort": insertionsort_execution_time_list,
        "Merge Sort": mergesort_execution_time_list,
        "Quick Sort": quicksort_execution_time_list,
        "Selection Sort": selectionsort_execution_time_list,
        "Shell Sort": shellsort_execution_time_list,
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