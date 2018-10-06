import pandas as pd

batch= 'E7'

url_2_yr="https://contribute.geeksforgeeks.org/wp-content/uploads/timetable-1.xlsx"

index_col_2_yr="B.TECH. II Yr.(III SEMESTER TIMETABLE) ODD SEMESTER 2018(Combined) JIIT128(Effective from 17/07/2018)"

data=pd.read_excel(url_2_yr, index_col=index_col_2_yr)


#sperating cols

data.columns=[1,2,3,4,5,6,7,8,9]

data.columns.name=" "

#seprating days

mon=data.loc["MON":"TUE"].iloc[:-1]
tue=data.loc["TUE":"WED"].iloc[:-1]
wed=data.loc["WED":"THURS"].iloc[:-1]
thu=data.loc["THURS":"FRI"].iloc[:-1]
fri=data.loc["FRI":"SAT"].iloc[:-1]
sat=data.loc["SAT":].iloc[:-1]



#list of df
data2=[mon,tue,wed,thu,fri,sat]

final=data.dropna()
#data2
#final=data.dropna()
#final
#edit data frame here . make first row the column labels

rows=[]

#realgame
#move all to class and fns

for i in range (0,6):
    newlist=[]
    for j in range(1,10):
        new=data2[i][j].dropna()
        new2=new.str.contains(batch)
        if not ((new[new2]).empty):
            temp=new[new2].tolist()[0].replace("\n","")
            
            #comment to show subject code
            temp1=temp.find('(')
            temp2=temp.find(')')
            temp=temp[:temp1]+temp[temp2+1:]
            #comment to show subject code
            
            temp3=temp.find('/')
            temp=temp[:temp3]
            newlist.append(temp)
            #method 2
            #newlist.append(new[new2].tolist().replace('\n',''))
        else:
            newlist.append(" ")
    rows.append(newlist)


#final.append(new[new2])
#final

final=pd.DataFrame(rows,index=["Mon","Tue","Wed","Thu","Fri","Sat"],columns=data.iloc[0])
final.columns.name="Days/Time"

#final.to_csv("new.csv")
final


#To convert to pdf run following code



'''
tt=final.transpose()
tt
tt.to_csv("new.csv")
print("hey")
import convertapi

convertapi.api_secret = '33DyvMnOn3HicKWp'



result = convertapi.convert('pdf', { 'File': 'new.csv' })



# save to file
result.file.save('timetable.pdf')

'''
