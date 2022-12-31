from tkinter import *
import settings
import utilities
from cell import Cell


# Create window
root = Tk()

# Override settings of window
root.configure(bg='lightgray')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(False, False)

# Top Bar
top_frame = Frame(
    root,
    bg='lightgray',
    width=settings.WIDTH,
    height=utilities.height_prct(20)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='lightgray',
    fg='black',
    text='Minesweeper',
    font=('Times', 22)
)

game_title.place(
    x=utilities.width_prct(50),
    y=utilities.height_prct(5)
)

# Left Side Bar
left_frame = Frame(
    root,
    bg='lightgray',
    width=utilities.width_prct(23),
    height=utilities.height_prct(80)
)
left_frame.place(x=0, y=utilities.height_prct(20))

center_frame = Frame(
    root,
    bg='lightgray',
    width=utilities.width_prct(75),
    height=utilities.height_prct(80)
)
center_frame.place(x=utilities.width_prct(23),
                   y=utilities.height_prct(20))

for x in range(settings.GRID_SIZE * 2):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
            )

# Call label from Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()


# Run the window
root.mainloop()
