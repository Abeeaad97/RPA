from OdcesForms import SeleniumAbid
from OdcesForms import IndiLog
#import testData


def AduRiskCode(dFrame, counter):
    risk = dFrame.iloc[counter]["Risk Categories"]
    riskCode = risk.split(";")
    for x in riskCode:
        if x == 'family missing/dead':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblAdultChildRiskCodes_0").click()
        elif x == 'friend missing/dead':        
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblAdultChildRiskCodes_1").click()
        elif x == 'pet missing/dead':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblAdultChildRiskCodes_2").click()
        elif x == 'home damaged or destroyed':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblAdultChildRiskCodes_3").click()
        elif x == 'vehicle or major property loss':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblAdultChildRiskCodes_4").click()
        elif x == 'other financial loss':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblAdultChildRiskCodes_5").click()
        elif x == 'disaster unemployed (self or household member)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblAdultChildRiskCodes_6").click()
        elif x == 'injured or physically harmed (self or household member)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblAdultChildRiskCodes_7").click()
        elif x == 'life was threatened (self or household member)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblAdultChildRiskCodes_8").click()
        elif x == 'witnessed death/injury (self or household member)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblAdultChildRiskCodes_9").click()
        elif x == 'assisted with rescue/recovery (self or household member)':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblAdultChildRiskCodes_10").click()
        elif x == 'had to change schools':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblAdultChildRiskCodes_11").click()
        elif x == 'prolonged separation from family':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblAdultChildRiskCodes_12").click()
        elif x == 'evacuated quickly with no time to prepare':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblAdultChildRiskCodes_13").click()
        elif x == 'displaced from home 1 week or more':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblAdultChildRiskCodes_14").click()
        elif x == 'sheltered in place or sought shelter due to immediate threat of danger':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblAdultChildRiskCodes_15").click()
        elif x == 'past substance use/mental health problem':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblAdultChildRiskCodes_16").click()
        elif x == 'preexisting physical disability':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblAdultChildRiskCodes_17").click()
        elif x == 'past trauma':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblAdultChildRiskCodes_18").click()

def AduAgeGen(dFrame, counter):
    if dFrame.iloc[counter]["Adult Age"] == 'adult (18-39)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlAdultAgeCode_0").click()
    elif dFrame.iloc[counter]["Adult Age"] == 'adult (40-64)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlAdultAgeCode_1").click()
    elif dFrame.iloc[counter]["Adult Age"] == 'older adult (65 years or older)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlAdultAgeCode_2").click()
        
    if dFrame.iloc[counter]["Adult Gender"] == 'Male':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlSexCodes_0").click()
    elif dFrame.iloc[counter]["Adult Gender"] == 'Female':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlSexCodes_1").click
    elif dFrame.iloc[counter]["Adult Gender"] == 'Transgender':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlSexCodes_2").click()
    elif dFrame.iloc[counter]["Adult Gender"] == 'None':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlSexCodes_3").click()

