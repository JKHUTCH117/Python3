def steg_encode_char(char, cover):
  
  charbin = format(ord(char), '0>8b')
  
  for i in range(0,8):
    coverbinl = list(format(int(cover[i]), '8>8b'))
    coverbinl[-1] = charbin[i]
    cover[i] = str(int(''.join(coverbinl), 2))
