import pandas as pd 
#import baseFile
pd.set_option("display.max_rows", 10, "display.max_columns", 100)
df = pd.read_csv('iCarolTestData.csv')
df = df.fillna(0)
print(df)

y=0

EmployID = None

##Employee Relation Loop##

WorkerNum = 0
if WorkerNum == 162047:
    EmployID == 1234
if WorkerNum == 162458:
    EmployID = 10053 #CAguayo 
elif WorkerNum == 162486:
    EmployID = 9924 #JAyinala
elif WorkerNum == 162047:
    EmployID = 9815 #MBayona
elif WorkerNum == 163490:
    EmployID = 9928 #VBostic 
elif WorkerNum == 162594:
    EmployID = 10469 #SBrown 
elif WorkerNum == 163489:
    EmployID = 10468 #ECampos 
elif WorkerNum == 162523:
    EmployID = 9812 #TCochran 
elif WorkerNum == 162485:
    EmployID = 9923 #DDixon 
elif WorkerNum == 162478:
    EmployID = 9867 #KDOonovan 
elif WorkerNum == 162489:
    EmployID = 9927 #FEchols 
elif WorkerNum == 162482:
    EmployID = 9921 #RFelleke
elif WorkerNum == 163490:
    EmployID = 10467 #JFlores 
elif WorkerNum == 163491:
    EmployID = 9916 #SFord 
elif WorkerNum == 162460: 
    EmployID = 9858 #JGarcia 
elif WorkerNum == 162453:
    EmployID = 9813 #IGutierrez 
elif WorkerNum == 162476:
    EmployID = 10198 #PGutierrez 
elif WorkerNum == 162455:
    EmployID = 9814 #FGuzman 
elif WorkerNum == 163492:
    EmployID = 11107 #IHidalgo 
elif WorkerNum == 163493: 
    EmployID = 99156 #SHighbaugh 
elif WorkerNum == 162491: 
    EmployID = 9931 #JHinshilwood 
elif WorkerNum == 162483:
    EmployID = 9920
elif WorkerNum == 163494:
    EmployID = 11280
elif WorkerNum == 161576:
    EmployID = 10678
elif WorkerNum == 163495:
    EmployID = 9863
elif WorkerNum == 162454:
    EmployID = 9864
elif WorkerNum == 162477:
    EmployID = 9862
elif WorkerNum == 163496:
    EmployID = 9869
elif WorkerNum == 162475:
    EmployID = 9869    
elif WorkerNum == 163497:
    EmployID = 11106
elif WorkerNum == 162493:
    EmployID = 10466
elif WorkerNum == 162474:
    EmployID = 9861
elif WorkerNum == 162488:
    EmployID =  9926
elif WorkerNum == 162473:
    EmployID = 9859
elif WorkerNum == 162457:
    EmployID = 9929
elif WorkerNum == 162481:
    EmployID = 9917
elif WorkerNum == 162459:
    EmployID = 9934
elif WorkerNum == 162484:
    EmployID = 10465
elif WorkerNum == 162479:
    EmployID = 9868
elif WorkerNum == 162480:
    EmployID = 9914    
elif WorkerNum == 162491:
    EmployID = 9933
elif WorkerNum == 162487:
    EmployID = 9925
elif WorkerNum == 163498:
    EmployID = 9816
elif WorkerNum == 163499:
    EmployID = 11181	


################################Test Data#####################################int
formName = df.iloc[y]["Report Version"]
numofPeople = df.iloc[y]["Number of People"]
numofVisit = df.iloc[y]["Visit Number"]
visitDur = 15 #df.iloc[2]["Visit Duration"]
ageGen = {
    'm' : [24, 24, 23],
    'f' : [25],
    't' : []
    }
raceEth = df.iloc[y]["Race/Ethnicity"]
langspoke = df.iloc[y]["Primary Language"]
otherLang = df.iloc[y]["Other Language"]
disCode = df.iloc[y]["Disability"]
location = 'permanent home'
otherLoc = 'Girlfriends house'
tempMinor = 'YES'
permMinor = 'YES'
#minor = df.iloc[1]["Minor"] 
crisis = df.iloc[y]["Crisis Line"] 
risk = df.iloc[y]["Risk Categories"]
riskCode = risk.split(";")
numofReacs = str(df.iloc[y]["NumofEventReacs"])
reactions = ['irritable', 'anxious', 'headaches', 'eating problems']
info = ['reactions', 'this crisis', 'reducing', 'mutual', 'doing']
otherInfo = 'how to apply for work'
materials = True
referrals = ['mental', 'crisis', 'substance', 'other']
otherRefs = str(df.iloc[y]["Other Referrals"])
lead = 'YES'

adultAge = str(df.iloc[y]["Adult Age"])
adultGen = str(df.iloc[y]["Adult Gender"])
aduAssessQ = {
    1:5,
    2:5,
    3:5,
    4:5,
    5:5,
    6:5,
    7:5,
    8:5,
    9:5,
    10:5,
    11:5,
    12:'YES',
    13:'NO',
    14:'YES'
    }
refAccept = True

parPres = True
leadPres = 'YES' 
childAge = str(df.iloc[y]["Child Age"])
childGen = str(df.iloc[y]["Child Gender"])
grLevel = int(df.iloc[y]["Grade Level"])

chiAssessQ = {
    1:2,
    2:4,
    3:4,
    4:3,
    5:1,
    6:2,
    7:3,
    8:3,
    9:3,
    10:2,
    11:4,
    12:4,
    13:1,
    14:2,
    15:3,
    16:1,
    17:2,
    18:3,
    19:4,
    20:4,
    21:'NO',
    22:'NO',
    23:'NO',
    24:'NO'     
    }

ChiAccept = df.iloc[y]["Child Referral Acceptance"]
ParAccept = df.iloc[y]["Parent Referral Acceptance"]
################################Test Data#####################################

