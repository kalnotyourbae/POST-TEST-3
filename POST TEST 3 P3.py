from prettytable import PrettyTable
import os
import time
import getpass
os.system("cls")

#Ini function untuk memberikan delay sejenak 
def cleardelay():
    os.system("cls")
    time.sleep(0.8)

class Game:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        self.next = None

class GameStore:
    def __init__(self):
        self.head = None
        #history sama dengan list kosong yang nantinya akan terisi
        self.history = []

    #function menambah game
    def add_game(self, game):
        if self.head is None:
            self.head = game
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = game
        self.history.append(('add', game.name, game.price, game.stock))

    #function menghapus game
    def remove_game(self, name):
        if self.head is None:
            return
        elif self.head.name == name:
            self.head = self.head.next
            self.history.append(('remove', name))
            return
        current = self.head
        while current.next is not None:
            if current.next.name == name:
                current.next = current.next.next
                self.history.append(('remove', name))
                return
            current = current.next

    #function menampilkan game
    def show_games(self):
        table = PrettyTable()
        table.title = "Game Tersedia"
        table.field_names = ["Nama Game", "Harga", "Stok"]
        if self.head is None:
            print("Daftar Game yang Tersedia Masih Kosong")
        else:
            current = self.head
            while current is not None:
                table.add_row([current.name, current.price, current.stock])
                current = current.next
            print(table)

    #function menampilkan history
    def show_history(self):
        table = PrettyTable()
        table.field_names = ["Keterangan", "Nama Game", "Harga", "Stok"]
        for item in self.history:
            if item[0] == 'add':
                table.add_row(['Ditambahkan', item[1], item[2], item[3]])
            elif item[0] == 'remove':
                table.add_row(['Dihapus', item[1], '-', '-'])
        print(table)

store = GameStore()
game1 = Game("Assassin Creed Origin", 60, 10)
game2 = Game("Forza Horizon 4", 55, 10)
game3 = Game("God of War IV", 50, 10)
store.add_game(game1)
store.add_game(game2)
store.add_game(game3)

def login():
    while True :
        username = input("Input Username Anda: ")
        password = getpass.getpass("Input Password Anda: ")
        # Validasi username dan password

    # Main program
        if username == "admin" and password == "11233":
            while True:
                os.system("cls")
                print("<><><><><> Welcome To My Game Store <><><><><>")
                print(" <><><><><>  Game   Store   Menu   <><><><><>")
                print("1. Tampilkan Game Yang Tersedia")
                print("2. Tambahkan Game Baru ke dalam List")
                print("3. Hapus Game Dari List")
                print("4. Tampilkan History")
                print("5. Exit")
                choice = input("Input Opsi (1-5): ")
                if choice == '1':
                    cleardelay()
                    store.show_games()
                    input("Tekan Enter Untuk Lanjut...")
                elif choice == '2':
                    name = input("Input Nama Game : ")
                    price = input("Input Harga : ")
                    stock = input("Input Jumlah Stok : ")
                    game = Game(name, price, stock)
                    store.add_game(game)
                    cleardelay()
                    print("Game Baru Berhasil Ditambahkan")
                    input("Tekan Enter Untuk Lanjut...")
                elif choice == '3':
                    name = input("Masukan Judul Game yang Ingin Dihapus : ")
                    store.remove_game(name)
                    cleardelay()
                    print("Game Telah Berhasil Dihapus")
                    input("Tekan Enter Untuk Lanjut...")
                elif choice == '4':
                    cleardelay()
                    store.show_history()
                    input("Tekan Enter Untuk Lanjut...")
                elif choice == '5':
                    raise SystemExit
                else:
                    print("Invalid choice, please try again")
                    time.sleep(0.8)
        else :
            print("Invalid Login")
login()