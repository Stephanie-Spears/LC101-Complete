"""input/output tests"""
import turtle

def student_data():
    """docstring"""
    infile = open("studentdata.txt", "r")
    val_list = ""
    for line in infile:
        values = line.split()
        if len(values) > 7:
            val_list += values[0]
    infile.close()
    return val_list

def average_grade():
    """docstring"""
    infile = open("studentdata.txt", "r")
    lines_list = infile.readlines()
    student_average_list = []
    for line in lines_list:
        aline = line.split()
        student_average = [aline[0], sum(int(x) for x in aline[1:])]
        student_average_list += [student_average]
    infile.close()
    return student_average_list

def student_min_max():
    """docstring"""
    infile = open("studentdata.txt", "r")
    lines_list = infile.readlines()
    student_list = []
    for line in lines_list:
        aline = line.split()
        student_score = [aline[0], min(aline[1:]), max(aline[1:])]
        student_list += [student_score]
    infile.close()
    return student_list

def plotRegression():
    """docstring"""
    # wn = turtle.Screen()
    # a_turtle = turtle.Turtle()
    # wn.setworldcoordinates(-300, -300, 300, 300)
    infile = open("labdata.txt", "r")
    coord_pos = []
    for line in infile:
        aline = line.split()
        x_pos, y_pos = aline[0], aline[1]
        coord_pos += [(int(x_pos), int(y_pos))]
    infile.close()
    return coord_pos


def main():
    """main"""
#    print(student_data())
#    print(average_grade())
#    print(student_min_max())
    print(plotRegression())


if __name__ == "__main__":
    main()
