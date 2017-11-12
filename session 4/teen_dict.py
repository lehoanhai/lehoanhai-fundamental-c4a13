teen_dict = {
    'hc':'hoc',
    'pt':'phat trien',
    'eny':'em nguoi yeu',
    'ngta':"nguoi ta",
    'cc':'cuc cung'
}
print(*teen_dict,sep='   ')
print('* '*30)
T = True
while T:
    qu = input('Your code? ')
    if qu in teen_dict:
        print('Code: ',qu)
        print('Translation: ',teen_dict[qu])
    else:
        nqu = input('Not found, do you want to contribute this word? (Y/N)? ').upper()
        if nqu == 'Y':
            ntl = input("Enter your tranlation: ")
            print('Updating...')
            print("*"*30)
            teen_dict[qu] = ntl
            print("*"*30)
            print(*teen_dict)
            print ('Lets search again')
        else:
            print ('Lets search again')
