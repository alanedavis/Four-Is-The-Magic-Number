#!/usr/bin/python

num2words1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
num2words2 = { 2: 'twenty', 3: 'thirty',4: 'forty',5: 'fifty',6: 'sixty',7: 'seventy',8: 'eighty',9: 'ninety' }


def MagicNum(num, s):
    if num == 0:
        if s == "":
            return "zero"
        return s
    elif (num >= 1) and (num <= 19):
        s = s + (num2words1[num])
        return s
    elif (num >= 20) and (num <= 99):
        new_num = num % 10
        return MagicNum(new_num, s + num2words2[num//10])
    elif (num >= 100) and (num <= 999):
        new_num = num % 100
        return MagicNum(new_num, s + num2words1[num//100] + "hundred")
    elif (num >= 1000) and (num <= 999999):
        thousand_num = num // 1000
        hundred_num = num % 1000
        s = MagicNum(thousand_num, s)
        s = s + "thousand"
        return MagicNum(hundred_num, s)
    elif (num >= 1000000) and (num <= 999999999):
        million_num = num // 1000000
        thousand_num = num % 1000000
        s = MagicNum(million_num, s)
        s = s + "million"
        return MagicNum(thousand_num, s)
    else:
        return "Number Out Of Range\n"




if __name__ == "__main__":
    while True:
        print("Enter the Number:")
        number = str(input())
        if number == "stop":
            break
        num_string = ""
        try:
            num_string = MagicNum(int(number), num_string)
        except ValueError as e:
            print(e)
        if num_string == "Number Out Of Range\n":
            print(num_string)
        else:
            print("The magic number path for %d is:" % (int(number)))
            magic_num = len(num_string)
            while magic_num != 4:
                print("%d -> " % (magic_num), end='')
                num_string = ""
                magic_num = len(MagicNum(int(magic_num), num_string))
            print("4\n")
        print("Enter 'stop' to end\n")
