import sys


def main():
    circle = open(sys.argv[1], "rt", encoding="utf-8")
    circle_strip = [line.strip() for line in circle.readlines()]

    x, y = map(int, circle_strip[0].split())
    r = int(circle_strip[1])

    circle.close()

    coordinates = open(sys.argv[2], "rt", encoding="utf-8")
    coordinates_strip = [line.strip() for line in coordinates.readlines()]

    for c in coordinates_strip:
        x0, y0 = map(int, c.split())
        if (x - x0) ** 2 + (y - y0) ** 2 == r ** 2:
            print(0)
        elif (x - x0) ** 2 + (y - y0) ** 2 <= r ** 2:
            print(1)
        elif not (x - x0) ** 2 + (y - y0) ** 2 <= r ** 2:
            print(2)

    coordinates.close()


if __name__ == "__main__":
    main()
