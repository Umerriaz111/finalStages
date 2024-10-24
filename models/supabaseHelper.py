from supabase import create_client, Client

class DataBase:
    def __init__(self):
        url = 'https://oisnwqukbdazqqvgrgww.supabase.co'
        key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9pc253cXVrYmRhenFxdmdyZ3d3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mjk0OTAzNjAsImV4cCI6MjA0NTA2NjM2MH0.duT-FOPGa0LcWgsQKRTKH9vscq25hR1sAtqdLpbKgOw'
        self.client = create_client(url, key)

    def alreadyExistuser(self, email):
        response = self.client.table('accounts').select('*').eq('email', email).execute()
        return response.data[0] if response.data else None
    
    def alreadyExistuserbyphonenumber(self, phonenumber):
        response = self.client.table('accounts').select('*').eq('phonenumber', phonenumber).execute()
        return response.data[0] if response.data else None

    def get_u_id(self, email):
        response = self.client.table('accounts').select('u_id').eq('email', email).execute()
        return response.data[0]['u_id'] if response.data else None

    def insert_private_template(self, Templatename, PageSize, Orientation, Margin, Columns1,
                                FontStyle, FontSize, FontColor, FontStyling, TextAlign, LineSpacing,
                                ParaSpacing, PageNumber, CustomHeader, Indentation, TabStops,
                                BulletPoints, NumberedLists, TableBorder, RowsAndColumns,
                                TextAlignment, tableofcontent, u_template_id):
        data = {
            'templatename': Templatename,
            'pagesize': PageSize,
            'orientation': Orientation,
            'margin': Margin,
            'columns1': Columns1,
            'fontstyle': FontStyle,
            'fontsize': FontSize,
            'fontcolor': FontColor,
            'fontstyling': FontStyling,
            'textalign': TextAlign,
            'linespacing': LineSpacing,
            'paraspacing': ParaSpacing,
            'pagenumber': PageNumber,
            'customheader': CustomHeader,
            'indentation': Indentation,
            'tabstops': TabStops,
            'bulletpoints': BulletPoints,
            'numberedlists': NumberedLists,
            'tableborder': TableBorder,
            'rowsandcolumns': RowsAndColumns,
            'textalignment': TextAlignment,
            'tableofcontent': tableofcontent,
            'u_template_id': u_template_id
        }
        response = self.client.table('privatetemplates').insert(data).execute()
        print("###############")
        print(response)
        print("###############")
        if response is not None:
            print("Template inserted successfully!")
        else:
            print("Template Not inserted SuccessFully")

    def insert_public_template(self, Templatename, PageSize, Orientation, Margin, Columns1,
                               FontStyle, FontSize, FontColor, FontStyling, TextAlign, LineSpacing,
                               ParaSpacing, PageNumber, CustomHeader, Indentation, TabStops,
                               BulletPoints, NumberedLists, TableBorder, RowsAndColumns,
                               TextAlignment, tableofcontent, u_template_id):
        data = {
            'templatename': Templatename,
            'pagesize': PageSize,
            'orientation': Orientation,
            'margin': Margin,
            'columns1': Columns1,
            'fontstyle': FontStyle,
            'fontsize': FontSize,
            'fontcolor': FontColor,
            'fontstyling': FontStyling,
            'textalign': TextAlign,
            'linespacing': LineSpacing,
            'paraspacing': ParaSpacing,
            'pagenumber': PageNumber,
            'customheader': CustomHeader,
            'indentation': Indentation,
            'tabstops': TabStops,
            'bulletpoints': BulletPoints,
            'numberedlists': NumberedLists,
            'tableborder': TableBorder,
            'rowsandcolumns': RowsAndColumns,
            'textalignment': TextAlignment,
            'tableofcontent': tableofcontent,
            'u_template_id': u_template_id
        }
        response = self.client.table('publictemplates').insert(data).execute()
        if response is not None:
            print("Inserted Successfully")
        else:
            print("Not Inserted Due to Some Error")

    def delete_private_template(self, template_id):
        response = self.client.table('privatetemplates').delete().eq('t_id', template_id).execute()
        if response is not None:
            print("Inserted Successfully")
        else:
            print("Not Inserted Due to Some Error")

    def insert_data(self, name, email, password, phonenumber, country):
        data = {
            'name': name,
            'email': email,
            'password': password,
            'phonenumber': phonenumber,
            'country': country
        }
        response = self.client.table('accounts').insert(data).execute()
        return "Sucess"


    def get_Private_template(self, u_id):
        response = self.client.table('privatetemplates').select('*').eq('u_template_id', u_id).execute()
        return response.data if response.data else None

    def get_Public_template(self):
        response = self.client.table('publictemplates').select('*').execute()
        return response.data if response.data else None
