#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    num = len(dir(hidden_4))
    i = 1
    while i <= num:
        if dir(hidden_4) [i][:2] != "__":
            print(dir(hidden_4) [i])
        i = i + 1
    
