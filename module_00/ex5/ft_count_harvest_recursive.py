def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count_down(counter):
        if counter > days:
            print('Harvest time!')
            return
        print(f'day {counter}')
        count_down(counter + 1)
    count_down(1)
