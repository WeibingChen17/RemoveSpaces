import os
try:
    popclip_text = os.getenv('POPCLIP_TEXT')
    print(''.join([a_str[0].upper() + a_str[1:] for a_str in popclip_text.split()]))
except:
    pass
