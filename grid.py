import tkinter as tk

# ширината/височината на клетката в пиксели
CELL_SIZE = 50
grid_dimension = (5, 5)
current_pos = (0, 0)
row,col = current_pos

def draw_grid(canvas, grid_size):
    rows, cols = grid_size
    for row in range(rows):
        for col in range(cols):
            upper_corner = (row * CELL_SIZE, col * CELL_SIZE)
            lower_right_corner = (row * CELL_SIZE + CELL_SIZE, col * CELL_SIZE + CELL_SIZE)
            canvas.create_rectangle(upper_corner, lower_right_corner, fill='white')

def draw_player(canvas, position):
    # Тук следва да викнете canvas метода, create_oval за да начертаете кръг на позицията -> position
    row, col = position
    x = col*CELL_SIZE
    y = row*CELL_SIZE
    canvas.create_oval(x,y,x + CELL_SIZE,y + CELL_SIZE,fill = 'blue')
    print('you should complete this funciton to draw a circle at the specified grid position')

def reset_square(canvas, position):
    #TODO: draw an empty square in the given position it should be with fill="white"
    row, col = position
    x = col*CELL_SIZE
    y = row*CELL_SIZE
    canvas.create_rectangle(x,y,x + CELL_SIZE,y + CELL_SIZE,fill = 'white')

# Функция вид event handler, която се вика при натискане на клавиш
def key_pressed(keyEvent):
    global current_pos
    max_row,max_col = grid_dimension
    if keyEvent.keysym.lower() == "right":
        reset_square(canvas, current_pos)
        prev_row, prev_col = current_pos
        if prev_col < max_col - 1:
            current_pos = prev_row, prev_col + 1
        draw_player(canvas, current_pos)
    elif keyEvent.keysym.lower() == "left":
        reset_square(canvas, current_pos)
        prev_row, prev_col = current_pos
        if prev_col > 0:
            current_pos = prev_row, prev_col - 1
        draw_player(canvas, current_pos)
    elif keyEvent.keysym.lower() == "up":
        reset_square(canvas, current_pos)
        prev_row, prev_col = current_pos
        if prev_row > 0:
            current_pos = prev_row - 1, prev_col
        draw_player(canvas, current_pos)
    elif keyEvent.keysym.lower() == "down":
        reset_square(canvas, current_pos)
        prev_row, prev_col = current_pos
        if prev_row < max_row:
            current_pos = prev_row + 1, prev_col
        draw_player(canvas, current_pos)
    

app = tk.Tk()
app.geometry('800x600')
app.title('Grid Demo')

canvas = tk.Canvas(app, width=600, height=400, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)

draw_grid(canvas, grid_dimension)
draw_player(canvas, current_pos)

app.bind("<KeyPress>", key_pressed) 

app.mainloop()



