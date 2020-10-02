import pandas
from sklearn.impute import KNNImputer 

filenames = ['X_trainData_AMK.csv','X_trainData_CAP.csv','X_trainData_CIP.csv','X_trainData_EMB.csv','X_trainData_INH.csv','X_trainData_KAN.csv','X_trainData_MOXI.csv','X_trainData_OFLX.csv','X_trainData_PZA.csv','X_trainData_RIF.csv','X_trainData_STR.csv']

output = ['../kNN_imputation/X_trainData_kNN_AMK.csv','../kNN_imputation/X_trainData_kNN_CAP.csv','../kNN_imputation/X_trainData_kNN_CIP.csv','../kNN_imputation/X_trainData_kNN_EMB.csv','../kNN_imputation/X_trainData_kNN_INH.csv','../kNN_imputation/X_trainData_kNN_KAN.csv','../kNN_imputation/X_trainData_kNN_MOXI.csv','../kNN_imputation/X_trainData_kNN_OFLX.csv','../kNN_imputation/X_trainData_kNN_PZA.csv','../kNN_imputation/X_trainData_kNN_RIF.csv','../kNN_imputation/X_trainData_kNN_STR.csv']

for index in range(len(filenames)):
    data = pandas.read_csv(filenames[index], usecols = [*range(222)])
    labels = pandas.read_csv(filenames[index], usecols = [222])
    imputer = KNNImputer(missing_values = -1, n_neighbors = 15)
    data = pandas.DataFrame(imputer.fit_transform(data),columns = data.columns)

    def threshold(value):
        if(float(value) < 0.5):
            return 0
        else:
            return 1


    data = data.applymap(threshold)
    data = pandas.concat([data,labels], axis = 1)
    data.to_csv(output[index], index=False)

