import time
import requests
import card
import re


def call_random_api(params):
    payload = params
    response = requests.get(
        "https://api.scryfall.com/cards/random",
        params=payload,
        verify=True
    )
    time.sleep(0.01)
    return response


def generate_commander():
    response = call_random_api({
        "q": "type:creature type:legendary game:paper", "format": "json"
    })
    commander = card.Card(response.json())
    print(commander.generate_name())
    print("1 Worldknit")
    return commander.get_color_id()


def generate_spells(colors):
    regex_search = re.findall("[A-Z]", colors)
    colors_string = "".join(regex_search)
    response = call_random_api({
        "q": f"id:{colors_string} -type:land game:paper", "format": "json"
    })
    spell = card.Card(response.json())
    print(spell.generate_name())
    return


def generate_lands():
    print("40 Wastes")
    return


def main():
    inpt = ""
    while True:
        inpt = input("Press enter to generate a list, or type exit to exit > ")
        if inpt == "exit":
            break
        else:
            pass
        color_id = generate_commander()
        print()
        for i in range(59):
            generate_spells(color_id)
        print()
        generate_lands()
    return


if __name__ == "__main__":
    main()
