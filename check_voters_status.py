# ========= Functions in Python ========= #
# ===== Functions with no argument ====== #
# ======== Voters Eligibility Checker App ====== #
def title():
    title = input("Title(Mr/Mrs/Miss)๐ ")
    if title == 'Mr':
        return (title + "๐น")
    elif title == "Mrs":
        return (title + "๐บ")
    else:
        return (title + "๐ผ")

def full_name():
    full_name = input("Full_name๐ ")
    return full_name

def country():
    country = input("Country๐ ")
    return country

def state_origin():
   state_origin = input("State of Origin๐ ")
   return state_origin

def age():
    age = int(input("Enter age๐ "))
    if age > 18:
        return (f"{age}years"
                f"\n๐Voters Status: Eligible")
    else:
        return (f"{age}years"
                f"\n๐ Voters Status: not Eligible")

def check_voters_status():
    print("๐ป๐ป----------๐Fill the details-----------------๐ป๐ป")
    return (f"๐ป๐ป----------๐Status Information๐-----------------๐ป๐ป"
            f"\n๐ Title: {title()} "
            f"\n๐ Full Name: {full_name()}"
            f"\n๐ Country: {country()}"
            f"\n๐ State of Origin: {state_origin()}"
            f"\n๐ Age: {age()}"
            f"\n๐ป๐ป------------๐Thank you!๐--------------------๐ป๐ป")
