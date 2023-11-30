import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 540, 540
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

def draw_board(board, color_numbers):
    for i in range(GRID_SIZE + 1):
        line_width = 2 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), line_width)
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), line_width)

    font = pygame.font.Font(None, 36)

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] != 0:
                color = color_numbers.get((i, j), BLACK)
                text = font.render(str(board[i][j]), True, color)
                text_rect = text.get_rect(center=(j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text, text_rect)

def find_empty_cells(board):
    empty_cells = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                empty_cells.append((i, j))
    return empty_cells

def is_valid(board, row, col, num):
    # Check if the number can be placed in the given row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
            return False
    return True

def solve_sudoku_visual(board):
    empty_cells = find_empty_cells(board)
    if not empty_cells:
        return True

    row, col = empty_cells[0]

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            added_numbers.append((row, col))
            board[row][col] = num

            # Visualize the process
            screen.fill(WHITE)
            draw_board(board, {pos: GREEN for pos in added_numbers})
            pygame.display.flip()
            pygame.time.delay(200)

            if solve_sudoku_visual(board):
                return True

            # Color the invalid number red
            draw_board(board, {(row, col): RED})
            pygame.display.flip()
            pygame.time.delay(200)

            # Remove the invalid number
            board[row][col] = 0

    added_numbers.pop()
    return False

# Given Sudoku board
board = [[3, 0, 6, 0, 8, 2, 0, 7, 0],
         [0, 5, 0, 7, 0, 9, 2, 6, 0],
         [0, 2, 9, 0, 0, 1, 0, 0, 0],
         [8, 3, 0, 6, 0, 0, 0, 0, 0],
         [6, 0, 0, 1, 0, 8, 0, 0, 4],
         [0, 0, 0, 0, 0, 7, 0, 8, 5],
         [0, 0, 0, 8, 0, 0, 1, 9, 0],
         [0, 9, 1, 2, 0, 3, 0, 5, 0],
         [0, 8, 0, 9, 1, 0, 4, 0, 2]]

# Keep track of added numbers for coloring
added_numbers = []

# Solve the Sudoku puzzle visually
solve_sudoku_visual(board)

# Keep the window open until the user closes it
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()