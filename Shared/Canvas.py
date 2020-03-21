import tkinter as tk
import math

r_graph = 200
r_circle = 25
graph_height = 600
graph_width = 600
graph_height_center = graph_height / 2
graph_width_center = graph_width / 2

root = tk.Tk()
root.geometry('600x600')
canvas = tk.Canvas(root, height=graph_height, width=graph_width, bg="white")


def create_circle(canvas, x, y, r):
    return canvas.create_oval(x - r, y - r, x + r, y + r, fill="white")


def draw_graph(graph):
    global root

    canvas.delete("all")
    diff_angle = 2 * math.pi / len(graph.adjMatrix)

    for i in range(len(graph.adjMatrix)):
        angle_circle = i * diff_angle
        x_circle = graph_height_center + r_graph * math.sin(angle_circle)
        y_circle = graph_width_center - r_graph * math.cos(angle_circle)
        neighbour_id = 0

        # create edges
        for neighbour in graph.adjMatrix[i]:
            if neighbour_id > i and int(neighbour) is 1:
                angle_neighbour = diff_angle * neighbour_id
                x_neighbour = graph_height_center + r_graph * math.sin(angle_neighbour)
                y_neighbour = graph_width_center - r_graph * math.cos(angle_neighbour)
                canvas.create_line(x_circle, y_circle, x_neighbour, y_neighbour)
            neighbour_id += 1

        create_circle(canvas, x_circle, y_circle, r_circle)
        canvas.create_text(x_circle, y_circle, text=i + 1)

    canvas.pack()
    root.mainloop()
