import numpy as np
def weatherAnalysis(temparature):
    #daily maximum and minimum temparture
    min=temparature.min(axis=1)
    print("Daily Minimum temparature: ",min)
    max=temparature.max(axis=1)
    print("Daily Maximum temparature: ",max)
    #largest temparature variation
    day_variation=max-min
    print("Day with largest variation in temparature: ",np.argmax(day_variation))
    #Replace outliers beyond ±2 standard deviations with the mean temperature
    standard_deviation=np.std(day_variation)
    mean=np.mean(day_variation)
    lower_bound=mean-2*standard_deviation
    upper_bound=mean+2*standard_deviation
    temp=temparature.copy()
    outliers=(temp<lower_bound)|(temp>upper_bound)
    temp[outliers]=mean
    print(mean)
    print(standard_deviation)
    print(np.sum(outliers))
def main():
    weather_station=np.random.randint(10,40,size=(7,24))
    print(weather_station)
    weatherAnalysis(weather_station)
if __name__=="__main__":
    main()
