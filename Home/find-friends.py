def check_connection(network, first, second):
    socials = []
    s = str.split(network[0], '-')
    socials.append(s)
    for x in range(1, len(network)):
        next = str.split(network[x], '-')
        added = False
        for soc in socials:            
            if soc.count(next[0]) > 0  or soc.count(next[1]) > 0:
                soc += set(soc).difference(next)
                added = True
                break
        if added == False:
            socials.append(next)
            added = False
        next = 0


    for soc in socials:            
            if soc.count(first) > 0  and soc.count(second) > 0:
                return True            
    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for
    #auto-testing
    assert check_connection(("nikola-robin","batman-nwing","mr99-batman","mr99-robin","dr101-out00","out00-nwing",),"dr101","mr99") == True