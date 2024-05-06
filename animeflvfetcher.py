import animeflv.exception
import requests.exceptions
from animeflv import AnimeFLV


# This gives the links for every chapter from a serie
def give_serie_links(chapters, serie_name, server):
    with AnimeFLV() as api:
        finished = 0
        errors = 0
        while finished == 0:
            if errors >= 3:
                print("Too Many Errors! Stopping...")
                exit(1)
            try:
                for i in range(1, chapters + 1):
                    link_list = api.get_links(serie_name, i)
                    print(f"Chapter #{i}: " + str(link_list[server-1]) + "\n")
                    finished = 1
            except animeflv.exception.AnimeFLVParseError:
                print(f"Chapter #{i}: Parse Error or the chapter/serie doesn't exist, retrying...(Attempt {errors+1})")
                errors += 1
            except requests.exceptions.ConnectionError:
                print(f"Chapter #{i}: Connection Error, Retrying...(Attempt {errors+1})")
                errors += 1


# This gives the links for a specified start and end chapter of a serie
def give_sequence_links(start_point, end_point, serie_name, server):
    with AnimeFLV() as api:
        finished = 0
        errors = 0
        while finished == 0:
            if errors >= 3:
                print("Too Many Errors! Stopping...")
                exit(1)
            try:
                for i in range(start_point, end_point + 1):
                    link_list = api.get_links(serie_name, i)
                    print(f"Chapter #{i}: " + str(link_list[server-1]) + "\n")
                    finished = 1
            except animeflv.exception.AnimeFLVParseError:
                print(f"Chapter #{i}: Parse Error or the chapter/serie doesn't exist, retrying...(Attempt {errors+1})")
                errors += 1
            except requests.exceptions.ConnectionError:
                print(f"Chapter #{i}: Connection Error, Retrying...(Attempt {errors+1})")
                errors += 1


# This gives a unique chapter for a serie
def give_a_link(chapter_number, serie_name, server):
    with AnimeFLV() as api:
        finished = 0
        errors = 0
        while finished == 0:
            if errors >= 3:
                print("Too Many Errors! Stopping...")
                exit(1)
            try:
                for i in range(chapter_number, chapter_number + 1):
                    link_list = api.get_links(serie_name, i)
                    print(f"Chapter #{i}: " + str(link_list[server-1]))
                    finished = 1
            except animeflv.exception.AnimeFLVParseError:
                print(f"Chapter #{i}: Parse Error or the chapter/serie doesn't exist, retrying...(Attempt {errors+1})")
                errors += 1
            except requests.exceptions.ConnectionError:
                print(f"Chapter #{i}: Connection Error, Retrying...(Attempt {errors+1})")
                errors += 1


print("AnimeFLV Downloader!\nCreated by iWisp360\n")
print("Select an option: ")
print("1: Get every link for a serie")
print("2: Get links from a start point to an end point of a serie")
print("3: Get only one link from a serie, use this if you are fetching a movie")
print("Or enter any other key to exit")

try:
    option = int(input())
except ValueError:
    exit(0)

try:
    server = int(input("Which server do you want to use?(1- MEGA, 2- 1Fichier, 3- Stream Tape): "))
    while 1 > server > 3:
        print("Not a valid server, try again(1- MEGA, 2- 1Fichier, 3- Stape): ")
    # if 3 is passed to the get_links function in animeflv module it will give Zippyshare links, but
    # Zippyshare service is down permanently
    if server == 3:
        server = int(4)
except ValueError:
    print("Not A valid input, assuming 1...")
    server = int(1)

try:
    if option == 1:

        serie_name = input("Enter the serie ID(you can see it in the url of animeflv.net): ")
        chapters = input("How many chapters this series has?: ")
        print(give_serie_links(int(chapters), serie_name, server))

    elif option == 2:

        serie_name = input("Enter the serie ID(you can see it in the url of animeflv.net): ")
        start_point = input("Give a start point: ")
        end_point = input("Give an end point: ")
        print(give_sequence_links(int(start_point), int(end_point), serie_name, server))

    elif option == 3:

        serie_or_movie_name = input("Enter the serie or movie ID(you can see it in the url of animeflv.net): ")
        chapter = input("Which chapter do you want to download?: ")
        print(give_a_link(int(chapter), serie_or_movie_name, server))

    else:
        exit(0)
except ValueError:
    print("Looks Like you entered a character that is not a number, try again...")
