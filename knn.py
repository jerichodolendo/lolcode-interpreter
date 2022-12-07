"""
Dolendo, Jericho Paolo T.
2020-03010
K Nearest Neighbor
170 X-1L
"""
import math

# gets user input for K value
k = int(input("Please enter K value: "))

# reads data input from a .csv file
with open('diabetes.csv', 'r') as f:
    content_one = f.read().splitlines()
    data = []

    # appends each line of data into an array
    for i in content_one:
        temp_one = i.split(",")
        temp_one = [float(j) for j in temp_one]
        data.append(temp_one)
    
# function that returns computed knn classification of each line of data
def get_knn(x):
    # gets user input of k value
    global k
    answers = []

    # computes for distance of each x to v
    for i in data:
        sum = 0
        # gets summation of squared difference of Xi and Vi
        for j in range(len(i)-1):
            sum += (x[j] - i[j])**2
        sum = math.sqrt(sum)
        # appends each result to answers list
        answers.append([sum, i])

    # sorts answers based on distance
    answers.sort(key=lambda x:x[0])
    answers = answers[:k]
     
    return answers

# reads x vectors from .in file
with open('input.in', 'r') as f:
    content_two = f.read().splitlines()

    # writes results into output.txt file
    with open('output.txt', 'w') as fp:
        """
            calls function get_knn to compute for k nearest neigbors
            for each input from .in file
        """
        for i in content_two:
            frequency = {}
            temp = i.split(",")
            temp = [float(j) for j in temp]
            answer = get_knn(temp)

            # for loop that gets frequency of its classification
            for j in answer:
                mode = j[-1][-1]
                if mode in frequency:
                    frequency[mode] += 1
                else:
                    frequency[mode] = 1

            # gets classification of x 
            classification = max(frequency, key=frequency.get)
            temp.append(classification)

            print(temp)
            for j in answer:
                print(j)
            print("")

            # writes all results in output.txt
            for l in range(len(temp)-1):
                fp.write(str(temp[l]) + ", ")
            
            # writes classification of an input vector
            fp.write(str(temp[-1]) + "\n")
    