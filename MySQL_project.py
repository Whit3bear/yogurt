# Импортируем библиотеку для соединения с MySQL
import mysql.connector

# Проходим аутентификацию
my_db = mysql.connector.connect(
    host = "localhost",
    user = "Nata",
    passwd = "MySuperPassword2019"    
)
# Создаем курсор для выполнения запросов
my_cursor = my_db.cursor()

# Создаем базу
my_cursor.execute("CREATE DATABASE nata_python")

# Создаем таблицу и колонки
my_cursor.execute("CREATE TABLE nata_python.my_table (`number` INT NOT NULL AUTO_INCREMENT, `datetime` DATETIME NULL, `result` VARCHAR(25) NULL, `quote` VARCHAR(125) NULL, `etc` VARBINARY(225) NULL, PRIMARY KEY (`number`));")
