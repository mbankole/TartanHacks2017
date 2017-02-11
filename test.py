import Database_Ops
cnx = Database_Ops.get_cnx()
Database_Ops.init(cnx)
Database_Ops.add_location("wow3", 335235, 232522.2, [
        {
            'name':'adjacent name',
            'distance':2525,
        },
        {
            'name':'adjacent name',
            'distance':2525,
        }],cnx)
print(Database_Ops.get_locations(cnx))