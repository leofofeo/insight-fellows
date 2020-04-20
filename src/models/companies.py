class Companies:
    """
    The Companies class models information about companies that we 
    want to track, especially for the final couple of columns of output.
    At the moment, the Companies class is compositional and is only 
    instantiated as a property on the Product class.

    To be honest, I created it when I thought that I would need company names
    for my output - as it stands, it's a little extra and what I'm doing within
    the class could also be done within the Product class.
    """

    def __init__(self):
        self.companies_data = {}

    def __str__(self):
        return f"{self.companies_data}"

    def add_company_complaint(self, company_name):
        company_name = company_name.lower()
        if company_name in self.companies_data:
            self.companies_data[company_name] = self.companies_data[company_name] + 1
        else:
            self.companies_data[company_name] = 1
    
    def get_worst_company_percentage(self) -> float:
        complaints = [c for c in self.companies_data.values()]
        total_complaints = float(sum(complaints))
        highest_complaint = float(max(complaints))
        # I thought I needed to return the name of the company as well; leaving
        # this in here in case I need it later
        # highest_complaint = max(self.companies_data, key=self.companies_data.get)
        try :
            percentage = (highest_complaint / total_complaints) * 100
            return "{:.2f}".format(percentage)
        except ZeroDivisionError:
            return 0.0
        
        


        
