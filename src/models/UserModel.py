from database.db import get_connection
from .entities.User import User


class UserModel():

    @classmethod
    def get_users(self):
        try:
            connection = get_connection()
            users = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nombre, apellido, rut, cargo, descripcion, pais, ciudad, postal, celular, correo FROM public.user")
                resultset = cursor.fetchall()

                for row in resultset:
                    user = User(row[0], row[1], row[2], row[3], row[4],
                                row[5], row[6], row[7], row[8], row[9], row[10])
                    users.append(user.to_JSON())

            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nombre, apellido, rut, cargo, descripcion, pais, ciudad, postal, celular, correo FROM public.user WHERE id = %s", (id,))
                row = cursor.fetchone()

                user = None
                if row != None:
                    user = User(row[0], row[1], row[2], row[3], row[4],
                                row[5], row[6], row[7], row[8], row[9], row[10])
                    user = user.to_JSON()

            connection.close()
            return user
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO public.user (id, nombre, apellido, rut, cargo, descripcion, pais, ciudad, postal, celular, correo) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (user.id, user.nombre, user.apellido, user.rut, user.cargo,
                                                                                         user.descripcion, user.pais, user.ciudad, user.postal, user.celular, user.correo))

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE public.user SET nombre = %s, apellido = %s, rut = %s, cargo = %s, descripcion = %s, pais = %s, 
                                                            ciudad = %s, postal = %s, celular = %s, correo = %s
                                WHERE id = %s""", (user.nombre, user.apellido, user.rut, user.cargo,
                                                   user.descripcion, user.pais, user.ciudad, user.postal, user.celular, user.correo, user.id))

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM public.user WHERE id = %s", (user.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
