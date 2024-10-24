import mysql.connector

class DataBase:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host='localhost', user='root', password='', database='DocGenerator')
            self.mycourser = self.conn.cursor()
        except Exception as e:
            print(f"Not Connected Successfully: {e}")
        else:
            print("Connected Successfully, Thanks!")

    def alreadyExistuser(self, email):
        self.mycourser.execute('SELECT * FROM Accounts WHERE Email = %s', (email,))
        return self.mycourser.fetchone()

    def get_u_id(self, email):
        self.mycourser.execute("SELECT u_id FROM Accounts WHERE Email=%s", (email,))
        result = self.mycourser.fetchone()
        return result[0] if result else None

    def insert_private_template(self, Templatename, PageSize, Orientation, Margin, Columns1,
                                FontStyle, FontSize, FontColor, FontStyling, TextAlign, LineSpacing,
                                ParaSpacing, PageNumber, CustomHeader, Indentation, TabStops,
                                BulletPoints, NumberedLists, TableBorder, RowsAndColumns,
                                TextAlignment, tableofcontent, u_template_id):
        insert_query = """
            INSERT INTO PrivateTemplates 
            (TemplateName, PageSize, Orientation, Margin, Columns1, FontStyle, FontSize, FontColor, 
            FontStyling, TextAlign, LineSpacing, ParaSpacing, PageNumber, CustomHeader, Indentation, 
            TabStops, BulletPoints, NumberedLists, TableBorder, RowsAndColumns, TextAlignment, Tableofcontent, u_template_id) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (Templatename, PageSize, Orientation, Margin, Columns1, FontStyle, FontSize, FontColor,
                  FontStyling, TextAlign, LineSpacing, ParaSpacing, PageNumber, CustomHeader, Indentation,
                  TabStops, BulletPoints, NumberedLists, TableBorder, RowsAndColumns, TextAlignment,
                  tableofcontent, u_template_id)
        try:
            self.mycourser.execute(insert_query, values)
            self.conn.commit()
            print("Template inserted successfully!")
        except Exception as e:
            self.conn.rollback()
            print(f"An error occurred: {e}")
        finally:
            self.mycourser.close()
            print("Cursor closed.")

    def insert_public_template(self, Templatename, PageSize, Orientation, Margin, Columns1,
                               FontStyle, FontSize, FontColor, FontStyling, TextAlign, LineSpacing,
                               ParaSpacing, PageNumber, CustomHeader, Indentation, TabStops,
                               BulletPoints, NumberedLists, TableBorder, RowsAndColumns,
                               TextAlignment, tableofcontent, u_template_id):
        insert_query = """
            INSERT INTO PublicTemplates 
            (TemplateName, PageSize, Orientation, Margin, Columns1, FontStyle, FontSize, FontColor, 
            FontStyling, TextAlign, LineSpacing, ParaSpacing, PageNumber, CustomHeader, Indentation, 
            TabStops, BulletPoints, NumberedLists, TableBorder, RowsAndColumns, TextAlignment, Tableofcontent, u_template_id) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (Templatename, PageSize, Orientation, Margin, Columns1, FontStyle, FontSize, FontColor,
                  FontStyling, TextAlign, LineSpacing, ParaSpacing, PageNumber, CustomHeader, Indentation,
                  TabStops, BulletPoints, NumberedLists, TableBorder, RowsAndColumns, TextAlignment,
                  tableofcontent, u_template_id)
        try:
            self.mycourser.execute(insert_query, values)
            self.conn.commit()
            print("Template inserted successfully!")
        except Exception as e:
            self.conn.rollback()
            print(f"An error occurred: {e}")
        finally:
            self.mycourser.close()
            print("Cursor closed.")

    def delete_private_template(self, template_id):
        delete_query = "DELETE FROM PrivateTemplates WHERE t_id = %s"
        values = (template_id,)
        try:
            self.mycourser.execute(delete_query, values)
            self.conn.commit()
            if self.mycourser.rowcount > 0:
                print("Template deleted successfully!")
            else:
                print("No template found with the given ID.")
        except Exception as e:
            self.conn.rollback()
            print(f"An error occurred: {e}")
        finally:
            self.mycourser.close()
            print("Cursor closed.")

    def insert_data(self, name, email, password, phonenumber, country):
        self.mycourser.execute("INSERT INTO Accounts (u_id, Name, Email, Password, Phonenumber, Country) VALUES (NULL, %s, %s, %s, %s, %s)",
                               (name, email, password, phonenumber, country))
        self.conn.commit()

    def get_Private_template(self, u_id):
        self.mycourser.execute("SELECT * FROM PrivateTemplates WHERE u_template_id=%s", (u_id,))
        result = self.mycourser.fetchall()
        return result if result else None

    def get_Public_template(self):
        self.mycourser.execute("SELECT * FROM PublicTemplates WHERE 1")
        result = self.mycourser.fetchall()
        return result if result else None