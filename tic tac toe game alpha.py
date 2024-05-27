import tkinter as tk
from tkinter import messagebox

def create_main_window():
    window = tk.Tk()
    window.title("Tic-Tac-Toe")
    return window

def initialize_board(window):
    board = [[None for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            button = tk.Button(window, text=' ', font=('normal', 40), width=5, height=2,
                               command=lambda r=row, c=col: on_click(r, c))
            button.grid(row=row, column=col)
            board[row][col] = button
    return board

current_player = 'X'

def on_click(row, col):
    global current_player
    if board[row][col]['text'] == ' ' and not check_winner():
        board[row][col]['text'] = current_player
        if check_winner():
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            reset_board()
        elif check_tie():
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            reset_board()
        else:
            current_player = 'O' if current_player == 'X' else 'X'

def check_winner():
    for row in range(3):
        if board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text'] != ' ':
            return True
    for col in range(3):
        if board[0][col]['text'] == board[1][col]['text'] == board[2][col]['text'] != ' ':
            return True
    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != ' ':
        return True
    if board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != ' ':
        return True
    return False

def check_tie():
    for row in range(3):
        for col in range(3):
            if board[row][col]['text'] == ' ':
                return False
    return True

def reset_board():
    global current_player
    current_player = 'X'
    for row in range(3):
        for col in range(3):
            board[row][col]['text'] = ' '

if __name__ == "__main__":
    window = create_main_window()
    board = initialize_board(window)
    window.mainloop()
