class Bill:
    """
    Object contains data about an apartment bill, e.g. total amount and
    billing period.
    """

    def __init__(self, amount, billing_period):
        self.amount = amount
        self.billing_period = billing_period


class Roommate:
    """"
    Creates a roommate who shares an apartment and pays a part of the
    bill.
    """

    def __init__(self, name, days_stayed):
        self.name = name
        self.days_stayed = days_stayed

    def pays(self, bill,roommate2):
        weight = self.days_stayed / (self.days_stayed + roommate2.days_stayed)
        to_pay = round(bill.amount * weight,2)
        return to_pay
