import csv

import requests


SOMWANG_BRANCH_DATA_API = "https://www.somwang.co.th/bin/searchBranchServlet"

if __name__ == "__main__":
    body = {
        "method": "getAllSomwangBranchDetail",
    }
    response = requests.post(SOMWANG_BRANCH_DATA_API, json=body)
    data = response.json()

    columns = [
        "addressDetailEn",
        "addressDetailTh",
        "addressEn",
        "addressTh",
        "branchNameEn",
        "branchNameTh",
        "districtEn",
        "districtTh",
        "faxExt",
        "faxTh",
        "latitude",
        "longtitude",
        "provinceNameEn",
        "provinceNameTh",
        "subDistrictEn",
        "subDistrictTh",
        "telExt",
        "telTh",
        "timeEn",
        "timeTh",
        "timeWeekendEn",
        "timeWeekendTh",
        "workingHourEn",
        "workingHourTh",
        "workingHourWeekendEn",
        "workingHourWeekendTh",
        "zipCode",
        "code",
        "mobile",
        "branchType",
    ]
    with open("somwang_branches.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        for each in data:
            writer.writerow(each)
