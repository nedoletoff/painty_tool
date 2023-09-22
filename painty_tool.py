import tkinter as tk
import os
import img_converter as img_c
import byte_converter as byte_c


class Paint(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.t = 0
        self.bin_arr = [[0 for _ in range(28)] for _ in range(28)]

        self.grid = [[] for _ in range(28)]

        # if button 1 is pressed generate event pressed_1
        master.bind("<Button-1>", self.change_t)
        # master.bind("<ButtonRelease-1>", self.change_t0)

        for x in range(28):
            for y in range(28):
                label = tk.Label(self, width=3, height=1, relief=tk.RAISED, borderwidth=1, bg="white")
                label.bind("<Enter>", lambda e, x=x, y=y: self.change_color(x=x, y=y))
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
        self.name_entry.insert(0, "100")
        self.t_status = tk.Label(self, text="draw: " + str(self.t))
        self.t_status.grid(row=0, column=28)

    def change_t(self, *args):
        self.t = not self.t
        self.t_status.config(text="draw: " + str(self.t))

    def change_t1(self, *args):
        self.t = 1

    def change_t0(self, *args):
        self.t = 0

    def save(self, *args):
        name = self.name_entry.get()
        pth = os.path.join(os.getcwd(), 'imgs', 'test', name + '.bmp')

        for x in range(28):
            for y in range(28):
                if self.grid[x][y].cget("bg") == "white":
                    self.bin_arr[x][y] = 1
                else:
                    self.bin_arr[x][y] = 0

        img_c.save_img(pth, byte_c.bin_to_bytes(byte_c.d2_to_d1(self.bin_arr)))

    def clear(self, *args):
        for x in range(28):
            for y in range(28):
                self.grid[x][y].config(bg="white")

    def next(self, *args):
        self.save()
        self.clear()
        text = str(int(self.name_entry.get()) + 1)
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, text)
        self.t = 0
        self.clear()

    def change_color(self, x, y, *args):
        if not self.t:
            return
        if self.grid[x][y].cget("bg") == "white":
            self.grid[x][y].config(bg="black")
        # else:
        #    self.grid[x][y].config(bg="white")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Painty Tool")
    root.resizable(False, False)
    paint = Paint(root)
    paint.pack()

    root.mainloop()

root.mainloop()
