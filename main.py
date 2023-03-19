# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    threads = [(i, 0) for i in range(n)]
    for i in range(m):
        job = data[i]
        next_thread = min(threads, key = lambda x: (x[1], x[0]))
        output.append((next_thread[0], next_thread[1]))
        threads.remove(next_thread)
        threads.append((next_thread[0], next_thread[1] + job))
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i in range(m):
        print(result[i][0], result[i][1])


if __name__ == "__main__":
    main()
