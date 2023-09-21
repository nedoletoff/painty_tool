import tkinter as tk
import os


class Paint(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.bin_arr = [[1 for _ in range(28)] for _ in range(28)]

        self.grid = [[] for _ in range(28)]

        for x in range(28):
            for y in range(28):
                label = tk.Label(self, width=3, height=1, relief=tk.RAISED, borderwidth=1, bg="white")
                label.bind("<Button-1>", lambda e, x=x, y=y: self.change_color(x=x, y=y))
                label.grid(row=x, column=y)
                self.grid[x].append(label)

        next_btn = tk.Button(self, text="Next", width=20, height=1, command=self.next)
        next_btn.grid(row=30, column=28)
        save_btn = tk.Button(self, text="Save", width=20, height=1, command=self.save)
        save_btn.grid(row=29, column=28)
        clear_btn = tk.Button(self, text="Clear", width=20, height=1, command=self.clear)
        clear_btn.grid(row=28, column=28)

        # bind buttons to keys
        master.bind("n", self.next)
        master.bind("s", self.save)
        master.bind("c", self.clear)

        self.name_entry = tk.Entry(self, width=20)
        self.name_entry.grid(row=27, column=28)

        # найти на каком label находится мышь

    def save(self, *args):
        for x in range(28):
            for y in range(28):
                if self.grid[x][y].cget("bg") == "white":
                    self.bin_arr[x][y] = 0
                else:
                    self.bin_arr[x][y] = 1
        print(self.bin_arr)
        print(self.name_entry.get())

    def clear(self, *args):
        for x in range(28):
            for y in range(28):
                self.grid[x][y].config(bg="white")

    def next(self, *args):
        self.save()
        self.clear()

    def change_color(self, x, y, *args):
        print(*args)
        if self.grid[x][y].cget("bg") == "white":
            self.grid[x][y].config(bg="black")
        #else:
        #    self.grid[x][y].config(bg="white")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Painty Tool")
    root.resizable(False, False)
    paint = Paint(root)
    paint.pack()

    root.mainloop()

root.mainloop()
