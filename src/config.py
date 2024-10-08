from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}

    if parser.has_section(section):
        print(section)
        params = parser.items(section)

        for param in params:
            db[param[0]] = param[1]
        else:
            raise Exception("Раздел {0} не найдено в {1} файл".format(section, filename))
    db['user'] = 'postgres'
    db['password'] = 'iLmF-13.'
    return db
