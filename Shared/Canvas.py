from functools import partial
import tkinter as tk
import tkinter.filedialog
import math
from Shared.Converter import list_to_adj
from Shared.Converter import inc_to_adj

r_graph = 200
r_circle = 25
graph_height = 600
graph_width = 600
graph_height_center = graph_height / 2
graph_width_center = graph_width / 2

root = tk.Tk()
root.geometry('600x600')
canvas = tk.Canvas(root, height=graph_height, width=graph_width, bg="white")


def read_adj(graph, event=None):
    file = tk.filedialog.askopenfile(parent=root, mode='r')
    if file is not None and file.mode == 'r':
        lines = file.readlines()
        lines = [list(line.replace('\n', '').split()) for line in lines]
        graph.change_adj_matrix(lines)
        draw_graph(graph)
        file.close()


def read_inc(graph, event=None):
    file = tk.filedialog.askopenfile(parent=root, mode='r')
    if file is not None and file.mode == 'r':
        lines = file.readlines()
        lines = [line.replace('\n', '') for line in lines]
        lines = [list(map(lambda x: int(x), line.split())) for line in lines]
        graph_ajc = inc_to_adj(lines)
        graph.change_adj_matrix(graph_ajc)
        draw_graph(graph)
        file.close()


def read_list(graph, event=None):
    file = tk.filedialog.askopenfile(parent=root, mode='r')
    if file is not None and file.mode == 'r':
        lines = file.readlines()
        for elem in ['.', '\n']:
            lines = [line.replace(elem, '') for line in lines]
        lines = [list(map(lambda x: int(x), line.split())) for line in lines]
        lines = [line[1:] for line in lines]
        graph_adj = list_to_adj(lines)
        graph.change_adj_matrix(graph_adj)
        draw_graph(graph)
        file.close()


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
        canvas.create_text(x_circle, y_circle, text=i)

    b_adj = tk.Button(root, text="Wczytaj jako macierz sąsiedztwa", command=partial(read_adj, graph))
    b_inc = tk.Button(root, text="Wczytaj jako macierz incydencji", command=partial(read_inc, graph))
    b_list = tk.Button(root, text="Wczytaj jako lista sąsiedztwa", command=partial(read_list, graph))
    b_adj.pack()
    b_inc.pack()
    b_list.pack()
    canvas.pack()
    root.mainloop()
