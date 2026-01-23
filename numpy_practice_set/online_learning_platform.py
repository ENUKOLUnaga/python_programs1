import numpy as np
def onlinePlatformTracking(time):
    #total time spent for course
    total_time_for_course=time.sum(axis=0)
    print("total time spent for course: ",total_time_for_course)
    #average daily engagements exceeds threshold
    average_of_daily_engagement=time.mean(axis=0)
    print(average_of_daily_engagement)
    threshold=25
    exceed=np.where(average_of_daily_engagement>threshold)[0]
    print(exceed)
    #ranking the courses based on engagement
    rankings=np.argsort(average_of_daily_engagement)[::-1]
    print(rankings)
def main():
    time_spent=np.random.randint(0,60,size=(14,6))
    print(time_spent)
    onlinePlatformTracking(time_spent)
if __name__=="__main__":
    main()
