def check_perfect(*args):
    
    for num in args:
        total = 0
        
        for i in range(1, num):
            if num % i == 0:
                total += i
        if total == num:
            print(f"{num} is a perfect number")
        else:
            print(f"{num} is not a perfect number")
            
check_perfect(6, 28, 12)
