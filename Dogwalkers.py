
def Range_calc():
    Dogs, Walkers = map(int, input().split())
    Dog_list = list(map(int,input().split()))
    Dog_list.sort()
    diff_arr = [Dog_list[i+1]-Dog_list[i] for i in range(Dogs-1)]
    diff_arr.sort(reverse=True)

    return Dog_list[-1] - Dog_list[0] - sum(diff_arr[:Walkers-1])


    
if __name__ == '__main__':
    T = int(input())
    while T:
        print(Range_calc())
        T -= 1










