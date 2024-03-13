from time import time
from . import Database
from .Util import random_string
import time
import os

def delete(no_music):
    print(Database.DB_NAME)
    try:
        with open(Database.DB_NAME,'r') as file:
            counter = 0

            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_music - 1:
                    pass
                else:
                    with open("data_temp.txt",'a',encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("database error")
    
    # Delete existing data.txt file if it exists
    if os.path.exists('data.txt'):
        os.remove('data.txt')

    # Rename data_temp.txt to data.txt
    os.rename('data_temp.txt', 'data.txt')

def update(no_music,pk,data_add,year,title,artist):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["artist"] = artist + Database.TEMPLATE["artist"][len(artist):]
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["year"] = str(year)

    data_str = f'{data["pk"]},{data["date_add"]},{data["artist"]},{data["title"]},{data["year"]}\n'
    
    panjang_data = len(data_str)

    try:
        with open(Database.DB_NAME,'r+',encoding="utf-8") as file:
            file.seek(panjang_data*(no_music-1))
            file.write(data_str)
    except:
        print("error dalam update data")

def create(year,title,artist):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["artist"] = artist + Database.TEMPLATE["artist"][len(artist):]
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["year"] = str(year)

    data_str = f'{data["pk"]},{data["date_add"]},{data["artist"]},{data["title"]},{data["year"]}\n'
    
    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data sulit ditambahkan boooos, gagal maning")

def create_first_data():
    artist = input("artist: ")
    title = input("title: ")
    while(True):
        try:
            year = int(input("year\t: "))
            if len(str(year)) == 4:
                break
            else:
                print("year harus angka, silahkan masukan year lagi (yyyy)")    
        except:
            print("year harus angka, silahkan masukan year lagi (yyyy)")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["artist"] = artist + Database.TEMPLATE["artist"][len(artist):]
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["year"] = str(year)

    data_str = f'{data["pk"]},{data["date_add"]},{data["artist"]},{data["title"]},{data["year"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Udah lah Gagal")

def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_music = len(content)
            if "index" in kwargs:
                index_music = kwargs["index"]-1
                if index_music < 0 or index_music > jumlah_music:
                    return False
                else:    
                    return content[index_music]
            else:
                return content
    except:
        print("Membaca database error")
        return False
    