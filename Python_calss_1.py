import time
while True:
    time1 = time.time()
    typingtest = input('The Quick Brown Fox Jumps Over The Lazy Dog: ')
    if typingtest == 'the quick brown fox jumps over the lazy dog':
        time2 = time.time()
        print(time2 - time1,'seconds')
    elif typingtest == 'The Quick Brown Fox Jumps Over The Lazy Dog':
        time2 = time.time()
        print(time2 - time1,'seconds')
    elif typingtest == 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG':
        time2 = time.time()
        time3 = time2 - time1
        print(f'''You have Cap Lock on. Right?!
But Anyway, Your Time is: {time3}''')
    elif typingtest == 'DevMode::True':
        print('you read the code ;)')
    print()