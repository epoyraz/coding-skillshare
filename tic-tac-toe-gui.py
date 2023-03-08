import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.player = "X"
        self.board = [" "] * 9
        self.game_over = False

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text=" ", font=("Helvetica", 20), width=5, height=2,
                                   command=lambda i=i, j=j: self.handle_click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.status_label = tk.Label(self.root, text="It's your turn, " + self.player, font=("Helvetica", 16))
        self.status_label.grid(row=3, columnspan=3)

    def handle_click(self, i, j):
        if self.board[3*i+j] == " " and not self.game_over:
            self.board[3*i+j] = self.player
            self.buttons[i][j].config(text=self.player)
            if self.check_win():
                self.status_label.config(text=self.player + " wins!")
                self.game_over = True
            elif " " not in self.board:
                self.status_label.config(text="It's a tie!")
                self.game_over = True
            else:
                self.player = "O" if self.player == "X" else "X"
                self.status_label.config(text="It's your turn, " + self.player)

    def check_win(self):
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != " ":
                return True
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                return True
        if self.board[0] == self.board[4] == self.board[8] != " " or \
           self.board[2] == self.board[4] == self.board[6] != " ":
            return True
        return False

    def run(self):
        self.root.mainloop()

game = TicTacToe()
game.run()
