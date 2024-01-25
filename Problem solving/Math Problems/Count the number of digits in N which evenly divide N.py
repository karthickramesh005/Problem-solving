# Given a number N. Count the number of digits in N which evenly divide N.

def count(N):
        temp = N
        count = 0
        while (temp != 0):
            # extract the last digit
            d = temp % 10;
            temp = temp//10;
            # check if d divides N evenly
            if d > 0 and N%d == 0:
              count+=1;
        
        return count;

n = int(input())

ans = count(n)
print(ans)
