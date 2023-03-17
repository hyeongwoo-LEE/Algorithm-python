
#n,m = map(int, input().split())
n,m = 4,6
#arr = list(map(int,input().split()))
arr = [19,15,10,17]

def b_search(arr, target):

    start = 0
    end = max(arr)

    while start <= end:

        total = 0
        mid = (start+end)//2
        for i in arr:
            if i >mid:
                total += (i-mid)

        if total == target:
            return mid
        # 왼쪽
        elif total < target:
            end = mid-1
        # 오른쪽
        else:
            start = mid+1

    return None



print(b_search(arr,m))