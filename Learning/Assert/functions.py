def name_is_cool(name):
    return name + " is cool :)"

def add(a=0, b=0, c=0, d=0):
    return a + b + c + d

def blip_blop(words):
    final = ""

    words = words.split()

    for i in range(len(words)):
        if i % 2 == 0:
            final += "blip "
        elif i % 2 != 0:
            final += "blop "
    
    final = final.strip()

    return final
        
