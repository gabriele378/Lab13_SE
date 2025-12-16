from database.DB_connect import DBConnect
from model.cromosoma import Cromosoma
from model.gene import Gene
from model.interazione import Interazione


class DAO:

    @staticmethod
    def read_cromosomi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT cromosoma FROM gene"""

        cursor.execute(query)

        for row in cursor:
            result.append(Cromosoma(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_geni():
        conn = DBConnect.get_connection()

        result = {}

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * from gene"""

        cursor.execute(query)

        for row in cursor:
            result.append(Gene(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_interazioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * from interazione"""

        cursor.execute(query)

        for row in cursor:
            result.append(Interazione(**row))

        cursor.close()
        conn.close()
        return result


