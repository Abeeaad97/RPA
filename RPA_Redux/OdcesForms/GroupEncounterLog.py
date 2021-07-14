from OdcesForms import SeleniumAbid

def groupType(daFra, counter):
    if str(daFra.iloc[counter]["GroupSessionType"]) == 'GROUP COUNSELING':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlServiceTypeCode_0").click()
    else:
        SeleniumAbid .driver.find_element_by_id("ContentPlaceHolder1_rdlServiceTypeCode_1")
def groupLoca(daFra, counter): 
    if str(daFra.iloc[counter]["Location"]) == 'school and child care (all ages through college)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_0").click()
    elif str(daFra.iloc[counter]["Location"]) == 'community center (e.g. recreation club)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_1").click()
    elif str(daFra.iloc[counter]["Location"]) == 'provider site/mental health agency (agency involved with Crisis Counseling Assistance and Training Program [CCP])':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_2").click()
    elif str(daFra.iloc[counter]["Location"]) == 'workplace (workplace of the disaster survivor and/or first responder)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_3").click()
    elif str(daFra.iloc[counter]["Location"]) == 'disaster recovery center (e.g. Federal Emergency Management Agency [FEMA] American Red Cross)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_4").click()
    elif str(daFra.iloc[counter]["Location"]) == 'place of worship (e.g. church synagogue mosque)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_5").click()
    elif str(daFra.iloc[counter]["Location"]) == 'home (temporary or permanent residence including friend/family home; group homes including houses apartments trailers and other dwellings)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_6").click()
    elif str(daFra.iloc[counter]["Location"]) == 'retail (e.g. restaurant mall shopping center store)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_7").click()
    elif str(daFra.iloc[counter]["Location"]) == 'medical center (e.g. doctor dentist hospital mental health or substance abuse specialty center)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_8").click()
    elif str(daFra.iloc[counter]["Location"]) == 'public place/event (e.g. street sidewalk town square fair festival sports)':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_9").click()
    elif str(daFra.iloc[counter]["Location"]) == 'Other':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlGroupServiceLocationCode_10").click()
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtGroupServiceLocationOther").send_keys(str(daFra.iloc[counter]["Other Location"]))
def groupSessNum(daFra, counter):
    if str(daFra.iloc[counter]["Visit Number"]) == 'First session of group expected to meet once':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlSessionNumberCode_0").click()
    elif str(daFra.iloc[counter]["Visit Number"]) == 'First session of group expected to meet more than once':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlSessionNumberCode_1").click()
    elif str(daFra.iloc[counter]["Visit Number"]) == 'Second or greater session of ongoing group':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlSessionNumberCode_2").click()
def groupNumofPeople(daFra, counter):
    if int(daFra.iloc[counter]["GroupMinor"]) > 0:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtParticipant18").send_keys(str(daFra.iloc[counter]["GroupMinors"]))
    if int(daFra.iloc[counter]["GroupAdult"]) > 0:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtParticipant64").send_keys(str(daFra.iloc[counter]["GroupAdults"]))
    if int(daFra.iloc[counter]["GroupSenior"]) > 0:
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtParticipant65").send_keys(str(daFra.iloc[counter]["GroupSeniors"]))
def groupCompo(daFra, counter):
    if str(daFra.iloc[counter]["GroupIdentities"]) == 'Children or youth (Under age 18) CHECK if yes':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlIdentitiesCode_0").click()
    if str(daFra.iloc[counter]["GroupIdentities"]) == 'Adult survivors (adults who were directly affected by the disaster)? CHECK if yes':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlIdentitiesCode_1").click()
    elif str(daFra.iloc[counter]["GroupIdentities"]) == 'Public safety workers and first responders (e.g.  police  fire  emergency medical services  rescue)? CHECK  if yes.':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlIdentitiesCode_2").click()
    elif str(daFra.iloc[counter]["GroupIdentities"]) == 'Other recovery workers(e.g. health care disaster relief social services)? CHECK if yes':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlIdentitiesCode_3").click()
    elif str(daFra.iloc[counter]["GroupIdentities"]) == 'Was the group composed of a mixture of the above or none of the above (i.e. no clear group identity)? CHECK if yes':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_rdlIdentitiesCode_4").click()
def groupRaceEth(daFra, counter):
    if str(daFra.iloc[counter]["Race/Ethnicity"]) == 'American Indian/Alaska Native':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_0").click()
    elif str(daFra.iloc[counter]["Race/Ethnicity"]) == 'Native Hawaiian/Other Pacific Islander':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_1").click()
    elif str(daFra.iloc[counter]["Race/Ethnicity"]) == 'Asian':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_2").click()
    elif str(daFra.iloc[counter]["Race/Ethnicity"]) == 'White':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_3").click()
    elif str(daFra.iloc[counter]["Race/Ethnicity"]) == 'Black or African American':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_4").click()
    elif str(daFra.iloc[counter]["Race/Ethnicity"]) == 'Hispanic or Latino':
        SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_cblRaceCodes_5").click()
def groupDis(daFra, counter):
    None 
def groupFocus(daFra, counter):
    None
    

def start(y, df):
    counter = y
    daFra = df
    SeleniumAbid.driver.find_element_by_id("UCSideNav_HyperLink30")
    SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_txtEmployeeNumber1").send_keys(1234)
    groupType(daFra, counter)
    groupLoca(daFra, counter)
    groupSessNum(daFra, counter)
    groupNumofPeople(daFra, counter)
    groupCompo(daFra, counter)
    groupRaceEth(daFra, counter)
    groupDis(daFra, counter)
    groupFocus(daFra, counter)
