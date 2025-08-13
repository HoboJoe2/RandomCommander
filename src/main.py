import time
import requests


def call_random_api(params):
    payload = params
    response = requests.get(
        "https://api.scryfall.com/cards/random",
        params=payload,
        verify=True
    )
    time.sleep(0.1)
    return response


def generate_spell():
    response = call_random_api({
        "q": f"-type:land legal:vintage -name:'Garth One-Eye'", "format": "json"
    })
    spell = response.json()["name"]
    print(f"1 {spell}")
    return


def generate_lands():
    print("1 Arid Mesa")
    print("1 Ash Barrens")
    print("1 Badlands")
    print("1 Bayou")
    print("1 Bloodstained Mire")
    print("1 City of Brass")
    print("1 Command Tower")
    print("1 Exotic Orchard")
    print("1 Flooded Strand")
    print("1 Indatha Triome")
    print("1 Jetmir's Garden")
    print("1 Ketria Triome")
    print("1 Mana Confluence")
    print("1 Marsh Flats")
    print("1 Misty Rainforest")
    print("1 Plateau")
    print("1 Polluted Delta")
    print("1 Raffine's Tower")
    print("1 Raugrin Triome")
    print("1 Savai Triome")
    print("1 Savannah")
    print("1 Scalding Tarn")
    print("1 Scrubland")
    print("1 Snow-Covered Forest")
    print("1 Snow-Covered Island")
    print("1 Snow-Covered Mountain")
    print("1 Snow-Covered Plains")
    print("1 Snow-Covered Swamp")
    print("1 Spara's Headquarters")
    print("1 Taiga")
    print("1 Tropical Island")
    print("1 Tundra")
    print("1 Underground Sea")
    print("1 Verdant Catacombs")
    print("1 Volcanic Island")
    print("1 Windswept Heath")
    print("1 Wooded Foothills")
    print("1 Xander's Lounge")
    print("1 Zagoth Triome")
    print("1 Ziatora's Proving Ground")
    return

def main():
    inpt = ""
    while True:
        inpt = input("Press enter to generate a list, or type exit to exit > ")
        if inpt == "exit":
            break
        else:
            pass
        for _ in range(59):
            generate_spell()
        generate_lands()
    return


if __name__ == "__main__":
    main()
