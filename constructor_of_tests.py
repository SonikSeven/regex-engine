with open("TESTS.txt") as TESTS_file:
    with open("RESULT.txt", "w") as RESULT_file:
        for line in TESTS_file:
            r = line.replace("|", " ").split()
            print(f'self.assert{r[2]}(main.find_match("{r[0]}", "{r[1]}"))', file=RESULT_file)
