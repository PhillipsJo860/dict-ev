# Joshua Phillips
# 2/3/2025
# Dictionaries Assesment project.

artists_art = {'Unlike Pluto': 'Better Luck Next Life', '8 Graves': 'The Underground', 'Confetti': 'Balloons', 'Neoni': 'Outlaw', 'Desi Valentine': 'Someone New', 'Foreign Figures': 'King'}
print(f'My Current list of favorite artists and their best song (in my opinion) is {artists_art}')

artists_art.update({'Unlike Pluto': 'Digital Junkie'})
print(f'New update to the list {artists_art}')

for artists in artists_art:
    print(artists)

for songs in artists_art.values():
    print(songs)

for combined in artists_art.items():
    print(combined)


RED = (255, 0, 0)
