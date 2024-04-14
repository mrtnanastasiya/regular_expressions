import csv
import re
from pprint import pprint
def fix_names(contacts_list):
    for contact in contacts_list:
        fullname = " ".join(contact[0:3]).split()
        contact[0] = fullname[0]
        contact[1] = fullname[1]
        if len(fullname) == 3:
            contact[2] = fullname[2]
    return contacts_list

def fix_phones(contacts_list):
    phone_pattern = re.compile(
        r'(\+7|8)?\s*\(?(\d{3})\)?\s*\W?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    phone_substitution = r'+7(\2)\3-\4-\5\7\8\9'

    for contact in contacts_list:
        contact[5] = phone_pattern.sub(phone_substitution, contact[5])

    return contacts_list

def fix_duplicates(contacts_list):
    uni_contacts = {}
    for contact in contacts_list[1:]:
        key = contact[0] + contact[1]
        if key in uni_contacts:
            for i in range(0, len(contact)):
                if uni_contacts[key][i] == '':
                    uni_contacts[key][i] = contact[i]
        else:
            uni_contacts[key] = contact
    result_list = list(uni_contacts.values())

    return result_list


if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding="utf-8") as in_file:
        rows = csv.reader(in_file, delimiter=",")
        contacts_list = list(rows)
        header = contacts_list[0]
        contacts_list2 = fix_names(contacts_list)
        contacts_list3 = fix_phones(contacts_list2)
        result_list = fix_duplicates(contacts_list3)

    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows([header] + result_list)



