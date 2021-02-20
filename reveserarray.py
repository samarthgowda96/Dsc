def reverses(arr):
    return arr.reverse()


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    m=map(str,arr)
  
    print(' '.join(m))
    
    
    
