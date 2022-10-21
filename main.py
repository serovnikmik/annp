import time


class Tests():
    def __init__(self):
        pass
    def start_test(self, name):
        nums = parse(name)
        return _max(nums), _min(nums), _sum(nums), _mult(nums)
    def check_test(self, ans, corr_ans):
        return ans == corr_ans
    def custom_check(self, ans, corr_ans=()):
        return ans[0] >= ans[1]

    def run_tests(self):

        st = time.time()
        print('---test1-----')
        if self.check_test(self.start_test('test1.txt'), (95, -344, 52, 11331274492116074496000)): print('OK')
        else: print('WA')
        print(time.time() - st)

        st = time.time()
        print('---test2-----')
        if self.check_test(self.start_test('test2.txt'), (911, -344, 1079, -1951771397316665103692857344000)): print('OK')
        else: print('WA')
        print(time.time() - st)

        st = time.time()
        print('---test3-----')
        if self.check_test(self.start_test('test3.txt'), (59, -43, 57, -649472)): print('OK')
        else: print('WA')
        print(time.time() - st)

        st = time.time()
        print('---test4-----')
        if self.check_test(self.start_test('test4.txt'), (14, 1, 92, 6706022400)): print('OK')
        else: print('WA')
        print(time.time() - st)

        st = time.time()
        print('---Custom test4-----')
        if self.custom_check(self.start_test('test4.txt')): print('OK')
        else: print('WA')
        print(time.time() - st)

    #changed some numbers, so there are some mistakes
    def write_uncomplished(self):
        #changed first number (95 -> 96)
        if not self.check_test(self.start_test('test1.txt'), (95, -344, 52, 11331274492116074496000)):
            with open("uncomplished_tests.txt", "w") as f:
                f.write('\n')
                f.write('1')
        #changed first number (59 -> 60)
        if not self.check_test(self.start_test('test3.txt'), (60, -43, 57, -649472)):
            with open("uncomplished_tests.txt", "w") as f:
                f.write('\n')
                f.write('2')
        if not self.check_test(self.start_test('test3.txt'), (59, -43, 57, -649472)):
            with open("uncomplished_tests.txt", "w") as f:
                f.write('\n')
                f.write('3')
        if not self.check_test(self.start_test('test4.txt'), (14, 1, 92, 6706022400)):
            with open("uncomplished_tests.txt", "w") as f:
                f.write('\n')
                f.write('4')

def parse(path_to_f):

    f = open(path_to_f, 'r', encoding="utf8")
    a = f.readline().split()
    return [int(i) for i in a]

def _max(arr):
    mn = int(-10e10)
    for i in arr:
        if i > mn: mn = i
    return mn

def _min(arr):
    mn = int(10e10)
    for i in arr:
        if i < mn: mn = i
    return mn

def _sum(arr):
    s = 0
    for i in arr: s += i
    return s

def _mult(arr):
    s = 1
    for i in arr: s *= i
    return s

def main():

    tests = Tests()
    tests.run_tests()
    tests.write_uncomplished()

    '''
    print('Введите путь к файлу:')
    path_to_f = 'test1.txt'
    nums = parse(path_to_f)
    print(f'max: {_max(nums)}\nmin: {_min(nums)}\nsum: {_sum(nums)}\nmult: {_mult(nums)}')
    print(f'({_max(nums)}, {_min(nums)}, {_sum(nums)}, {_mult(nums)})')
    '''

if __name__ == '__main__':
    main()