# ========= Functions in Python ========= #
# ===== Functions with no argument ====== #
# ======== Voters Eligibility Checker App ====== #
def title():
    title = input("Title(Mr/Mrs/Miss)👉 ")
    if title == 'Mr':
        return (title + "🚹")
    elif title == "Mrs":
        return (title + "🚺")
    else:
        return (title + "👼")

def full_name():
    full_name = input("Full_name👉 ")
    return full_name

def country():
    country = input("Country👉 ")
    return country

def state_origin():
   state_origin = input("State of Origin👉 ")
   return state_origin

def age():
    age = int(input("Enter age👉 "))
    if age > 18:
        return (f"{age}years"
                f"\n👉Voters Status: Eligible")
    else:
        return (f"{age}years"
                f"\n👉 Voters Status: not Eligible")

def check_voters_status():
    print("💻💻----------🖊Fill the details-----------------💻💻")
    return (f"💻💻----------🖊Status Information🖊-----------------💻💻"
            f"\n👉 Title: {title()} "
            f"\n👉 Full Name: {full_name()}"
            f"\n👉 Country: {country()}"
            f"\n👉 State of Origin: {state_origin()}"
            f"\n👉 Age: {age()}"
            f"\n💻💻------------🖊Thank you!🖊--------------------💻💻")
