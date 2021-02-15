"""Tame of Thrones"""
import sys


class TameOfThrones:
    """Tame of Thrones"""

    def __init__(self, list_of_kingdom, kingdom, secret):
        self.list_of_kingdom = list_of_kingdom
        self.kingdom = kingdom
        self.secret = secret
        self.message = self.result()
        self.logo = self.list_of_kingdom[self.kingdom]
        self.agree = CheckMessage(self.logo, self.message)

    def find(self):
        """function to find if won the kingdom"""
        if self.agree.validate_message():
            return self.kingdom
        return None

    def result(self):
        """Function to decrypt the message"""
        key = len(self.list_of_kingdom[self.kingdom])
        output = ""
        for letter in self.secret:
            # to form cyclic alphabet chart
            output += chr((ord(letter) - key - 65) % 26 + 65)
        return output


class CheckMessage:
    """check if logo letters are present in the message"""

    def __init__(self, logo, message):
        self.logo = logo
        self.message = message
        self.checked_dict = self.compare_message()

    def compare_message(self):
        """function to compare the message with the logo"""
        check_dict = dict()
        for letter in self.logo:
            if letter in check_dict:
                check_dict[letter] = check_dict[letter] + 1
            else:
                check_dict[letter] = 1

        for letter in self.message:
            if letter in check_dict:
                check_dict[letter] = check_dict[letter] - 1
        return check_dict

    def validate_message(self):
        """if hash table has less or equal to zero the logo is present"""
        final_result = all(value <= 0 for value in self.checked_dict.values())
        if final_result:
            return True
        return None


class FinalAnswer:
    """Return the final answer"""

    def __init__(self, input_file, list_of_kingdom):
        self.input_file = input_file
        self.list_of_kingdom = list_of_kingdom
        self.ans_list = self.extract()
        self.final_list = []

    def extract(self):
        """Extract the input from input  file"""
        ans_list = ["SPACE"]
        filename = open(self.input_file, 'r')
        with filename as sentence:
            for row in sentence:
                each_line = row.strip().split()
                kingdom = each_line[0]
                message = "".join(each_line[1:])
                value = TameOfThrones(self.list_of_kingdom, kingdom, message)
                ans_list.append(value.find())
        sentence.close()
        return ans_list

    def checked_answer(self):
        """ check for None and repeated values"""
        self.ans_list = [i for i in self.ans_list if i]
        for j in self.ans_list:
            if j not in self.final_list:
                self.final_list.append(j)

        # check if 3 kingdoms agreed
        if len(self.final_list) > 3:
            return self.final_list
        return None


kingdomlist = {'SPACE': 'GORILLA',
               'LAND': 'PANDA',
               'WATER': 'OCTOPUS',
               'ICE': 'MAMMOTH',
               'AIR': 'OWL',
               'FIRE': 'DRAGON'
               }
file = sys.argv[1]
ans = FinalAnswer(file, kingdomlist)
if ans.checked_answer() is not None:
    for i in ans.checked_answer():
        print(i, end=" ")
else:
    print("NONE")
