def partOne():
    with open("input.txt") as file:

        passport = ""
        valid = 0
        for line in file:
            if line.rstrip("\n") == "":
                if "byr:" in passport \
                        and "iyr:" in passport \
                        and "eyr:" in passport \
                        and "hgt:" in passport \
                        and "hcl:" in passport \
                        and "ecl:" in passport \
                        and "pid:" in passport:
                    valid += 1

                passport = ""

            passport = passport + " " + line.rstrip("\n")
    print(valid)


def partTwo():
    with open("input.txt") as file:

        passport = ""
        valid = 0
        for line in file:
            if line.rstrip("\n") == "":
                if "byr:" in passport \
                        and "iyr:" in passport \
                        and "eyr:" in passport \
                        and "hgt:" in passport \
                        and "hcl:" in passport \
                        and "ecl:" in passport \
                        and "pid:" in passport:

                    fieldsValid = True
                    fields = passport.split()
                    eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                    validHairChars = "0123456789abcdef"
                    for field in fields:
                        if fieldsValid and "byr" in field:
                            byr = field.split(":")
                            if len(byr[1]) != 4 or int(byr[1]) > 2002 or int(byr[1]) < 1920:
                                fieldsValid = False
                        elif fieldsValid and "iyr" in field:
                            iyr = field.split(":")
                            if len(iyr[1]) != 4 or int(iyr[1]) > 2020 or int(iyr[1]) < 2010:
                                fieldsValid = False
                        elif fieldsValid and "eyr:" in field:
                            eyr = field.split(":")
                            if len(eyr[1]) != 4 or int(eyr[1]) > 2030 or int(eyr[1]) < 2020:
                                fieldsValid = False
                        elif fieldsValid and "hgt:" in field:
                            hgt = field.split(":")
                            if "cm" in hgt[1]:
                                if int(hgt[1].rstrip("cm")) < 150 or int(hgt[1].rstrip("cm")) > 193:
                                    fieldsValid = False
                            elif "in" in hgt[1]:
                                if int(hgt[1].rstrip("in")) < 59 or int(hgt[1].rstrip("in")) > 76:
                                    fieldsValid = False
                            else:
                                fieldsValid=False
                        elif fieldsValid and "hcl:" in field:
                            hcl = field.split(":")
                            if not ("#" in hcl[1]) or len(hcl[1].lstrip("#")) != 6 or not all(c in validHairChars for c in hcl[1].lstrip("#").lower()):
                                fieldsValid = False
                        elif fieldsValid and "ecl:" in field:
                            ecl = field.split(":")
                            if len(ecl[1]) != 3 or not (ecl[1] in eyeColors):
                                fieldsValid = False
                        elif fieldsValid and "pid:" in field:
                            pid = field.split(":")
                            if len(pid[1]) != 9:
                                fieldsValid = False
                    if fieldsValid:
                        valid += 1

                passport = ""

            passport = passport + " " + line.rstrip("\n")
    print(valid)


partOne()
partTwo()
