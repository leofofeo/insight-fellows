from models.companies import Companies

class Product:
    """
    The Product class models a self-contained representation of the majority
    of the output. Since the CSV output rows are largely centered around aggregated
    data about products in the CSV input, the Product class is used to keep track
    of that data and make the necessary calculations
    """
    def __init__(self, name, year, product_id = ""):
        self.year = year
        self.name = name
        self.product_id = str(year) + name if product_id == "" else product_id
        self.reported_companies = set()
        self.complaints = 0
        self.companies = Companies()
    
    def __str__(self):
        return f"""Product {self.name} for {self.year}
        Product id: {self.product_id}
        Reported companies: {self.reported_companies}
        Number of complaints: {self.complaints}
        Companies data: {self.companies}
        Full name: {self.full_product_name}
        """
    
    def __repr__(self):
        return f"""Product.product_id<{self.product_id}>
        Product.name<{self.name}
        Product.year<{self.year}>
        Product.reported_companies{self.reported_companies}>
        Product.complaints<{self.complaints}>
        Product.companies<{self.companies}>
        """
    
    @property
    def full_product_name(self):
        try:
            return ProductNames.get_full_product_name(self.name)
        except:
            return self.name

class ProductNames:
    names = [
        "debt collection", 
        "credit reporting, credit repair services, or other personal consumer reports",
    ]
    product_symbols = {
        "debt": names[0],
        "credit": names[1],
    }

    @classmethod
    def get_product_name_symbol(cls, product_name: str) -> str:
        product_name = product_name.lower()
        if product_name not in cls.names:
                raise ProductNameDoesNotExistException("Product name doesn't exist")
        if product_name == cls.product_symbols["debt"]:
            symbol = "debt"
        elif product_name == cls.product_symbols["credit"]:
            symbol = "credit"
        return symbol

    @classmethod
    def get_full_product_name(cls, product_symbol) -> str:
        product_symbol = product_symbol.lower()
        if product_symbol not in cls.product_symbols:
            raise ProductNameDoesNotExistException("Product symbol doesn't exist")
        return cls.product_symbols[product_symbol]

class ProductNameDoesNotExistException(Exception):
    """An extended exception for handling the name look up errors"""
    def __init__(cls, message):
        cls.message = message

