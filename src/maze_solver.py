from line import Line, Point
from window import Window

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(20, 20), Point(90, 90)), "black")
    win.wait_for_close()

if __name__ == "__main__":
    main()