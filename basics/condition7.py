salary =int(input('Enter your Salary =>'))

if salary > 100000:
    da = salary/3.5
    hra= salary/9.1
    final = da + hra + salary
    print('the final salary is',final)
elif salary > 80000:
     da = salary/3.2
     hra= salary/9
     final = da + hra + salary
     print('the final salary is',final)    
elif salary > 60000:
     da = salary/2.8
     hra= salary/9
     final = da + hra + salary
     print('the final salary is',final)
elif salary > 50000:
     da = salary/2.5
     hra= salary/8
     final = da + hra + salary
     print('the final salary is',final)
elif salary > 40000:
     da = salary/2.5
     hra= salary/7.7
     final = da + hra + salary
     print('the final salary is',final)
elif salary > 30000:
     da = salary/2.2
     hra= salary/8
     final = da + hra + salary
     print('the final salary is',final)
elif salary > 20000:
     da = salary/2.2
     hra= salary/7
     final = da + hra + salary
     print('the final salary is',final)
elif salary > 10000: 
     da = salary/2.2
     hra= salary/6
     final = da + hra + salary
     print('the final salary is',final)
