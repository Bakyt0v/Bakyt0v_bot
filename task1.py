
def Seishely():
    days = int(input('Enter the day: '))
    if days > 3 and days < 7:
        return (days * 40) - 20
    elif days >= 7:
        return(days * 40) - 50
    return days * 40
print(Seishely())