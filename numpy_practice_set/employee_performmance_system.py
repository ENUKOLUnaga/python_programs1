import numpy as np
def employeePerformmanceAnalysis(ratings):
    #normalize the data 
    normailsed_ratings=(ratings-ratings.min())/(ratings.max()-ratings.min())
    print(normailsed_ratings)
    #average rating per employee
    average_rating_per_employee=normailsed_ratings.mean(axis=1)
    print("Average rating per employee: ",average_rating_per_employee)
    #employees who are above the company mean
    company_mean=normailsed_ratings.mean()
    print(company_mean)
    high_performmers=np.where(average_rating_per_employee>company_mean)[0]
    print(high_performmers)
def main():
    #getting employee performmance ratings(1-5) for 100 employees
    employee_performmance_ratings=np.random.randint(1,6,size=(100,4))
    print(employee_performmance_ratings)
    employeePerformmanceAnalysis(employee_performmance_ratings)
if __name__=="__main__":
    main()