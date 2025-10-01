def commaCode():
    spam = ["apples", "bananas", "tofu", "cats", "coffee"]

    for i, item in enumerate(spam):
        if item == spam[-1]:
            print("and " + f"{spam[-1]}", end=" ")
            print("\n")
            exit()
        print(f"{spam[i]},", end=" ")


commaCode()
