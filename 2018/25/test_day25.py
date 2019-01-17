import day25


class TestClass(object):
    def test_one(self):
        case_one = """-1,2,2,0
0,0,2,-2
0,0,0,-2
-1,2,0,0
-2,-2,-2,2
3,0,2,-1
-1,3,2,2
-1,0,-1,0
0,2,1,-2
3,0,0,0""".splitlines()
        c = day25.find_constellations(case_one)
        assert day25.count_constellations(c) == 4

    def test_two(self):
        case_two = """1,-1,0,1
2,0,-1,0
3,2,-1,0
0,0,3,1
0,0,-1,-1
2,3,-2,0
-2,2,0,0
2,-2,0,-1
1,-1,0,-1
3,2,0,2""".splitlines()
        c = day25.find_constellations(case_two)
        assert day25.count_constellations(c) == 3

    def test_three(self):
        case_three = """1,-1,-1,-2
-2,-2,0,1
0,2,1,3
-2,3,-2,1
0,2,3,-2
-1,-1,1,-2
0,-2,-1,0
-2,2,3,-1
1,2,2,0
-1,-2,0,-2""".splitlines()
        c = day25.find_constellations(case_three)
        assert day25.count_constellations(c) == 8

