curMonth = input("Enter Month: ")

if curMonth.lower() == 'february':
    print("28 days")
elif curMonth.lower() in ['april', 'june', 'september', 'november']:
    print("30 days")
elif curMonth.lower() in ['may', 'july', 'october', 'december']:
    print("31 days")