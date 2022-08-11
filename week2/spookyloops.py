#!/usr/bin/python3

def main():
    teeth_count = 0
    with open('dracula.txt', 'r') as fangs: #opens text as file object
        for line in fangs:
            if "vampire" in line.lower():
                teeth_count+=1
                print(line)
    print(teeth_count)


if __name__ == "__main__":
    main()
