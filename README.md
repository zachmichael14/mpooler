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
    cards with Disperse and Dispersal in the name.
- Ask to save before closing if any cards in detection
- For collection management, robust filtering
- Populate with Scryfall data
- Add attribute to card data for physical location within collection
- Possibly add condition? I'm not sure there's a great way to automate this, but it could be nice to have
- A SQLite DB should be enough for most collections? This would support collection management nicely
