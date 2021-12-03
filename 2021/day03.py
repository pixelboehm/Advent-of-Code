import unittest

class MyClass():

    def main(self):
        with open ("input_day03.txt") as fp: 
            one_counter = 0
            zero_counter = 0
            gamma = ""
            epsilon = ""
            result_task_one = 0
            result_task_two = 0
            bits = fp.readlines()
            for i in range(len(bits)):
                bits[i] = bits[i].rstrip("\n")
            oxygen = list(bits)
            co_two = list(bits)
            for i in range(len(bits[0])):
                for j in range(len(bits)): ## correct order?
                    if bits[j][i] == '1':
                        one_counter += 1
                    elif bits[j][i] == '0':
                        zero_counter += 1
                if one_counter >= zero_counter:
                    gamma += '1'
                    epsilon += '0'
                else:
                    gamma += '0'
                    epsilon += '1'
                one_counter = 0
                zero_counter = 0
            result_task_one =  int(gamma, 2) * int(epsilon, 2)


            for i in range(0, len(oxygen)):
                oxygen = self.get_content(oxygen, i)
                if (len(oxygen) == 1):
                    break
            
            for i in range(0, len(co_two)):
                co_two = self.get_content2(co_two, i)
                if (len(co_two) == 1):
                    break

            tmp1 = int(oxygen[0], 2)
            tmp2 = int(co_two[0], 2)
            print(tmp1 * tmp2)


            result_task_two = int(oxygen[0], 2) * int(co_two[0], 2) 

    def get_content(self, content, i):
        one_counter = 0
        zero_counter = 0
        for j in range(len(content)):
            if content[j][i] == '1':
                one_counter += 1
            elif content[j][i] == '0':
                zero_counter += 1
        if one_counter >= zero_counter:
            result = [x for x in content if x[i] == '1']
        else:
            result = [x for x in content if x[i] == '0']
        return result
 
    def get_content2(self, content, i):
        one_counter = 0
        zero_counter = 0
        for j in range(len(content)):
            if content[j][i] == '1':
                one_counter += 1
            elif content[j][i] == '0':
                zero_counter += 1
        if one_counter < zero_counter:
            result = [x for x in content if x[i] == '1']
        else:
            result = [x for x in content if x[i] == '0']
        return result
    

class Tests(unittest.TestCase):

    def setUp(self):
        self.object = MyClass() 

    def test_shouldFail(self):
        self.fail("Initial Fail for Setup")


if __name__ == '__main__':
    test = MyClass()
    test.main()
    # unittest.main()
