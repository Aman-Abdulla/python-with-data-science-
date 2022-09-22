num = int(input('enter a number'))

match num:
    case 1:
        print('sunday')
    case 2:
        print('monday')
    case 3:
        print('tuesday')
    case 4:
        print('wednesday')

    case _ :
        print('invalid data')
