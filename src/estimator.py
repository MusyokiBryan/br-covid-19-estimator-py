def get_currentlyInfected(reportedCases, multiplier):
    return reportedCases * multiplier

def get_infectionsByRequestedTime(currentlyInfected, timeToElapse):
    factor = int(timeToElapse / 3)
    result = currentlyInfected * pow(2, factor)
    result = int(result)
    return result

def get_severeCasesByRequestedTime(infectionsByRequestedTime):
    severeCasesByRequestedTime = infectionsByRequestedTime * (15 / 100)
    return int(severeCasesByRequestedTime)

def get_hospitalBedsByRequestedTime(severeCasesByRequestedTime, totalHospitalBeds):
    expectedHospitalBeds = totalHospitalBeds * (35 / 100)
    hospitalBedsByRequestedTime = expectedHospitalBeds - severeCasesByRequestedTime
    return int(hospitalBedsByRequestedTime)

def get_casesForICUByRequestedTime(infectionsByRequestedTime):
    casesForICUByRequestedTime = infectionsByRequestedTime * (5 / 100)
    return int(casesForICUByRequestedTime)

def get_casesForVentilatorsByRequestedTime(infectionsByRequestedTime):
    casesForVentilatorsByRequestedTime = infectionsByRequestedTime * (2 / 100)
    return int(casesForVentilatorsByRequestedTime)

def get_dollarsInFlight(infectionsByRequestedTime, avgDailyIncomePopulation, avgDailyIncomeInUSD, timeToElapse):
    dollarsInFlight = (infectionsByRequestedTime * avgDailyIncomePopulation * avgDailyIncomeInUSD) / timeToElapse
    return int(dollarsInFlight)

def estimator(data):

    periodType = data["periodType"]
    avgDailyIncomePopulation = data["region"]["avgDailyIncomePopulation"]
    avgDailyIncomeInUSD = data["region"]["avgDailyIncomeInUSD"]
    timeToElapse = int(data["timeToElapse"])
    
    if periodType == 'months':
        timeToElapse = int(data["timeToElapse"]) * 30
    else:
        if periodType == 'weeks':
            timeToElapse = int(data["timeToElapse"]) * 7
    
    impact = {}
    impact.update({"currentlyInfected": get_currentlyInfected(data["reportedCases"], 10)})
    impact.update({"infectionsByRequestedTime": get_infectionsByRequestedTime(impact["currentlyInfected"], timeToElapse)})
    impact.update({"severeCasesByRequestedTime": get_severeCasesByRequestedTime(impact["infectionsByRequestedTime"])})
    impact.update({"hospitalBedsByRequestedTime": get_hospitalBedsByRequestedTime(impact["severeCasesByRequestedTime"], data["totalHospitalBeds"])})
    impact.update({"casesForICUByRequestedTime": get_casesForICUByRequestedTime(impact["infectionsByRequestedTime"])})
    impact.update({"casesForVentilatorsByRequestedTime": get_casesForVentilatorsByRequestedTime(impact["infectionsByRequestedTime"])})
    impact.update({"dollarsInFlight": get_dollarsInFlight(impact["infectionsByRequestedTime"], avgDailyIncomePopulation, avgDailyIncomeInUSD, timeToElapse)})
    
    severeImpact = {}
    severeImpact.update({"currentlyInfected": get_currentlyInfected(data["reportedCases"], 50)})
    severeImpact.update({"infectionsByRequestedTime": get_infectionsByRequestedTime(severeImpact["currentlyInfected"], timeToElapse)})
    severeImpact.update({"severeCasesByRequestedTime": get_severeCasesByRequestedTime(severeImpact["infectionsByRequestedTime"])})
    severeImpact.update({"hospitalBedsByRequestedTime": get_hospitalBedsByRequestedTime(severeImpact["severeCasesByRequestedTime"], data["totalHospitalBeds"])})
    severeImpact.update({"casesForICUByRequestedTime": get_casesForICUByRequestedTime(severeImpact["infectionsByRequestedTime"])})
    severeImpact.update({"casesForVentilatorsByRequestedTime": get_casesForVentilatorsByRequestedTime(severeImpact["infectionsByRequestedTime"])})
    severeImpact.update({"dollarsInFlight": get_dollarsInFlight(severeImpact["infectionsByRequestedTime"], avgDailyIncomePopulation, avgDailyIncomeInUSD, timeToElapse)})
    
    estimate = {}
    estimate.update({"data": data})
    estimate.update({"impact": impact})
    estimate.update({"severeImpact": severeImpact})
    
    return estimate