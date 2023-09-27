from itertools import chain
import csv
import re


class RepairAddrBook:
    def receiving_data(self, file_name='phonebook_raw.csv'):
        with open(file_name, encoding='utf-8') as f:
            rows = csv.reader(f)
            contacts_list = list(rows)
        return contacts_list

    def write_by_column(self, contacts_list):
        for el in contacts_list[1:]:
            new_list = ' '.join(el[:3]).split()
            for index, value in enumerate(new_list):
                el[index] = value
        return contacts_list

    def del_duplicat(self, contacts_list):
        new_list = []
        for data in contacts_list:
            if data[0] and data[1] not in list(chain(*new_list)):
                new_list.append(data)
            else:
                for id, elem in enumerate(new_list):
                    if elem[0] == data[0] and elem[1] == data[1]:
                        for index, el in enumerate(elem):
                            if el == '':
                                elem[index] = data[index]
                    new_list[id] = elem
        return new_list
    
    def phones_normalize(self, contacts_list):
        pattern = r'(\+7|7|8)[\s|-]*\(?(\d{1,3})\)?[\s|-]*(\d{1,3})[\s|-]*(\d{2})[\s|-]*(\d{2})[\s|\(]*(\w+\.\s\d+)?\)?'
        for contacts in contacts_list:
            r = re.sub(pattern, r'+7(\2)\3-\4-\5 \6', contacts[5])
            contacts[5] = r.strip(' ')
        return contacts_list
    
    def save_file(self, contacts_list, file_name='phonebook.csv'):
        with open(file_name, 'w', encoding='utf-8', newline='') as f:
            datawriter = csv.writer(f, delimiter=',')
            datawriter.writerows(contacts_list)

if __name__ == '__main__':
    RepairAddrBook()