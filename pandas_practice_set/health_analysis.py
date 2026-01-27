import pandas as pd
def healthAnalysis(df):
    df['timestamp']=pd.to_datetime(df['timestamp'])
    #Average heart rate per ward
    avg_heart_rate=df.groupby('ward')['heart_rate'].mean().reset_index()
    print(avg_heart_rate)
    # Get patients with sudden spikes
    df=df.sort_values(['patient_id','timestamp'])
    df['hr_diff']=df.groupby('patient_id')['heart_rate'].diff()
    print(df)
    df['sudden_spike']=df['hr_diff']>20
    patient_with_spike=df[df['sudden_spike']]['patient_id'].unique()
    print(patient_with_spike)
    #critical cases
    critical_case=(df['heart_rate']>=120)|(df['heart_rate']<=50)
    print(critical_case)

def main():
    df=pd.read_csv(r"C:\Users\ENKOL\PyCharmMiscProject\pandas_practice_set\health_dat.csv")
    healthAnalysis(df)

if __name__=="__main__":
    main()