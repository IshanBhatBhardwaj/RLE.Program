
def to_hex_string(data):
    for values in data:
        if values == 10:
            data[(data.index(10))] = 'a'
        if values == 11:
            data[(data.index(11))] = 'b'
        if values == 12:
            data[(data.index(12))] = 'c'
        if values == 13:
            data[(data.index(13))] = 'd'
        if values == 14:
            data[(data.index(14))] = 'e'
        if values == 15:
            data[(data.index(15))] = 'f'

    total = ''
    for values in data:
        x = str(values)
        total = total + x
    return total




def count_runs(flat_data):
    j = 0
    count = 0
    my_list = []

    for i in range(0, len(flat_data)):
        if flat_data[i] == flat_data[j]:
            count = count + 1
            if count >= 15:
                my_list.append(15)
                my_list.append(flat_data[j])
                j = i
                count = 0

        elif flat_data[i] != flat_data[j]:
            my_list.append(count)
            my_list.append(flat_data[j])
            j = i
            count = 1

    my_list.append(count)
    my_list.append(flat_data[j])

    x = len(my_list) // 2

    return x



def encode_rle(flat_data):
    j = 0
    count = 0
    my_list = []

    for i in range(0, len(flat_data)):
        if flat_data[i] == flat_data[j]:
            count = count + 1
            if count >= 15:
                my_list.append(15)
                my_list.append(flat_data[j])
                j = i
                count = 0

        elif flat_data[i] != flat_data[j]:
            my_list.append(count)
            my_list.append(flat_data[j])
            j = i
            count = 1

    my_list.append(count)
    my_list.append(flat_data[j])

    # for i in range(0, len(my_list)):
    #     if my_list[i] == 'a' or my_list[i] == 'A':
    #         my_list[i] = 10
    #     if my_list[i] == 'b' or my_list[i] == 'B':
    #         my_list[i] = 11
    #     if my_list[i] == 'c' or my_list[i] == 'C':
    #         my_list[i] = 12
    #     if my_list[i] == 'd' or my_list[i] == 'D':
    #         my_list[i] = 13
    #     if my_list[i] == 'e' or my_list[i] == 'E':
    #         my_list[i] = 14
    #     if my_list[i] == 'f' or my_list[i] == 'F':
    #         my_list[i] = 15
    #
    # for i in range(0, len(my_list)):
    #     my_list[i] = int(my_list[i])


    return my_list




def get_decoded_length(rle_data):
    rle_data = (rle_data[0:len(rle_data) + 1:2])
    total = sum(rle_data)

    return total





def decode_rle(rle_data):
    my_list = []
    for i in range(0, len(rle_data), 2):
        for j in range(0, rle_data[i]):
            my_list.append(rle_data[i + 1])

    return my_list






def string_to_data(data_string):
    data_string = list(data_string)
    for i in range(0, len(data_string)):
        if data_string[i] == 'a' or data_string[i] == 'A':
            data_string[i] = 10
        if data_string[i] == 'b' or data_string[i] == 'B':
            data_string[i] = 11
        if data_string[i] == 'c' or data_string[i] == 'C':
            data_string[i] = 12
        if data_string[i] == 'd' or data_string[i] == 'D':
            data_string[i] = 13
        if data_string[i] == 'e' or data_string[i] == 'E':
            data_string[i] = 14
        if data_string[i] == 'f' or data_string[i] == 'F':
            data_string[i] = 15

    for i in range(0, len(data_string)):
        data_string[i] = int(data_string[i])

    return data_string




def to_rle_string(rle_data):

    my_list = []
    my_list_sub = []
    count = 0

    for i in range(1, len(rle_data), 2):
        if rle_data[i] == 10:
            rle_data[i] = 'a'
        if rle_data[i] == 11:
            rle_data[i] = 'b'
        if rle_data[i] == 12:
            rle_data[i] = 'c'
        if rle_data[i] == 13:
            rle_data[i] = 'd'
        if rle_data[i] == 14:
            rle_data[i] = 'e'
        if rle_data[i] == 15:
            rle_data[i] = 'f'

    for i in range(0,len(rle_data),1):

        if count == 2:
            my_list_sub.append(':')
            my_list = my_list + my_list_sub
            my_list_sub.clear()
            my_list_sub.append(rle_data[i])
            count = 1
        else:
            my_list_sub.append(rle_data[i])
            count = count + 1

    my_list = my_list + my_list_sub


    total = ''

    for values in my_list:
        x = str(values)
        total = total + x


    return total




