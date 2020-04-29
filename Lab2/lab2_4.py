import Shared.Euler
import Shared.Canvas

euler = Shared.Euler.generateEuler(6)
print(Shared.Euler.findEuler(euler))
Shared.Canvas.draw_graph(euler)