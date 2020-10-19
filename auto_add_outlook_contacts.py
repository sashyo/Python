import extract_msg
import sys
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


#reads .msg file
msg = extract_msg.openMsg('test.msg')




contact = msg.sender
#split name and email address
splitContact = contact.split('<')
contactName = splitContact[0]
contactEmail = splitContact[1].replace('>','')

# Find Telephone number , grabs first number found . Wont grab second telephone number e.g. FAX
contactPhone = re.search("(\+\d{2}\s\d{1}\s\d{4}\s\d{4})|(\d{2}\s\d{4}\s\d{4})|(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})",msg.body)
contactPhone =(contactPhone[0])

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
ContactItem.Save()




    







