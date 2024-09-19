email = "benjamins@oomph.ac"
username = email[:9]
company = email[10:(len(email)-3)]

print("Email address: " + email)
print("Username: " + username)
print("Company: " + company.upper())