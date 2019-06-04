def Phone_contacts(print_contacts):

    def print_numbers(numbers):                             #1.CONTACTS
        print("Telephone Numbers:")
        for x in numbers.keys():
            print("Name:", x, "\tNumber:", numbers[x])
        print

    def add_number(numbers, name, number):
        numbers[name] = number

    def search_number(numbers, name):
        if name in numbers:
            return "The number is " + numbers[name]
        else:
            return name + " was not found"

    def remove_number(numbers, name):
        if name in numbers:
            del numbers[name]
        else:
            print(name + " was not found")

    def load_numbers(numbers, filename):
        in_file = open(filename, "r")
        for in_line in in_file:
            in_line = in_line.rstrip('\n')     
            name, number = in_line.split(",")
            numbers[name] = number
        in_file.close()

    def save_numbers(numbers, filename):
        out_file = open(filename, "w")
        for x in numbers.keys():
            out_file.write(x + "," + numbers[x] + "\n")
        out_file.close()

    def print_contacts():
        print('1. Print Phone Numbers')
        print('2. Add a Phone Number')
        print('3. Delete Phone Number')
        print('4. Search Phone Number')
        print('5. Load numbers')
        print('6. Save numbers')
        print('7. Quit')
        print

    phone_list = {}
    contacts_choice = 0
    print_contacts()
    while True:
        contacts_choice = int(raw_input("Type in a number (1-7): "))
        if contacts_choice == 1:
            print("Phonebook List:")
            print_numbers(phone_list)
        elif contacts_choice == 2:
            print("Add Name and Number")
            name = raw_input("Name: ")
            phone = raw_input("Number: ")
            add_number(phone_list, name, phone)
        elif contacts_choice == 3:
            print("Number(s) to Delete:")
            name = raw_input("Name: ")
            remove_number(phone_list, name)
        elif contacts_choice == 4:
            print("Number(s) to search:")
            name = raw_input("Name: ")
            print(search_number(phone_list, name))
        elif contacts_choice == 5:
            filename = raw_input("Filename to load: ")
            load_numbers(phone_list, filename)
        elif contacts_choice == 6:
            filename = raw_input("Filename to save: ")
            save_numbers(phone_list, filename)
        elif contacts_choice == 7:
            break
        else:
            print_contacts()

    print("Goodbye")

def internet(print_internet):                                   #2.INTERNET
    def print_internet():                                      
        
        print('1. Google')
        print('2. Yahoo')
        print('3. AOL')
        print('4. DuckDuckGo')
        print('5. Bing')
        print('6. Ask')
        print('7. Baidu')
        print('8. Wolfram Alpha')   
        print('9. Quit')
        print

    import webbrowser
    webPage_choice = 0
    print_internet()
    while True:
        webPage_choice = int(raw_input("Choose from the above (1-9): "))
        if webPage_choice == 1:
            webbrowser.open("https://www.google.com/")
        elif webPage_choice == 2:
            webbrowser.open("https://uk.yahoo.com/")
        elif webPage_choice == 3:
            webbrowser.open("https://www.aol.com/")
        elif webPage_choice == 4:
            webbrowser.open("https://duckduckgo.com/")
        elif webPage_choice == 5:
            webbrowser.open("https://www.bing.com/")
        elif webPage_choice == 6:
            webbrowser.open("https://www.ask.com/")
        elif webPage_choice == 7:
            webbrowser.open("https://www.baidu.com/")
        elif webPage_choice == 8:
            webbrowser.open("https://www.wolframalpha.com/")   
        elif webPage_choice == 9:
            break
        else:
            print_internet()

    print("Goodbye")

