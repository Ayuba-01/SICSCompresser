from main import SICSCompresser

# Test with given example
text = ("Marley was dead: to begin with. There is no doubt whatever about that. The register of his burial was signed "
        "by the clergyman, the clerk, the undertaker, and the chief mourner. Scrooge signed it: and Scrooge’s name "
        "was good upon ’Change, for anything he chose to put his hand to. Old Marley was as dead as a door-nail. "
        "Mind! I don’t mean to say that I know, of my own knowledge, what there is particularly dead about a "
        "door-nail. I might have been inclined, myself, to regard a coffin-nail as the deadest piece of ironmongery "
        "in the trade. But the wisdom of our ancestors is in the simile; and my unhallowed hands shall not disturb "
        "it, or the Country’s done for. You will therefore permit me to repeat, emphatically, that Marley was as dead "
        "as a door-nail.")
sics_compressor = SICSCompresser()
compressed = sics_compressor.compress(text)
print(f"Compressed: {compressed}")

decompressed = sics_compressor.decompress(compressed)
print(f"Decompressed: {decompressed}")
