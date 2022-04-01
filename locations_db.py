import mariadb

def create_connetcion():
    conn = mariadb.connect(
        user="locations",
        password="locations",
        host="localhost",
        port=3306,
        database="locations"

    )
    return conn

def delete_all_locations():
    conn = create_connetcion()
    cur = conn.cursor()
    cur.execute("delete from location")
    conn.commit()

def create_location(name_prefix,coords):
   conn = create_connetcion()
   cur = conn.cursor()
   parts = coords.split(",")
   lat=parts[0]
   lon=parts[1]
   cur.execute("insert into location(name,lat,lon) values(?,?,?)", (name_prefix,lat,lon)) 
   conn.commit()


if __name__ == "__main__":
    delete_all_locations()
    create_location("Hello","1,1")
    create_location("World","2,2")
    conn = create_connetcion()

    cur = conn.cursor()
    cur.execute("SELECT id,name,lat,lon from location")

    for id,name,lat,lon in cur:
        print(f"{id} - {name} - {lat}, {lon}")

