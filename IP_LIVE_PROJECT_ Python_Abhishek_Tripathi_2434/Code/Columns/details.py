from bs4 import BeautifulSoup
from urllib.request import urlopen


class AccessCollege:

    # Defalut Constructor
    def __init__(self, url):

        # College page url
        self.url = url

        self.uClient = urlopen(self.url)
        self.HTMLpage = self.uClient.read()
        self.uClient.close()
        self.soup = BeautifulSoup(self.HTMLpage, "html.parser")

        self.ID = (self.soup.findAll(
            "span", {"id": "ctl00_ContentPlaceHolder1_lblInstituteCode"}))[0].text

        self.collegeName = self.soup.findAll("span", {"id": "ctl00_ContentPlaceHolder1_lblInstituteNameEnglish"})[
            0].text
        if "," in self.collegeName:
            self.collegeName = self.collegeName.replace(',', '-').strip()
        elif "\n" in self.collegeName:
            self.collegeName = self.collegeName.replace('\n', ' ').strip()

        self.address = (self.soup.findAll(
            "span", {"id": "ctl00_ContentPlaceHolder1_lblAddressEnglish"}))[0].text
        if "," in self.address:
            self.address = self.address.replace(',', '-').strip()
        elif "\n" in self.address:
            self.address = self.address.replace('\n', ' ').strip()

        self.emailID = (list(self.soup.findAll(
            "span", {"id": "ctl00_ContentPlaceHolder1_lblEMailAddress"}))[0].text.split(",")[0]).strip()

        self.district = (self.soup.findAll(
            "span", {"id": "ctl00_ContentPlaceHolder1_lblDistrict"}))[0].text.strip()

        self.website = (self.soup.findAll(
            "span", {"id": "ctl00_ContentPlaceHolder1_lblWebAddress"}))[0].text
        if "," in self.website:
            self.website = self.website.replace(',', '-').strip()

        self.principalName = (list(self.soup.findAll("span", {"id": "ctl00_ContentPlaceHolder1_lblPrincipalNameEnglish"}))[
            0].text.split(",")[0])

        self.officeNumber = (list(
            (self.soup.findAll("span", {"id": "ctl00_ContentPlaceHolder1_lblOfficePhoneNo"}))[0].text.split(
                " "))[0])

        self.personalNumber = (
            list(((self.soup.findAll("span", {"id": "ctl00_ContentPlaceHolder1_lblPersonalPhoneNo"}))[
                0].text).split(" "))[0])

        self.registarName = \
            (self.soup.findAll("span", {"id": "ctl00_ContentPlaceHolder1_lblRegistrarNameEnglish"}))[
                0].text

        self.status = (self.soup.findAll(
            "span", {"id": "ctl00_ContentPlaceHolder1_lblStatus1"}))[0].text

        self.autonomyStatus = (self.soup.findAll(
            "span", {"id": "ctl00_ContentPlaceHolder1_lblStatus2"}))[0].text

        self.minorityStatus = (self.soup.findAll(
            "span", {"id": "ctl00_ContentPlaceHolder1_lblStatus3"}))[0].text

        self.yearOfEstablishment = (
            self.soup.findAll("span", {"id": "ctl00_ContentPlaceHolder1_lblEstablishmentYear"}))[0].text

        if "engineering" in self.collegeName.lower() or "technology" in self.collegeName.lower() or "technological" in self.collegeName.lower() or "technical" in self.collegeName.lower():
            self.course = "Engineering"
        elif "management" in self.collegeName.lower():
            self.course = "Management"
        elif "polytechnic" in self.collegeName.lower():
            self.course = "Polytechnic"
        elif "pharmacy" in self.collegeName.lower():
            self.course = "Pharmacy"
        elif "architecture" in self.collegeName.lower():
            self.course = "Architecture"
        elif "textile" in self.collegeName.lower():
            self.course = "Textile"
        else:
            self.course = "Other"

        if "research" in self.collegeName.lower():
            self.research = "Yes"
        else:
            self.research = "No"
