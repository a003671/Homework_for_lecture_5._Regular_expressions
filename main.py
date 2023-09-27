from repair.repair_book import RepairAddrBook



if __name__ == '__main__':
    book = RepairAddrBook()
    contacts_list = book.receiving_data()
    book.write_by_column(contacts_list)
    contacts_list = book.del_duplicat(contacts_list)
    contacts_list = book.phones_normalize(contacts_list)
    book.save_file(contacts_list)