def string_to_rle(rle_string):

    my_list = []

    strings = rle_string.split(':')

    for i in range(0,len(strings)):
        if len(strings[i]) == 2:
            for values in strings[i]:
                my_list.append(values)
        if len(strings[i]) == 3:
            my_list.append(strings[i][0] + strings[i][1])
            my_list.append(strings[i][2])

        for i in range(0, len(my_list)):
            if my_list[i] == 'a' or my_list[i] == 'A':
                my_list[i] = 10
            if my_list[i] == 'b' or my_list[i] == 'B':
                my_list[i] = 11
            if my_list[i] == 'c' or my_list[i] == 'C':
                my_list[i] = 12
            if my_list[i] == 'd' or my_list[i] == 'D':
                my_list[i] = 13
            if my_list[i] == 'e' or my_list[i] == 'E':
                my_list[i] = 14
            if my_list[i] == 'f' or my_list[i] == 'F':
                my_list[i] = 15

        for i in range(0, len(my_list)):
            my_list[i] = int(my_list[i])

    return(my_list)







if __name__ == '__main__':


    from console_gfx import ConsoleGfx

    print('Welcome to the RLE image encoder!')
    print('\nDisplaying Spectrum Image:')
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)


    # print('\nRLE Menu')
    # print('*' * 8)
    # print('0. Exit\n1. Load File\n2. Load Test Image\n3. Read RLE String\n4. Read RLE Hex String')
    # print(
    #     '5. Read Data Hex String\n6. Display Image\n7. Display RLE String\n8. Display Hex RLE Data\n9. Display Hex Flat Data')

    image_data = None
    # image_data = 0
    flat_byte_data = 0
    while True:
        print('\nRLE Menu')
        print('-' * 8)
        print('0. Exit\n1. Load File\n2. Load Test Image\n3. Read RLE String\n4. Read RLE Hex String')
        print(
            '5. Read Data Hex String\n6. Display Image\n7. Display RLE String\n8. Display Hex RLE Data\n9. Display Hex Flat Data')

        option = int(input('\nSelect a Menu Option: '))

        if option == 1:
            filename = input('Enter name of file to load: ')  # testfiles/fsu.gfx
            flat_byte_data = ConsoleGfx.load_file(filename)
        elif option == 2:
            flat_byte_data = ConsoleGfx.test_image
            print('Test image data loaded.')
        elif option == 6:
            if flat_byte_data == 0:
                print('Displaying image...\n(no data)')
            elif flat_byte_data != 0:
                print('Displaying image...')
                ConsoleGfx.display_image(flat_byte_data)
        # elif option == 6 and image_data != pass:

        elif option == 3:
            rle_string = input('Enter an RLE string to be decoded: ')
            flat_byte_data = decode_rle(string_to_rle(rle_string))
        elif option == 4:  #28106B10AB102B10CB102B105B20BB106B10
            rle_hex = input('Enter the hex string holding RLE data: ')
            flat_byte_data = decode_rle(string_to_data(rle_hex))
        elif option == 5:
            flat_string = input('Enter the hex string holding flat data: ')
            flat_byte_data = string_to_data(flat_string)

        elif option == 7:
            if flat_byte_data == 0:
                print('RlE representation: (no data)')
            elif flat_byte_data != 0:
                rle_byte_data = encode_rle(flat_byte_data)
                print('RLE representation:',to_rle_string(rle_byte_data))
                # rle_byte_data = encode_rle(image_data)
                # print(to_rle_string(rle_byte_data))

        elif option == 8:
            if flat_byte_data == 0:
                print('RLE hex values: (no data)')
            elif flat_byte_data != 0:
                rle_byte_data = encode_rle(flat_byte_data)
                print("RLE hex values:", to_hex_string(rle_byte_data))
            # rle_byte_data = encode_rle(image_data)
            # print(to_hex_string(rle_byte_data))

        elif option == 9:
            if flat_byte_data == 0:
                print('Flat hex values: (no data)')
            elif flat_byte_data != 0:
                print('Flat hex values:', to_hex_string(flat_byte_data))
                # print(to_hex_string(image_data))
        elif option == 0:
            break

        else:
            print('Error! Invalivd input.')











