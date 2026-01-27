import pandas as pd
def performmanceSystem(data):
    df=pd.DataFrame(data)
    print(df)
    grouped_data=df.groupby('department')
    print(grouped_data.apply(lambda x:x))
    quarterly_avg=df.groupby(['department','quarter'])['performance_score'].mean().reset_index(name='avg_performance')
    print(quarterly_avg)
    #improving gradually 
    print(quarterly_avg.columns)
    pivot=quarterly_avg.pivot(index='department',columns='quarter',values='avg_performance')
    pivot=pivot.reindex(columns=['Q1','Q2','Q3','Q4'])
    improving=pivot.dropna().loc[(pivot['Q1']<pivot['Q2'])&(pivot['Q2']<pivot['Q3'])&(pivot['Q3']<pivot['Q4'])]
    print(improving.reset_index())
def main():
    data={
        "emp_id": [101, 102, 103, 104, 105, 106, 107, 108, 101, 102, 103, 104],
    "department": ["Sales", "HR", "Sales", "IT", "HR", "IT", "Sales", "IT", "Sales", "HR", "Sales", "IT"],
    "quarter": ["Q1", "Q1", "Q1", "Q1", "Q1", "Q1", "Q2", "Q2", "Q2", "Q2", "Q2", "Q2"],
    "performance_score": [85, 90, 78, 88, 92, 80, 87, 85, 90, 93, 82, 89]
    }
    performmanceSystem(data)

if __name__=="__main__":
    main()