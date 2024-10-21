def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average_temperature(num_list)
    calc_min_max_temperature(num_list)



def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,33")

def get_user_input():
    x= input().split(",")
    x_float = [float(item) for item in x]
    return (x_float)

def calc_average_temperature(get_user_input):
    sum=0
    for i in get_user_input:
        sum += i
    avg = sum/len(get_user_input)
    print(avg)
    return avg



def calc_min_max_temperature(get_user_input):
    min=0
    max=0
    for i in get_user_input:
        if i<min :
            min = i
        elif i>min :
            max = i
    print(min)
    print(max)
    return min,max


main()