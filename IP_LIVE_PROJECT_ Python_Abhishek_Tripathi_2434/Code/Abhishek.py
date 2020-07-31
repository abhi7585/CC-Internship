from collegeList import getLink
from Columns.details import AccessCollege
from tqdm import tqdm

college = getLink()

# File to store the Scrapped College Details
f = open("MumbaiCollege.csv", "w")
f.write("Id,College_Name,Address,EmailID,District,Website,Principal_Name,Office_Number,Personal_Number,Registar_Name,Status,Autonomy_Status,Minority_Status,Establishment,Course,Research\n")

for i in tqdm(college):
    Obj = AccessCollege(i)
    data = Obj.ID + "," + Obj.collegeName + "," + Obj.address + "," + Obj.emailID + "," + Obj.district + "," + Obj.website + "," + Obj.principalName + "," + Obj.officeNumber + "," + Obj.personalNumber + \
        "," + Obj.registarName + "," + Obj.status + "," + Obj.autonomyStatus + "," + Obj.minorityStatus + \
        "," + Obj.yearOfEstablishment + "," + Obj.course + "," + Obj.research + "\n"
    f.write(data)

f.close()