def AduAssessQuest(dFrame, counter):
    AduAssessQ = {
        1:dFrame.iloc[counter]["Adu Assessment 1"],
        2:dFrame.iloc[counter]["Adu Assessment 2"],
        3:dFrame.iloc[counter]["Adu Assessment 3"],
        4:dFrame.iloc[counter]["Adu Assessment 4"],
        5:dFrame.iloc[counter]["Adu Assessment 5"],
        6:dFrame.iloc[counter]["Adu Assessment 6"],
        7:dFrame.iloc[counter]["Adu Assessment 7"],
        8:dFrame.iloc[counter]["Adu Assessment 8"],
        9:dFrame.iloc[counter]["Adu Assessment 9"],
        10:dFrame.iloc[counter]["Adu Assessment 10"],
        11:dFrame.iloc[counter]["Adu Assessment 11"],
        12:dFrame.iloc[counter]["Adu Assessment 12"],
        13:dFrame.iloc[counter]["Adu Assessment 13"],
        14:dFrame.iloc[counter]["Adu Assessment 14"]
    }
    
    for key in AduAssessQ:
        if key == 1:
            if AduAssessQ[key] == '1-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ1Code_0").click()
            elif AduAssessQ[key] == '2-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ1Code_1").click()
            elif AduAssessQ[key] == '3-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ1Code_2").click()
            elif AduAssessQ[key] == '4-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ1Code_3").click()
            elif AduAssessQ[key] == '5-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ1Code_4").click()
            elif AduAssessQ[key] == 'N/A':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ1Code_5").click()
        elif key == 2:
            if AduAssessQ[key] == '1-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ2Code_0").click()
            elif AduAssessQ[key] == '2-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ2Code_1").click()
            elif AduAssessQ[key] == '3-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ2Code_2").click()
            elif AduAssessQ[key] == '4-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ2Code_3").click()
            elif AduAssessQ[key] == '5-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ2Code_4").click()
            elif AduAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ2Code_5").click()
        elif key == 3:
            if AduAssessQ[key] == '1-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ3Code_0").click()
            elif AduAssessQ[key] == '2-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ3Code_1").click()
            elif AduAssessQ[key] == '3-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ3Code_2").click()
            elif AduAssessQ[key] == '4-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ3Code_3").click()
            elif AduAssessQ[key] == '5-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ3Code_4").click()
            elif AduAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ3Code_5").click()
        elif key == 4:
            if AduAssessQ[key] == '1-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ4Code_0").click()
            elif AduAssessQ[key] == '2-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ4Code_1").click()
            elif AduAssessQ[key] == '3-somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ4Code_2").click()
            elif AduAssessQ[key] == '4-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ4Code_3").click()
            elif AduAssessQ[key] == '5-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ4Code_4").click()
            elif AduAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ4Code_5").click()
        elif key == 5:
            if AduAssessQ[key] == '1-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ5Code_0").click()
            elif AduAssessQ[key] == '2-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ5Code_1").click()
            elif AduAssessQ[key] == '3-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ5Code_2").click()
            elif AduAssessQ[key] == '4-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ5Code_3").click()
            elif AduAssessQ[key] == '5-Very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ5Code_4").click()
            elif AduAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ5Code_5").click()
        elif key == 6:
            if AduAssessQ[key] == '1-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ6Code_0").click()
            elif AduAssessQ[key] == '2-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ6Code_1").click()
            elif AduAssessQ[key] == '3-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ6Code_2").click()
            elif AduAssessQ[key] == '4-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ6Code_3").click()
            elif AduAssessQ[key] == '5-very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ6Code_4").click()
            elif AduAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ6Code_5").click()
        elif key == 7:
            if AduAssessQ[key] == '1-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ7Code_0").click()
            elif AduAssessQ[key] == '2-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ7Code_1").click()
            elif AduAssessQ[key] == '3-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ7Code_2").click()
            elif AduAssessQ[key] == '4-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ7Code_3").click()
            elif AduAssessQ[key] == '5-very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ7Code_4").click()
            elif AduAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ7Code_5").click()
        elif key == 8:
            if AduAssessQ[key] == '1-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ8Code_0").click()
            elif AduAssessQ[key] == '2-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ8Code_1").click()
            elif AduAssessQ[key] == '3-somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ8Code_2").click()
            elif AduAssessQ[key] == '4-QUite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ8Code_3").click()
            elif AduAssessQ[key] == '5-very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ8Code_4").click()
            elif AduAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ8Code_5").click()
        elif key == 9:
            if AduAssessQ[key] == '1-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ9Code_0").click()
            elif AduAssessQ[key] == '2-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ9Code_1").click()
            elif AduAssessQ[key] == '3-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ9Code_2").click()
            elif AduAssessQ[key] == '4-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ9Code_3").click()
            elif AduAssessQ[key] == '5-very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ9Code_4").click()
            elif AduAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ9Code_5").click()
        elif key == 10:
            if AduAssessQ[key] == '1-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ10Code_0").click()
            elif AduAssessQ[key] == '2-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ10ode_1").click()
            elif AduAssessQ[key] == '3-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ10Code_2").click()
            elif AduAssessQ[key] == '4-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ10Code_3").click()
            elif AduAssessQ[key] == '5-very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ10Code_4").click()
            elif AduAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ10Code_5").click()
        elif key == 11:
            if AduAssessQ[key] == '1-Not at all':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ11Code_0").click()
            elif AduAssessQ[key] == '2-A little bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ11Code_1").click()
            elif AduAssessQ[key] == '3-Somewhat':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ11Code_2").click()
            elif AduAssessQ[key] == '4-Quite a bit':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ11Code_3").click()
            elif AduAssessQ[key] == '5-very much':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ11Code_4").click()
            elif AduAssessQ[key] == 'NA':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ11Code_5").click()
        elif key == 12:
            if AduAssessQ[key] == 'no':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ12Code_0").click()
            elif AduAssessQ[key] == 'yes':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ12Code_1").click()
        elif key == 13:
            if AduAssessQ[key] == 'no':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ13Code_0").click()
            elif AduAssessQ[key] == 'yes':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ13Code_1").click()
        elif key == 14: 
            if AduAssessQ[key] == 'no':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ14Code_0").click()
            elif AduAssessQ[key] == 'yes':
                SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlQ14Code_1").click()

