database = {
    "apple": "100",
    "orange": "200",
    "sliced_bread": "300"
}


def calculator(food):
    if food in database:
        return database[food]


def unit_test_happy_path():
    apple_response = calculator("apple")
    orange_response = calculator("orange")
    sliced_b_response = calculator("sliced_bread")

    if apple_response != "100" or orange_response != "200" or sliced_b_response != "300":
        print("False")
    else:
        print("True")


if __name__ in "__main__":
    unit_test_happy_path()