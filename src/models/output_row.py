class OutputRow():
    """Representation of each row in the output file"""
    def __init__(
        self, 
        year, 
        name, 
        total_complaints, 
        total_companies, 
        percentage
    ):
        self.year = year
        self.name = name
        self.total_complaints = total_complaints,
        self.total_companies = total_companies,
        self.percentage = percentage

    def __str__(self):
        return f"""
        name: {self.name}
        year: {self.year}
        total complaints: {self.total_complaints}
        total number of companies: {self.total_companies}
        highest percentage of complaints: {self.percentage}
        """
    
    def __repr__(self):
        return f"""
        name: {self.name}
        year: {self.year}
        total complaints: {self.total_complaints}
        total number of companies: {self.total_companies}
        highest percentage of complaints: {self.percentage}
        """