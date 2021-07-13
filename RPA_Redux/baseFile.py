from OdcesForms import *
from OdcesForms import IndiLog
from OdcesForms import AduAssess
from OdcesForms import ChiAssess
import time 
import testData
import pandas as pd 
pd.set_option("display.max_rows", 10, "display.max_columns", 100)
df = pd.read_csv('iCarolTestData.csv')
df = df.fillna(0)
from csv import reader 

y = 0

SeleniumAbid.driver.set_page_load_timeout(30)
            
#Main Login Page
SeleniumAbid.driver.get("https://ccpdata.org/ccp2field/")
            
#UserName and Password 
SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtLogin").send_keys("abakhtiyar@alterhealthgroup.com")
SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtPassword").send_keys("Alter123!")
SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_btnSubmit").click()

def workerID(df, y):
    WorkerNum = df.iloc[y]["WorkerNum"]
    if WorkerNum == 162047:
        df.at[y, "WorkerNum"] = 1234
        print (df.iloc[y]["WorkerNum"])
    if WorkerNum == 162458:
        df.at[y, "WorkerNum"] = 10053
       
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162486:
        df.at[y, "WorkerNum"] = 9924
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162456:
        df.at[y, "WorkerNum"] = 9815
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162490:
        df.at[y, "WorkerNum"] = 9928
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162494:
        df.at[y, "WorkerNum"] = 10469
        
        df.to_csv('ICarolTestData.csv', index = False)
    elif WorkerNum == 163489:
        df.at[y, "WorkerNum"] = 10468
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162523:
        df.at[y, "WorkerNum"] = 9812
        EmployID = 9812 #TCochran
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162485:
        df.at[y, "WorkerNum"] = 9923
        EmployID = 9923 #DDixon
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162478:
        df.at[y, "WorkerNum"] = 9867
        EmployID = 9867 #KDOonovan
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162489:
        df.at[y, "WorkerNum"] = 9927
        EmployID = 9927 #FEchols
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162482:
        df.at[y, "WorkerNum"] = 9921
        EmployID = 9921 #RFelleke
       
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 163490:
        df.at[y, "WorkerNum"] = 10467
        EmployID = 10467 #JFlores
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 163491:
        df.at[y, "WorkerNum"] = 9916
        EmployID = 9916 #SFord
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162460: 
        df.at[y, "WorkerNum"] = 9858
        EmployID = 9858 #JGarcia
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162453:
        df.at[y, "WorkerNum"] = 9813
        EmployID = 9813 #IGutierrez
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162476:
        df.at[y, "WorkerNum"] = 10198
        EmployID = 10198 #PGutierrez
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162455:
        df.at[y, "WorkerNum"] = 9814
        EmployID = 9814 #FGuzman
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 163492:
        df.at[y, "WorkerNum"] = 11107
        EmployID = 11107 #IHidalgo
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 163493: 
        df.at[y, "WorkerNum"] = 9915
        EmployID = 9915 #SHighbaugh
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162492: 
        df.at[y, "WorkerNum"] = 9931
        EmployID = 9931 #JHinshilwood
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162483:
        df.at[y, "WorkerNum"] = 162483
        EmployID = 9920
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 163494:
        df.at[y, "WorkerNum"] = 11280
        EmployID = 11280
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 163495:
        df.at[y, "WorkerNum"] = 10678
        EmployID = 10678 #DMarciano
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum ==  162454:
        df.at[y, "WorkerNum"] = 9863
        EmployID = 9863
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162477:
        df.at[y, "WorkerNum"] = 9864
        EmployID = 9864
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 163496:
        df.at[y, "WorkerNum"] = 9869
        EmployID = 9869
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162475:
        df.at[y, "WorkerNum"] = 9862
        EmployID = 9862
       
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 163497:
        df.at[y, "WorkerNum"] = 11106
        EmployID = 11106
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162493:
        df.at[y, "WorkerNum"] = 10466
        EmployID = 10466
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162474:
        df.at[y, "WorkerNum"] = 9861
        EmployID = 9861
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162488:
        df.at[y, "WorkerNum"] = 9926
        EmployID = 9926
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162473:
        df.at[y, "WorkerNum"] = 9859
        EmployID =  9859
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162457:
        df.at[y, "WorkerNum"] = 9929
        EmployID = 9929 #MSallus
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162481:
        df.at[y, "WorkerNum"] = 9917
        EmployID = 9917 #MSanders
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162459:
        df.at[y, "WorkerNum"] = 9934
        EmployID = 9934
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162484:
        df.at[y, "WorkerNum"] = 10465
        EmployID = 10465
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162479:
        df.at[y, "WorkerNum"] = 9869
        EmployID = 9868
       
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162480:
        df.at[y, "WorkerNum"] = 9914
        EmployID = 9914    
        
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 162491:
        df.at[y, "WorkerNum"] = 9933
        
        print (df.iloc[y]["WorkerNum"])
        EmployID = 9933
    elif WorkerNum == 162487:
        df.at[y, "WorkerNum"] = 9925
        EmployID = 9925
       
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 163498:
        df.at[y, "WorkerNum"] = 9816
        EmployID = 9816
        print (df.iloc[y]["WorkerNum"])
    elif WorkerNum == 163499:
        df.at[y, "WorkerNum"] = 11181
        EmployID = 11181  
        print (df.iloc[y]["WorkerNum"])
with open('ICarolTestData.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    if header != None:
        for row in csv_reader:  
            workerID(df, y)
                
            if int(df.iloc[y]["Report Version"]) == 60404:
                IndiLog.start(y, df)
                print("done " + str(df.iloc[y]["Report Version"]))
            elif int(df.iloc[y]["Report Version"]) == 60433:
                AduAssess.start(y, df)
                print("done " + str(df.iloc[y]["Report Version"]))
            elif int(df.iloc[y]["Report Version"]) == 60434:
                ChiAssess.start(y, df)
                print("done " + str(df.iloc[y]["Report Version"]))
            time.sleep(15)
            #counter+=1
            print("done " + str(df.iloc[y]["Report Version"]))
            y += 1