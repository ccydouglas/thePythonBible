email=input("What is your email address?")

username=email[:email.index("@"):1]

domain= email[email.index("@")+1:]

output= "Your user name is {} and your domain name is {}".format(username,domain)

print(output)
