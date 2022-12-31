import webbrowser
import os

from filestack import Client
from fpdf import FPDF


class PDF_Report:
    """
    Creates a PDF file that contains roommate names, their share of
    the bill, and the billing period.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):

        roommate1_share = str(roommate1.pays(bill, roommate2))
        roommate2_share = str(roommate2.pays(bill, roommate1))

        pdf = FPDF(orientation='P', unit='pt', format='letter')
        pdf.add_page()

        # Add house icon
        pdf.image("files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=20, style='B')
        pdf.cell(w=0, h=80, txt='Roommates Utility Bill', border=1, align='C', ln=1)

        # Insert billing period and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=150, h=40, txt='Billing Period: ', border=0, align='C')
        pdf.cell(w=150, h=40, txt=bill.billing_period, border=0, align='C', ln=1)

        # Insert name and utility bill share of first roommate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=150, h=25, txt= roommate1.name + ':', border=0, align='C')
        pdf.cell(w=150, h=25, txt= '$ ' + roommate1_share, border=0, ln=1, align='C')

        # Insert name and utility bill share of second roommate
        pdf.cell(w=150, h=25, txt= roommate2.name + ':', border=0, align='C')
        pdf.cell(w=150, h=25, txt= '$ '+ roommate2_share, border=0, ln=1, align='C')

        # Changed directory to files, and generate and open pdf in browser
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)

class FileSharer:

    def __init__(self, filepath, api_key="AOxNiW5S8S6SR8tGcJKQuz"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
