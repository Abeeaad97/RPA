from OdcesForms import SeleniumAbid
import testData
import pandas as pd 

#driver = webdriver.Chrome("C:/Users/Abid B/Odces_RPA/Drivers/chromedriver.exe")

#Determine the visit type
def visitType (counter, data):
    print(data.iloc[counter]["Number of People"])
    if data.iloc[counter]["Number of People"] == '1':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitTypeCode_0").click()
    elif data.iloc[counter]["Number of People"] == '2':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitTypeCode_1").click()
    elif data.iloc[counter]["Number of People"] == '3': 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceolder1_rdlVisitTypeCode_2").click()
    elif data.iloc[counter]["Number of People"] == '4': 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitTypeCode_3").click()
    elif data.iloc[counter]["Number of People"] == '5': 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitTypeCode_4").click()
    elif data.iloc[counter]["Number of People"] == '6 or more':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitTypeCode_5").click()

#determine the visit number 
def visitNumber (data, counter):
    print(data.iloc[counter]["Visit Number"])
    if str(data.iloc[counter]["Visit Number"]) == 'First Visit':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_0").click()
    elif str(data.iloc[counter]["Visit Number"]) == 'Second Visit':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_1").click() 
    elif str(data.iloc[counter]["Visit Number"]) == 'Third Visit':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_2").click()
    elif str(data.iloc[counter]["Visit Number"]) == 'Fourth Visit': 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_3").click()
    elif str(data.iloc[counter]["Visit Number"]) == 'Fifth Visit':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlVisitNumberCode_4").click()   
        
def visitDuration(data, counter):
    if int(data.iloc[counter]["Visit Duration"]) >= 15 and int(data.iloc[counter]["Visit Duration"]) <= 29:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlDurationCode_0").click()
    elif int(data.iloc[counter]["Visit Duration"]) >= 30 and int(data.iloc[counter]["Visit Duration"]) <= 44:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlDurationCode_1").click()
    elif int(data.iloc[counter]["Visit Duration"]) >= 45 and int(data.iloc[counter]["Visit Duration"]) <= 59:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlDurationCode_2").click()
    elif int(data.iloc[counter]["Visit Duration"]) >= 60:   
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlDurationCode_3").click()
        