def AdultLoca(dFrame, counter):
    print(dFrame.iloc[counter]["Location"])
    if dFrame.iloc[counter]["Location"] == 'school and child care (all ages through college)':    
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_0").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_0").click()
    elif dFrame.iloc[counter]["Location"] == 'community center (e.g.  recreation club)':    
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_1").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_1").click()
    elif dFrame.iloc[counter]["Location"] == 'provider site/mental health agency (agency involved with Crisis Counseling Assistance and Training Program [CCP])':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_2").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_2").click()
    elif dFrame.iloc[counter]["Location"] ==  'workplace (workplace of the disaster survivor and/or first responder)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_3").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_3").click()
    elif dFrame.iloc[counter]["Location"] == 'disaster recovery center (e.g.  Federal Emergency Management Agency [FEMA]  American Red Cross)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_4").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_4").click()
    elif dFrame.iloc[counter]["Location"] == 'place of worship (e.g., church, synagogue, mosque)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_5").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_5").click()
    elif dFrame.iloc[counter]["Location"] == 'retail (e.g., restaurant, mall, shopping center, store)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_6").click()
    elif dFrame.iloc[counter]["Location"] == 'public place/event (e.g., street, sidewalk, town square, fair, festival, sports)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_7").click()
    elif dFrame.iloc[counter]["Location"] == 'temporary home (including friend or family homes, group homes, shelters, apartments, trailers, and other dwellings)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_8").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_8").click()
        if dFrame.iloc[counter]["TempMinor"] == 'YES':
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_9").click()
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_9").click()
    elif dFrame.iloc[counter]["Location"] == 'permanent home':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_10").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_10").click()
        if dFrame.iloc[counter]["PermMinor"] == 'YES': 
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_11").click()
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_11").click()
    elif dFrame.iloc[counter]["Location"] == 'phone counseling (15 minutes or longer)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_12").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_12").click()
        if dFrame.iloc[counter]["Crisis Line"] == 'Crisis Line':        
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_13").click()
            SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_13").click()
    elif dFrame.iloc[counter]["Location"] == 'medical center (e.g., doctor, dentist, hospital, mental health, or substance abuse specialty center)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_14").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_14").click()
    elif dFrame.iloc[counter]["Location"] == 'other':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_15").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblServiceLocationCodes_15").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtServiceLocationOther").send_keys(dFrame.iloc[counter]["Other Location"])
def start(y, df):
    counter = y
    dFrame = df
    SeleniumAbid.driver.find_element_by_id("UCSideNav_HyperLink32").click()   
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtEmployeeNumber1").send_keys(str(dFrame.iloc[y]["WorkerNum"]))
    #IndiLog.loca(testData.location, testData.minor, testData.crisis, testData.otherLoc)
    AdultLoca(dFrame, counter)
    IndiLog.visitNumber(dFrame, counter)
    IndiLog.visitDuration(dFrame, counter)
    if dFrame.iloc[y]["Lead Pres"] == 'YES':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlLeadPresentCode_0").click()       
    else:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlLeadPresentCode_1").click()
    AduRiskCode(dFrame, counter)
    AduAgeGen(dFrame, counter)
    IndiLog.dis(dFrame, counter)
    IndiLog.lang(dFrame, counter)
    IndiLog.raceEthnicity(dFrame, counter)
    AduAssessQuest(dFrame, counter)
    IndiLog.referral(dFrame, counter)
    if dFrame.iloc[y]["Ref Accept"]:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlAcceptCode_1").click()
    else:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlAcceptCode_0").click()