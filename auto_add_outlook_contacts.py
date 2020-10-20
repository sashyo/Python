import extract_msg
import re
import win32com.client
import pywintypes

contact = ''
contactName = ''
contactEmail = ''
contactPhone = ''
contactMob = ''
contactAddress = ''
contactFax = ''
emailbody= ' '
signature=''
address=''
temp = ''
addressNo=0


#reads .msg file
msg = extract_msg.openMsg('test.msg')
contact = msg.sender
#split name and email address
splitContact = contact.split('<')
#removes any whitespace to match with text in bosy
contactName = re.search("(^(\w+)(\-|\s)(\w+))",splitContact[0])
contactName = contactName[0].strip()
contactEmail = splitContact[1].replace('>','')

emailBody,temp,signature = msg.body.partition(contactName)

# Find Telephone number , grabs first number found . Wont grab second telephone number e.g. FAX
contactPhone = re.search("(\+\d{2}\s\d{1}\s\d{4}\s\d{4})|(\d{2}\s\d{4}\s\d{4})|(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})",signature)
contactPhone =(contactPhone[0])
print(contactPhone)

#find first address

testAddress = signature.split('\n')
x = 0;
while(x < len(testAddress)):
    temp = re.search("([A-Z]{3}(\s\d{4}|\,\d{4}|\s\,\d{4}|\,\s\d{4}))", testAddress[x])
    if temp is None:
        x+=1
    else:
        addressNo= x
        break

address = re.search("([A-Z]{3}(\s\d{4}|\,\d{4}|\s\,\d{4}|\,\s\d{4}))", testAddress[addressNo])
address= address[0]


'''address = re.search("([A-Z]{3}(\s\d{4}|\,\d{4}|\s\,\d{4}|\,\s\d{4}))", signature)
address = address[0]
print(address)'''

contactAddress,address,temp = testAddress[addressNo].partition(address)
contactAddress = contactAddress + address




#open outlook
o = win32com.client.Dispatch("Outlook.Application")
ns = o.GetNamespace("MAPI")

contactsFolder=ns.GetDefaultFolder(10)
contacts = contactsFolder.Items

#create contacts , add name, email addres and work phone number
ContactItem = contactsFolder.Items.Add("IPM.Contact")
ContactItem.FullName = contactName
ContactItem.Email1Address = contactEmail
ContactItem.BusinessTelephoneNumber = contactPhone
ContactItem.BusinessAddress = contactAddress
ContactItem.Save()

#
#([^EIOU]{3})(\s\d{4}|\,\d{4}|\s\,\s\d{4}|\,\s\d{4})

msg.close()
    