def MaleAge(data, counter):
    if int(data.iloc[counter]["MalePre"]) > 0:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtMalePreschool").send_keys(int(data.iloc[counter]["MalePre"])) 
    if int(data.iloc[counter]["MaleChi"]) > 0:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtMaleChild").send_keys(int(data.iloc[counter]["MaleChi"]))
    if int(data.iloc[counter]["MaleAdo"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtMaleAdolescent").send_keys(int(data.iloc[counter]["MaleAdo"]))
    if int(data.iloc[counter]["MaleAdu"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtMaleAdult18").send_keys(int(data.iloc[counter]["MaleAdu"]))
    if int(data.iloc[counter]["MaleOldAdu"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtMaleAdult40").send_keys(int(data.iloc[counter]["MaleOldAdu"]))
    if int(data.iloc[counter]["MaleSen"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtMaleAdult65").send_keys(int(data.iloc[counter]["MaleSen"]))
    
def FemaleAge(data, counter):
    if int(data.iloc[counter]["FemalePre"]) > 0:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtFemalePreschool").send_keys(int(data.iloc[counter]["FemalePre"])) 
    if int(data.iloc[counter]["FemaleChi"]) > 0:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtFemaleChild").send_keys(int(data.iloc[counter]["FemaleChi"]))
    if int(data.iloc[counter]["FemaleAdo"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtFemaleAdolescent").send_keys(int(data.iloc[counter]["FemaleAdo"]))
    if int(data.iloc[counter]["FemaleAdu"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtFemaleAdult18").send_keys(int(data.iloc[counter]["FemaleAdu"]))
    if int(data.iloc[counter]["FemaleOldAdu"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtFemaleAdult40").send_keys(int(data.iloc[counter]["FemaleOldAdu"]))
    if int(data.iloc[counter]["FemaleSen"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtFemaleAdult65").send_keys(int(data.iloc[counter]["FemaleSen"]))
        
def TransAge(data, counter):
    if int(data.iloc[counter]["TransPre"]) > 0:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtTransgenderPreschool").send_keys(int(data.iloc[counter]["TransPre"])) 
    if int(data.iloc[counter]["TransChi"]) > 0:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtTransgenderChild").send_keys(int(data.iloc[counter]["TransChi"]))
    if int(data.iloc[counter]["TransAdo"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtTransgenderAdolescent").send_keys(int(data.iloc[counter]["TransAdo"]))
    if int(data.iloc[counter]["TransAdu"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtTransgenderAdult18").send_keys(int(data.iloc[counter]["TransAdu"]))
    if int(data.iloc[counter]["TransOldAdu"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtTransgenderAdult40").send_keys(int(data.iloc[counter]["TransOldAdu"]))
    if int(data.iloc[counter]["TransSen"]) > 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtTransgenderAdult65").send_keys(int(data.iloc[counter]["TransSen"]))       
            

def raceEthnicity(data, counter): 
    raceEthnicity = data.iloc[counter]["Race/Ethnicity"]
    raceEth = raceEthnicity.split(";")
    for x in raceEth:
        if str(x) == 'American Indian/Alaska Native':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_0").click()
        elif str(x) == 'Asian':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_1").click()
        elif str(x) == 'Black or African American':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_2").click()
        elif str(x) == 'Native Hawaiian/ Other Pacific Islander':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_3").click()
        elif str(x) == 'White':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_4").click()
        elif str(x) == 'Hispanic or Latino':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_5").click()

def lang(data, counter):
    if str(data.iloc[counter]["Primary Language"]) == 'English':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlPrimaryLanguageCode_0").click()
    elif str(data.iloc[counter]["Primary Language"]) == 'Spanish':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlPrimaryLanguageCode_1").click()
    elif str(data.iloc[counter]["Primary Language"]) == 'Other':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlPrimaryLanguageCode_2").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtPrimaryLanguageOther").send_keys(data.iloc[counter]["Other Language"])
        
def dis(data, counter):
    disabilityCode = data.iloc[counter]["Disability"]
    disCode = disabilityCode.split(";")
    #print(disCode)
    for x in disCode:
        if x == 'Physical (mobility  visual  hearing  medical  etc.)':
            print (x)
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblDisabilityCodes_0").click()
    #SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblDisabilityCodes_0").click()
        elif x  == 'Intellectual/Cognitive (learning disability  developmental delay  etc.)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblDisabilityCodes_1").click()
    #SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblDisabilityCodes_1").click()
        elif x  == 'Mental Health/Substance Abuse (psychiatric  substance dependence  etc.)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblDisabilityCodes_2").click()
    #SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblDisabilityCodes_2").click()

def loca(data, counter):
    if str(data.iloc[counter]["Location"]) == 'school or child care (all ages through college)':    
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_0").click()
    elif str(data.iloc[counter]["Location"]) == 'community center (e.g.  recreation club)':    
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_1").click()
    elif str(data.iloc[counter]["Location"]) == 'provider site/mental health agency (agency involved with Crisis Counseling Assistance and Training Program [CCP])':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_2").click()
    elif str(data.iloc[counter]["Location"]) ==  'workplace (workplace of the disaster survivor and/or first responder)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_3").click()
    elif str(data.iloc[counter]["Location"]) == 'disaster recovery center (e.g.  Federal Emergency Management Agency [FEMA]  American Red Cross)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_4").click()
    elif str(data.iloc[counter]["Location"]) == 'place of worship (e.g.  church  synagogue  mosque)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_5").click()
    elif str(data.iloc[counter]["Location"]) == 'retail (e.g.  restaurant  mall  shopping center  store)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_6").click()
    elif str(data.iloc[counter]["Location"]) == 'public place/event (e.g.  street  sidewalk  town square  fair  festival  sports)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_7").click()
    elif str(data.iloc[counter]["Location"]) == 'temporary home (including friend or family homes  group homes  shelters  apartments  trailers  and other dwellings)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_8").click()
        if str(data.iloc[counter]["TempMinor"]) == 'YES':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_9").click()
    elif data.iloc[counter]["Location"] == 'permanent home':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_10").click()
        if str(data.iloc[counter]["PermMinor"]) == 'YES': 
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_11").click()
    elif data.iloc[counter]["Location"] == 'phone counseling (15 minutes or longer)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_12").click()
        if str(data.iloc[counter]["Crisis Line"]) == 'YES':        
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_13").click()
    elif data.iloc[counter]["Location"] == 'medical center (e.g.  doctor  dentist  hospital  mental health or substance abuse specialty center)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_14").click()
    elif data.iloc[counter]["Location"] == 'other':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_15").click()
        if data.iloc[counter]["Other Location"] != '0.0':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtServiceLocationOther").send_keys(data.iloc[counter]["Other Location"])
        
def risks(data, counter):
    risk = data.iloc[counter]["Risk Categories"]
    riskCode = risk.split(";")
    for x in riskCode:
        if x == 'family missing/dead':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_0").click()
        elif x == 'friend missing/dead':        
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_1").click()
        elif x == 'pet missing/dead':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_2").click()
        elif x == 'home damaged or destroyed':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_3").click()
        elif x == 'vehicle or major property loss':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_4").click()
        elif x == 'other financial loss':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_5").click()
        elif x == 'disaster unemployed (self or household member)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_6").click()
        elif x == 'injured or physically harmed (self or household member)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_7").click()
        elif x == 'life was threatened (self or household member)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_8").click()
        elif x == 'witnessed death/injury (self or household member)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_9").click()
        elif x == 'assisted with rescue/recovery (self or household member)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_10").click()
        elif x == 'had to change schools':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_11").click()
        elif x == 'prolonged separation from family':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_12").click()
        elif x == 'evacuated quickly with no time to prepare':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_13").click()
        elif x == 'displaced from home 1 week or more':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_14").click()
        elif x == 'sheltered in place or sought shelter due to immediate threat of danger':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_15").click()
        elif x == 'past substance use/mental health problem':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_16").click()
        elif x == 'preexisting physical disability':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_17").click()
        elif x == 'past trauma':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRiskCodes_18").click()

def eventreac(data, counter):
    
    
    if str(data.iloc[counter]["NumofEventReacs"]) == '1':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlEventParticipantCode_0").click()
    elif str(data.iloc[counter]["NumofEventReacs"]) == '2':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlEventParticipantCode_1").click()
    elif str(data.iloc[counter]["NumofEventReacs"]) == '3':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlEventParticipantCode_2").click()
    elif str(data.iloc[counter]["NumofEventReacs"]) == '4':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlEventParticipantCode_3").click()
    elif str(data.iloc[counter]["NumofEventReacs"]) == '5':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlEventParticipantCode_4").click()
    elif str(data.iloc[counter]["NumofEventReacs"]) == '6 or more':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlEventParticipantCode_5").click()
        
    BehavioralReacs = str(data.iloc[counter]["Event Reactions - BEHAVIORAL"])
    BevReacs = BehavioralReacs.split(";")
    for x in BevReacs:
        if x == 'extreme change in activity level':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblBehavioralCodes_0").click()
        elif x == 'excessive drug or alcohol use':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblBehavioralCodes_1").click()
        elif x == 'isolation/withdrawal':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblBehavioralCodes_2").click()
        elif x == 'on guard/hypervigilant':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblBehavioralCodes_3").click()
        elif x == 'agitated/jittery/shaky':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblBehavioralCodes_4").click()
        elif x == 'violent or dangerous behavior':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblBehavioralCodes_5").click()
        elif x == 'acts younger than age (children or youth)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblBehavioralCodes_6").click()
    EmotionalReacs = str(data.iloc[counter]["Event Reactions - EMOTIONAL"])
    EmoReacs = EmotionalReacs.split(";")
    for x in EmoReacs:
        if x == 'sadness  tearful':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblEmotionalCodes_0").click()
        elif x == 'irritable  angry':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblEmotionalCodes_1").click()
        elif x == 'anxious  fearful':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblEmotionalCodes_2").click()
        elif x == 'despair  hopeless':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblEmotionalCodes_3").click()
        elif x == 'feelings of guilt/shame':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblEmotionalCodes_4").click()
        elif x == 'numb  disconnected':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblEmotionalCodes_5").click()
    PhysicalReacs = str(data.iloc[counter]["Event Reactions - PHYSICAL"])
    PhyReacs = PhysicalReacs.split(";")
    for x in PhyReacs:          
        if x == 'headaches':   
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblPhysicalCodes_0").click()
        elif x == 'stomach problems':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblPhysicalCodes_1").click()
        elif x == 'difficulty falling or staying asleep':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblPhysicalCodes_2").click()
        elif x == 'eating problems':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblPhysicalCodes_3").click()
        elif x == 'worsening of health problems':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblPhysicalCodes_4").click()
        elif x == 'fatigue exhaustion':
            SeleniumAbid.driver.find_element_by_if("ContentPlaceHolder1_cblPhysicalCodes_5").click()
    CognitiveReacs = str(data.iloc[counter]["Event Reactions - COGNITIVE"])
    CogReacs = CognitiveReacs.split(";")
    for x in CogReacs:
        if x == 'distressing dreams nightmares':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblCognitiveCodes_0").click()
        elif x == 'intrusive thoughts images':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblCognitiveCodes_1").click()
        elif x == 'difficulty concentrating':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblCognitiveCodes_2").click()
        elif x == 'difficulty remembering things':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblCognitiveCodes_3").click()
        elif x == 'difficulty making decisions':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblCognitiveCodes_4").click()
        elif x == 'preoccupied with death/destruction':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblCognitiveCodes_5").click()
            
    if str(data.iloc[counter]["Event Reaction - Coping"]) == 'If there are no participants experiencing the above event reactions please check this box':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cbCopingWell").click()
        
        
def focus(data, counter):
    
    focusInformation = data.iloc[counter]["Information Given"]
    focInfo = focusInformation.split(";")
    for x in focInfo:
        if str(x) == 'reactions to disaster':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblInformationAboutCodes_0").click()
        elif str(x) == 'community resources':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblInformationAboutCodes_1").click()
        elif str(x) == 'this crisis counseling program':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblInformationAboutCodes_2").click()

    focusTips = data.iloc[counter]["Tips"]
    focTips = focusTips.split(";")
    for x in focTips:
        if str(x) == 'reducing negative thoughts':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblTipsForCodes_0").click()
        elif str(x) == 'managing physical and emotional reactions (e.g.  breathing techniques)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblTipsForCodes_1").click()
        elif str(x) == 'doing positive things':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblTipsForCodes_2").click()
        elif str(x) == 'problem solving':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblTipsForCodes_3").click()
            
    focusHealth = data.iloc[counter]["Healthy Connections"]
    focHealth = focusHealth.split(";")
    for x in focHealth:
        if str(x) == 'mutual support/building social networks':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblHealthyConnectionCodes_0").click()
        elif str(x) == 'participating in community action':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblHealthyConnectionCodes_1").click()      
        elif str(x) == 'other':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtFocusOther").send_keys(x)
        
def material(data, counter):
    if str(data.iloc[counter]["Materials"]) == "Yes":
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlMaterialProvidedCode_0").click()
    else:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlMaterialProvidedCode_1").click()

def referral(data, counter):
    referralsGiven = data.iloc[counter]["Referrals"]
    refGiv = referralsGiven.split(";")
    if len(refGiv) == 0: 
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cbNoReferral").click()
    else:
        for x in refGiv:
            if str(x) == 'crisis counseling program services (e.g.  group counseling  referral to team leader  follow-up visit)':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblReferralCodes_0").click()
            elif str(x) == 'mental health services (e.g.  professional  longer-term counseling  treatment  behavioral  or psychiatric services)':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblReferralCodes_1").click()
            elif str(x) == 'substance abuse services (e.g.  professional  behavioral or medical treatment or self-help groups  such as Alcoholics Anonymous or Narcotics Anonymous)':
               SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblReferralCodes_2").click()
            elif str(x) == 'community services (e.g.  FEMA  loans  housing  employment  social services)':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblReferralCodes_3").click()
            elif str(x) == 'resources for those with disabilities  or other access or functional needs':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblReferralCodes_4").click()
            elif str(x) == 'other':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblReferralCodes_5").click()
                if x != '0.0':
                    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtReferralOther").send_keys(str(x))
            
def start(y, df):
    counter = y
    data = df
    SeleniumAbid.driver.find_element_by_id("UCSideNav_HyperLink29").click()   
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtEmployeeNumber1").send_keys(str(data.iloc[y]["WorkerNum"]))
    visitType(counter, data)
    visitNumber(data, counter)
    visitDuration(data, counter)
    MaleAge(data, counter)
    FemaleAge(data, counter)
    TransAge(data, counter)
    raceEthnicity(data, counter)
    lang(data, counter)
    dis(data, counter)
    loca(data, counter)
    risks(data, counter)
    eventreac(data, counter)
    focus(data, counter)
    material(data, counter)
    referral(data, counter)
    