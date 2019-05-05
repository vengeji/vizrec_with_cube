from partial_order import execute
if __name__ == '__main__':
    execute('', 'localhost', '3306', 'root', 'root', 'test',
            'websales2005_season1', "SELECT * FROM sales",
            'price', 'itemname', 'itemdesc', 'category', "solddate", 'quantity',
            'double', 'varchar', 'varchar(255)', 'varchar(255)', 'date', 'int')