
def snake_to_camel(word):
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(snake_to_camel('Hee_lL_mmK_Mbr_uhBre'))