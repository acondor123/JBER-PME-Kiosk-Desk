import re

'''
    This file contains the functions responsible for validating user input.
    The functions will validate each input as enforced by the website at the following URL:
        https://jberpme-96ea7d14ff9b.herokuapp.com/
'''

maxNameLength = 64
validPhoneNumberLength = 10
minUnitLength = 1
maxUnitLength = 5
nameRegex = r'^[a-zA-ZÀ-ÖØ-öø-ÿ-]+$'
phoneRegex = r'^[1-9]{1}[0-9]{9}'

def validateFirstName(name):


    if(not bool(name)):
       return False
    elif(len(name) >= maxNameLength):
        return False
    elif(bool(re.match(nameRegex, name.strip())) is False):
        return False
    else:
        return True


def validateLastName(name):
    if(not bool(name)):
       return False
    elif(len(name) >= maxNameLength):
        return False
    elif(bool(re.match(nameRegex, name.strip())) is False):
        return False
    else:
        return True


def validateRank(rank):
    validRanks = ["amn", "a1c", "sra", "ssgt", "tsgt", "msgt", "smsgt", "cmsgt"]
    if(rank not in validRanks):
        return False
    else:
        return True


def validateUnit(unit):
    if(not bool(unit)):
        return False
    elif(len(unit) <= minUnitLength or len(unit) >= maxUnitLength):
        return False
    else:
        return True


def validatePhoneNumber(phoneNumber):
    if(not re.match(phoneRegex, phoneNumber)):
        return False
    else:
        return True

def validateFitness(fitness):
    validResponses = ["yes", "no"]
    if(fitness not in validResponses):
        return False
    else:
        return True
    
def validateProfile(profile):
    validResponses = ["yes", "no"]
    if(profile not in validResponses):
        return False
    else:
        return True