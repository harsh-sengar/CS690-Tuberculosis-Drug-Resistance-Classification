import csv

filenames = ['X_trainData_AMK.csv','X_trainData_CAP.csv','X_trainData_CIP.csv','X_trainData_EMB.csv','X_trainData_INH.csv','X_trainData_KAN.csv','X_trainData_MOXI.csv','X_trainData_OFLX.csv','X_trainData_PZA.csv','X_trainData_RIF.csv','X_trainData_STR.csv']

output = ['../row_deletion/X_trainData_removal_AMK.csv','../row_deletion/X_trainData_removal_CAP.csv','../row_deletion/X_trainData_removal_CIP.csv','../row_deletion/X_trainData_removal_EMB.csv','../row_deletion/X_trainData_removal_INH.csv','../row_deletion/X_trainData_removal_KAN.csv','../row_deletion/X_trainData_removal_MOXI.csv','../row_deletion/X_trainData_removal_OFLX.csv','../row_deletion/X_trainData_removal_PZA.csv','../row_deletion/X_trainData_removal_RIF.csv','../row_deletion/X_trainData_removal_STR.csv']

for i in range(len(filenames)):
    in_file = open(filenames[i])
    reader = csv.reader(in_file, delimiter=',')
    out_file = open(output[i],'w')
    writer = csv.writer(out_file, delimiter=',')
    for row in reader:
        flag=0
        for j in range(len(row)):
            if(row[j] == '-1'):
                flag=1
                break


        if (flag == 0):
            writer.writerow(row)


    in_file.close()
    out_file.close()