def media_player(print_mediaPlayer):                        #3.MEDIAPLAYER

    def print_music(music):
        print("Music List:")
        for x in music.keys():
            print("Artist:", x, "\tSong:", music[x])
        return

    def add_music(music, artist, song):
        music[artist] = song

    def save_music(music, musicLibrary):
        outfile = open(musicLibrary, 'w')
        for x in music.keys():
            outfile.write(x + "," + music[x] + "\n")
        outfile.close()

    def load_music(music, musicLibrary):
        infile = open(musicLibrary, 'r+')
        for in_line in infile:
            in_line = in_line.rstrip('\n')
            artist, song = in_line.split(",")
            music[artist] = song
        infile.close()

    def search_music(music, artist):
        if artist in music:
            return("Artist: " + artist + "\tSong: " + music[artist])
        else:
            return(music[artist] + " cannot be found.")

    def play_music(music):
        from playsound import playsound
        playsound(music[artist])

    def delete_song(music, song):
        if artist in music:
            del music[artist]
        else:
            print(music[artist] + " not found.")
            
    def delete_artist(music, artist):
        if artist in music:
            del artist
        else:
            print(artist + " not found.")
        
    def print_mediaPlayer():

        print("1.Print Music")
        print("2.Add Music")
        print("3.Save Music")
        print("4.Load Music")
        print("5.Search Music")
        print("6.Play Music")
        print("7.Delete song")
        print("8.Delete Artist")
        print("9.Quit")
        print

    MP_menu_choice = 0
    MP_list = {}
    print_mediaPlayer()
    while True:
        MP_menu_choice = int(raw_input("Enter choices 1-8:"))
        if MP_menu_choice == 1:
            print("Music Library List:")
            print_music(MP_list)
        elif MP_menu_choice == 2:
            print("Add Artist Name & Song Name:")
            artist = raw_input("Enter Artist Name:")
            song = raw_input("Enter full song name under 'Properties':")
            add_music(MP_list, artist, song)
        elif MP_menu_choice == 3:
            filename = raw_input("Enter new filename to Save:")
            save_music(MP_list, filename)
        elif MP_menu_choice == 4:
            filename = raw_input("Filename to Load:")
            load_music(MP_list, filename)
        elif MP_menu_choice == 5:
            print("Search Songs(s):")
            artist = raw_input("Enter Artist(s) Name:")
            search_music(MP_list, artist)
        elif MP_menu_choice == 6:
            print_music(MP_list)
            print("Select the song you wish to play:")
            artist = raw_input("Enter Artist Name:\nOr enter 'Q' to return to main menu:")
            if artist == "Q":
                continue
            song = raw_input("Enter Song Name:\nOr enter 'Quit' to return to main menu:")
            if song == "Q":
                continue
            add_music(MP_list, artist, song)
            play_music(MP_list)
            continue
        elif MP_menu_choice == 7:
            print("Song(s) to delete:")
            artist = raw_input("Select which song you wish to delete:")                                     ##Work on music Deletion##
            delete_song(MP_list, artist)
        elif MP_menu_choice == 8:
            print("Artist(s) to delete:")
            artist = raw_input("Select which artist you wish to delete:")
            delete_artist(MP_list, artist)
        elif MP_menu_choice == 9:
            break
        else:
            print_mediaPlayer()


def gallery(print_gallery):                                 #4.GALLERY

    def print_photos(photos):
        print("Photos")
        for x in photos.keys():
            print("Photo Name:", x, "\tDate:", photos[x])
        print

    def add_photos(photos, photoName, photoDate):
         photos[photoName] = photoDate

    def save_photos(photos, filename):
        out_file = open(filename, "w")
        for x in photos.keys():
            print(x + "," + photos[x] + "\n")
        out_file.close()

    def load_photos(photos, filename):
        in_file = open(filename, "r+")
        for in_line in in_file:
            in_line = in_line.rstrip("\n")
            photos[photoName] = in_line.split(",")
            photos[photoName] = photoDate
        in_file.close()

    def search_photos(photos, photoName):
        if photoName in photos:
            print "Photo name: " + photos[photoName]
        else:
            print name + " cannot be found."

    def display_photos(photoName):
        import PIL
        from PIL import Image
        import webbrowser
        webbrowser.open(photoName)

    def delete_photos(photos, photoName):
        if photoName in photos:
            del photos[photoName]
        else:
            print photoName + "cannot be found."
            

    def print_gallery():
        print('1. Print Photos')
        print('2. Add Photo')
        print('3. Save Photo')
        print('4. Load Photo')
        print('5. Search Photo')
        print('6. Display Photo')
        print('7. Delete Photo')
        print('8. Quit')
        print

    photoList = {}
    photoChoice = 0
    print_gallery()
    while True:
        photoChoice = int(raw_input("Enter menu choices 1-8:"))
        if photoChoice == 1:
            print("Photo Gallery List:")
            print_photos(photoList)
        elif photoChoice == 2:
            print("Add Photo Name and Date:")
            imgName = raw_input("Name i.e. 'name.jpg':")
            imgDate = raw_input("Date i.e. dd/mm/yy:")
            add_photos(photoList, imgName, imgDate)
        elif photoChoice == 3:
            filename = raw_input("Filename to save:")
            save_photos(photoList, filename)
        elif photoChoice == 4:
            filename = raw_input("Filename to load:")
            load_photos(photoList, filename)
        elif photoChoice == 5:
            print("Photo(s) to search:")
            imgName = raw_input("Enter Photo Name i.e. name.jpg:")
            search_photos(photoList, imgName)
        elif photoChoice == 6:
            print("Photo(s) to display:")
            imgName = raw_input("Enter Photo Name i.e. name.jpg:")
            display_photos(imgName)
        elif photoChoice == 7:
            print("Photo(s) to delete:")
            imgName = raw_input("Enter Photo Name i.e. name.jpg:")
            delete_photos(photoList, imgName)
        elif photoChoice == 8:
            break
        else:
            print_gallery()


def print_menu():
    print('1. Contacts')
    print('2. Safari')
    print('3. Media Player')
    print('4. Gallery')
    print

menu_list = {}
menu_choice = 0
print_menu
while True:
    menu_choice = int(raw_input("Enter menu choice 1-4:\n 1. Contacts\n 2. Safari\n 3. MediaPlayer\n 4. Gallery\n\n"))
    if menu_choice == 1:
        print("Contacts:")
        Phone_contacts(menu_list)
    elif menu_choice == 2:
        print("Safari:")
        internet(menu_list)
    elif menu_choice == 3:
        print("Media Player:")
        media_player(menu_list)
    elif menu_choice == 4:
        print("Gallery:")
        gallery(menu_list)
