import numpy as np
def healthAnalysis(heart_rate):
    print(heart_rate)
    #hourly average heart rating
    hourly_avg=heart_rate.mean(axis=0)
    print(hourly_avg)
    #abnormal readings
    abnormal=(heart_rate<60)|(heart_rate>100)
    abnormal_values=heart_rate[abnormal]
    print(abnormal_values)
    #replace missing values with forward fill
    for i in range(heart_rate.shape[0]):
        for j in range(1,heart_rate.shape[1]):
            if np.isnan(heart_rate[i,j]):
                heart_rate[i,j]=heart_rate[i,j-1]
    print(heart_rate)

def main():
    heart_rate=np.random.randint(50,120,size=(60,24))
    healthAnalysis(heart_rate)
if __name__=="__main__":
    main()