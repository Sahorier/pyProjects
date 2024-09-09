from result_db import result
print("Wel")
passed = {}
passed_values = []
passed_keys = []
count_passed = 0
count_refard = 0
for index,sresult in enumerate(result.keys()):
    if type(result[sresult]) == float:
        count_passed = count_passed + 1
        passed_values.append(result[sresult])
        passed_keys.append(sresult)
        passed.update({result[sresult] : sresult})
    elif type(result[sresult]) == int:
        count_refard = count_refard + 1
passed_sorted = dict(reversed(sorted(passed.items())))
passlist = []
for passroll in passed_sorted.keys():
    passlist.append(passroll)
roll = int(input("Enter your roll: "))
if roll in result.keys():
    if type(result[roll]) == float:
        print(f"Your result is {result[roll]} and your position is {(passlist.index(result[roll]))+1}")
    elif result[roll] == 1:
        print(f"You have refard in {result[roll]} subject")
    elif result[roll] > 1:
        print(f"You have refard in {result[roll]} subjects")
print(f"Total number of passed students are {count_passed}")
print(f"Total number of refard students are {count_refard}")