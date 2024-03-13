from . import Operasi

def delete_console():
    read_console()
    while(True):
        print("Silahkan pilih nomor music yang akan di delete")
        no_music = int(input("Nomor music: "))
        data_music = Operasi.read(index = no_music)

        if data_music:
            data_break = data_music.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            artist = data_break[2]
            title = data_break[3]
            year = data_break[4][:-1]

    
            # data yang ingin diupdate
            print("\n"+"="*100)
            print("Data yang ingin anda Hapus")
            print(f"1. title\t: {title:.40}")
            print(f"2. artist\t: {artist:.40}")
            print(f"3. year\t: {year:4}")
            is_done = input("Apakah anda yakin (y/n)? ")
            if is_done == "y" or is_done == "Y":
                Operasi.delete(no_music)
                break
        else:
            print("nomor tidak valid, silahkan masukan lagi")

    print("Data berhasil di hapus")

            
def update_console():
    read_console()
    while(True):
        print("Silahkan pilih nomor music yang akan di update")
        no_music = int(input("Nomor music: "))
        data_music = Operasi.read(index=no_music)

        if data_music:
            break
        else:
            print("nomor tidak valid, silahkan masukan lagi")
    
    data_break = data_music.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    artist = data_break[2]
    title = data_break[3]
    year = data_break[4][:-1]
    
    while(True):
        # data yang ingin diupdate
        print("\n"+"="*100)
        print("Silahkan pilih data apa yang ingin anda ubah")
        print(f"1. title\t: {title:.40}")
        print(f"2. artist\t: {artist:.40}")
        print(f"3. year\t: {year:4}")

        # memilih mode untuk update
        user_option = input("Pilih data [1,2,3]: ")
        print("\n"+"="*100)
        match user_option:
            case "1": title = input("title\t: ")
            case "2": artist = input("artist\t: ")
            case "3": 
                while(True):
                    try:
                        year = int(input("year\t: "))
                        if len(str(year)) == 4:
                            break
                        else:
                            print("year harus angka, silahkan masukan year lagi (yyyy)")    
                    except:
                        print("year harus angka, silahkan masukan year lagi (yyyy)")
            case _: print("index tidak cuocuoook")

        print("Data baru anda")
        print(f"1. title\t: {title:.40}")
        print(f"2. artist\t: {artist:.40}")
        print(f"3. year\t: {year:4}")
        is_done = input("Apakah data sudah sesuai(y/n)? ")
        if is_done == "y" or is_done == "Y":
            break
    
    Operasi.update(no_music,pk,data_add,year,title,artist)
            


def create_console():
    print("\n\n"+"="*100)
    print("Silahkan tambah data music\n")
    artist = input("artist\t: ")
    title = input("title\t: ")
    while(True):
        try:
            year = int(input("year\t: "))
            if len(str(year)) == 4:
                break
            else:
                print("year harus angka, silahkan masukan year lagi (yyyy)")    
        except:
            print("year harus angka, silahkan masukan year lagi (yyyy)")

    Operasi.create(year,title,artist)
    print("\nBerikut adalah data baru anda")
    read_console()

def read_console():
    data_file = Operasi.read()
    
    index = "No"
    title = "title"
    artist = "artist"
    year = "year release"

    # Header
    print("\n"+"="*110)
    print(f"{index:4} | {title:40} | {artist:40} | {year:5}")
    print("-"*110)
    
    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        if len(data_break) < 5:
            print(data)  # Add this line to check if there's incomplete data
            continue
        pk = data_break[0]
        date_add = data_break[1]
        artist = data_break[2]
        title = data_break[3]
        year = data_break[4]
        print(f"{index+1:4} | {title:.40} | {artist:.40} | {year:4}",end="")

    # Footer
    print("="*110+"\n")