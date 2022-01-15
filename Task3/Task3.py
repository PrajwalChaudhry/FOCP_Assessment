from random import choice
def email():
    print("\n")
    print("Welcome to Pop Chat")
    print("One of our operators will be pleased to help you today.")
    print("\n")
    email=input("Please enter your poppleton email address: ")
    email=email.lower()
    if not "@pop.ac.uk" in email:
        print("Invalid email")
        return
    if len(email.split("@pop.ac.uk")[0])<2:
        print("Invalid email")
        return
    name=email.split("@pop.ac.uk")[0]
    cap_name=name.capitalize()
    conc_name=cap_name+"!"
    conc_name1=cap_name+","
    name_choice=['Janice,','Fiona,', 'Arthur,']
    print("Hi,",conc_name," Thank you, and Welcome to PopChat!")
    print("My name is",choice(name_choice)," and it will be my pleasure to help you.")
    user_input=input("----> ")  
    if "Wifi" in user_input:
        response=['Wifi is excellent','Wifi server is in maintainance','Restarting your Wifi ']
        print(choice(response))
        while True:
            user_input1=input("----> ")
            Exit=["exit",'bye','Goodbye','Exit','Bye','help']
            if not user_input1 in Exit:
                response1=['You should try working on this system','Report your problem on wifiproblem@gmail.com','mmm','We will inform you soon','yes','Hmmm',"Oh,yes","I see","Tell me more"]
                print(choice(response1))
            if user_input1 in Exit:
                print("Thanks,",conc_name1," for using PopChat. See you again soon!")
                break
    elif "network error" in user_input:
        response=['Sorry for the inconvineince','network line is in maintainance','Please wait for few minutes ']
        print(choice(response))
        while True:
            user_input1=input("----> ")
            Exit=["exit",'bye','Goodbye','Exit','Bye','help']
            if not user_input1 in Exit:
                response1=['You should try working on this system','Report your problem on networkproblem@gmail.com','mmm','We will inform you soon','yes','Hmmm',"Oh,yes","I see","Tell me more"]
                print(choice(response1))
            if user_input1 in Exit:
                print("Thanks,",conc_name1," for using PopChat. See you again soon!")
                break
    elif "library" in user_input:
        response=["Street 101 Library is opened till 6'Oclock",'library is closed today',"Library will opened at 10'Oclock"]
        print(choice(response))
        while True:
            user_input1=input("----> ")
            Exit=["exit",'bye','Goodbye','Exit','Bye','help']
            if not user_input1 in Exit:
                response1=['mmm','yes','Hmmm',"Oh,yes","I see","Tell me more"]
                print(choice(response1))
            if user_input1 in Exit:
                print("Thanks,",conc_name1," for using PopChat. See you again soon!")
                break
    elif "restaurant" in user_input:
        response=['Disort restaurant is open','restaurant is closed today',"sanny restaurant will open at 12'Oclock"]
        print(choice(response))
        while True:
            user_input1=input("----> ")
            Exit=["exit",'bye','Goodbye','Exit','Bye','help']
            if not user_input1 in Exit:
                response1=['mmm','yes','Hmmm',"Oh,yes","I see","Tell me more"]
                print(choice(response1))
            if user_input1 in Exit:
                print("Thanks,",conc_name1," for using PopChat. See you again soon!")
                break
    elif "deadline" in user_input:
        response=['Your deadline has been extended by two working days.']
        print(choice(response))
        while True:
            user_input1=input("----> ")
            Exit=["exit",'bye','Goodbye','Exit','Bye','help']
            if not user_input1 in Exit:
                response1=['mmm','yes','Hmmm',"Oh,yes","I see","Tell me more"]
                print(choice(response1))
            if user_input1 in Exit:
                print("Thanks,",conc_name1," for using PopChat. See you again soon!")
                break
    elif "weather" in user_input:
        response=['Sunny weather today','','Heavy rainfall','Snowfall',]
        print(choice(response))
        while True:
            user_input1=input("----> ")
            Exit=["exit",'bye','Goodbye','Exit','Bye','help']
            if not user_input1 in Exit:
                response1=['mmm','yes','Hmmm',"Oh,yes","I see","Tell me more"]
                print(choice(response1))
            if user_input1 in Exit:
                print("Thanks,",conc_name1," for using PopChat. See you again soon!")
                break
    else:
        print("Thanks,",conc_name1," for using PopChat. See you again soon!")
email() 
