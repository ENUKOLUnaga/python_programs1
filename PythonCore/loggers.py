import logging
def even_sum(lst):
    logging.info("execute Even_sum() function")
    sum=0
    for i in lst:
        if i%2==0:
            sum+=i
    logging.info(" Even_sum() function return value")
    return sum
def main():
    logging.basicConfig(filename="log.txt",level=20)
    logging.info("Main() started")
    lst=list(map(int,input().split()))
    logging.info("Calling Even_sum() function")
    res=even_sum(lst)

    print(res)
main()
