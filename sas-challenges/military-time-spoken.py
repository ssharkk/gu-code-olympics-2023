

def convert_to_military_time(time_str):
    time_str = time_str.strip()
    if ":" not in time_str:
        hh, mmXM = time_str[:-2], "00"+time_str[-2:]
    else:
        hh, mmXM = time_str.split(":")
    hh = int(hh)
    m1, m2 = int(mmXM[0]), int(mmXM[1])
    mm = (m1, m2)
    xm = mmXM[2:].upper()
    guide_hours = {
        (12, "AM"): "zero", (1, "AM"): "zero one", (2, "AM"): "zero two", (3, "AM"): "zero three",
        (4, "AM"): "zero four", (5, "AM"): "zero five", (6, "AM"): "zero six", (7, "AM"): "zero seven",
        (8, "AM"): "zero eight", (9, "AM"): "zero nine", (10, "AM"): "ten", (11, "AM"): "eleven",
        (12, "PM"): "twelve", (1, "PM"): "thirteen", (2, "PM"): "fourteen", (3, "PM"): "fifteen",
        (4, "PM"): "sixteen", (5, "PM"): "seventeen", (6, "PM"): "eighteen", (7, "PM"): "nineteen",
        (8, "PM"): "twenty", (9, "PM"): "twenty-one", (10, "PM"): "twenty-two", (11, "PM"): "twenty-three",
    }

    guide_m1 = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
    }
    guide_m2 = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
    }

    guide_mm = {}
    for i in range(10):
        guide_mm[(0, i)] = "zero " + guide_m2[i]
    for i in range(10, 20):
        guide_mm[(i//10, i%10)] = guide_m2[i]
    for i in range(20, 60):
        guide_mm[i//10, i%10] = (guide_m1[i//10] + "-" + guide_m2[i%10]).strip("-")
    ans = guide_hours[hh, xm]
    if mm == (0, 0):
        return ans + " hundred hours"
    return ans + " " + guide_mm[mm]

times = ["12AM   ", "12:00AM", "12:00PM", "12:34PM", "12:34AM", "7:45AM", "4:09AM", "5:05PM", "3PM"]
"Examples:"
for time in times:
    print(time, "\t", convert_to_military_time(time))

print("\nFull conversion table:")

for ampm in ["AM", "PM"]:
    for hr in [12] + list(range(1,12)):
        for mm in range(0, 60, 1):
            time = str(hr) + ":" + "{:02d}".format(mm) + ampm
            print(time.rjust(10), "_", convert_to_military_time(time))

print("\nThe military time is ", convert_to_military_time(input("What time is it in civilian (hh:mmAM or hh:mmPM or hhAM or hhPM)?\n")), ".", sep="")
input("Press enter to exit.")
