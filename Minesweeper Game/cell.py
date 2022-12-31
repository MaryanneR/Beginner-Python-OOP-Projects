from tkinter import Button, Label
import random
import settings
import ctypes
import sys


class Cell:

    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.possible_mine = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=4,
            height=2
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg = 'lightgray',
            fg='black',
            text=f'Cells Left: {Cell.cell_count}',
            width=15,
            height=10,
            font=("Times", 12)
        )
        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

            # If the MINES_COUNT is equal to the number of cells remaining, player has won game
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, "Whoohoo! \n You've won the game!", 'Congratulations!', 0)


        # If cell is opened, cancels future left/right click events
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def get_cell_by_axis(self, x, y):
        # Return a cell object based on the value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1)
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines)
            # Update count of cell count label
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f'Cells Left: {Cell.cell_count}'
                )
            # If cell was marked as possible mine, this will configure
            # the background color back to SystemButtonFace
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )

            # Marks cell as opened (Use as last line of this method)
            self.is_opened = True

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'Whoops! \n You clicked on a mine!', 'Game Over', 0)
        sys.exit()

    def right_click_actions(self, event):
        if not self.possible_mine:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.possible_mine = True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
            self.possible_mine = False

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all,
            settings.MINES_COUNT
        )
        for picked_cells in picked_cells:
            picked_cells.is_mine = True

    def __repr__(self):
        return f'Cell({self.x}, {self.y})'
