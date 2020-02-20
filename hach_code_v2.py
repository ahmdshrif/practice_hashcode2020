"""
_author_ = "AHMED SHERIF and Mohamed Aboushady"
_credits_ = ["AHMED SHERIF", Mohamed Aboushady"]
_license_ = "GPL"
_version_ = "1.0.1"
""""
##########################################################################################################################
file_name = 'e_also_big'
input = open(file_name + '.in').readlines()

maximum_slices = float(input[0].split()[0])
pizza = [int(n) for n in input[1].split()]
stop_points = []


#######################################################################################################################
def get_maximum(_pizza, _sum_slices=0, _start_point=-1, _solution_ids=[]):
    _pizza_length = len(_pizza)
    if _start_point != -1:
        _pizza_length = _start_point

    for id in range((_pizza_length - 1), -1, -1):
        if (_pizza[id] + _sum_slices) <= maximum_slices:
            _sum_slices += _pizza[id]
            _solution_ids.append(id)

        elif len(_solution_ids) > 0 and _solution_ids[-1] == (id + 1):

            save_solution = _solution_ids[:-1] #remove last number
            # print(save_solution)
            stop_points.append([id + 1, (_sum_slices - _pizza[id + 1]), save_solution])
            #print(_pizza[id + 1])
    return _sum_slices, _solution_ids


############################################################################################################################
#number python = numpy
best_sum_slices, best_solution = get_maximum(pizza)

while len(stop_points) > 0:
    stop_point = stop_points.pop(0)  # get first element and remove it
    # print(stop_point)
    pizza_stop_point = pizza[:stop_point[0]]  # new array
    sum_slices, solution = get_maximum(pizza_stop_point, stop_point[1], stop_point[0],
                                       stop_point[2])  # get maximum with out stop point
    # print(solution)
    if sum_slices > best_sum_slices:
        # if we get  new maximum num we save it as pest solution .
        best_sum_slices = sum_slices
        best_solution = solution

    if (sum_slices == maximum_slices):
        break
############################################################################################################################


best_solution.reverse()

# output
output = open(file_name + '.out', 'w+')
output.write(str(len(best_solution)) + "\r\n")
output.write(' '.join(map(str, best_solution)))

# print
print('Maximum:', maximum_slices)
print('Approached:', best_sum_slices)
print('Present:', (float(best_sum_slices / maximum_slices) * 100))
# print('Solution:', best_solution)
############################################################################################################################
