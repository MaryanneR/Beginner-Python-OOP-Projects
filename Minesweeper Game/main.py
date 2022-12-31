from reports import PDF_Report, FileSharer
from roommates import Bill, Roommate

intro = "This is a program that helps you and your roommate determine " \
        "how to split your utility bill depending on the days each of " \
        "you spent in your shared space."
print(intro)
amount = float(input("\nEnter your utility bill amount: $"))
bill_period = input("Enter the billing period (e.g. June 2020): ")
rm1 = input("What is your name?: ")
rm1_days = int(input(f"How many days did {rm1} stay in the apartment?: "))
rm2 = input("What is your roommate's name?: ")
rm2_days = int(input(f"How many days did {rm2} stay in the apartment?: "))

utility_bill = Bill(amount, bill_period)
roommate1 = Roommate(rm1, rm1_days)
roommate2 = Roommate(rm2, rm2_days)

print(f"{rm1} pays $", roommate1.pays(utility_bill, roommate2))
print(f"{rm2} pays $", roommate2.pays(utility_bill, roommate1))

pdf_report = PDF_Report(f"{bill_period}.pdf")
pdf_report.generate(roommate1, roommate2, utility_bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())