# get user email
email = input("What's your email?: ").strip()

# slice user name
user = email[:email.index("@")]

# slice domain
domain = email[(email.index("@")+1):]

# format message
output = "Your username is {}, and your domain is {}".format(user, domain)

# display outpout
print(output)
