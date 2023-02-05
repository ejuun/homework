N = int(input())
def collatz(N):
    cnt = 0
    while True:
        if cnt == 500:
            return print(-1)
        
        if N == 1:
            return print(cnt)

        if N % 2 == 1 :
            N = (N * 3) +1
            cnt += 1
        else:
            N = N / 2
            cnt += 1

# collatz(N)

# collatz(6)  # => 8
# collatz(16)  # => 4
# collatz(27)  # => 111
# collatz(626331)  # => -1
