#WAP a program that defines a list of  countries that are a member of BRICS. Check weather a country is member of BRICS or not.

brics_countries = ["Brazil", "Russia", "India", "China", "South Africa"]
def is_brics_member(country):
    if country in brics_countries:
        return True
    else:
        return False
print(is_brics_member("India")) 
print(is_brics_member("USA")) 
