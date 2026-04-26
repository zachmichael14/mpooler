TODOs:
 - Tail detected cards field
 - Add tabs for detection, collection mgmt
 - Figure out a better way to prevent it from populating when the detection is incorrect.
    It's tedious to have to move the window to prevent text box population.
    Maybe some kind of yes/no system where if no it won't suggest that one again?
    This would require some knowledge of when the card is moved and that suggestion
    can be used again. Maybe it could populate a separate box with several suggestions?
    These suggestions could maybe be based on similarity score. For instance, the card "Disperse"
    often gets suggested if the name contains "Dispersal", so it should populate that box with
    cards with Disperse and Dispersal in the name. (Gravity Negator was consistently detected as Megatog,
    Hightide Hermit was detected as High Tide, Jeskai Windscout as Windscouter, as Glarecaster)
- Ask to save before closing if any cards in detection
- For collection management, robust filtering
- Populate with Scryfall data
- Add attribute to card data for physical location within collection
- Possibly add condition? I'm not sure there's a great way to automate this, but it could be nice to have
- For collection mgmt, a SQLite DB should be enough for most collections
- Ouptut the detected name above the card. Possibly hange from red top green maybe. That way it's easier to confirm correct detection
- If detection (enter is pressed, yes key is hit, whatever), the populated text shouldn't change until 
    the card in frame changes. Once agian, this would require detection of when the card in frame changes.
- For keywords, a JSON seeded datbase table might be the way to go since there is the json file of keywords.
    it would be instatiated on startup

Known limitations:
Your mileage may vary when scanning white text



Database