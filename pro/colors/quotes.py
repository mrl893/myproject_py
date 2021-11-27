
quotes = "mkkdopkowoikdkdlkldkkjsjdbuygsuihdjsndjknjd."
with open("quotes.txt", "w", encoding="utf-8") as favorite_quotes:
    favorite_quotes.write(quotes)
    for quotes in quotes:
        quotes.format()
        print(quotes)
