def get_minimum_steps(series):
    steps = 0

    while series:
        array = list(series)
        new_array = []

        for i in range(len(array) - 1):
            if array[i] != array[i + 1]:
                new_array.append(array[i])
        
        new_array.append(array[len(array) - 1])

        count = {}
        for element in new_array:
            count[element] = count.get(element, 0) + 1

        min_count = min(count.values())
        array = [x for x in new_array if count[x] != min_count]

        steps += len(new_array) - len(array)
        series = "".join(array)

    return steps

series = "kjslaqpwoereeeeewwwefifjdksjdfhjdksdjfkdfdlddkjdjfjfjfjjjjfjffnefhkjgefkgjefkjgkefjekihutrieruhigtefhgbjkkkknbmssdsdsfdvneurghiueor"
steps = get_minimum_steps(series)
print("Minimum steps:", steps)

