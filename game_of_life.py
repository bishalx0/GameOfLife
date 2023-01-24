import pygame
import numpy as np

class GameOfLife:
    def __init__(self, surface, width=1920, height=1080, scale=10, offset=1, active_color=(255, 255, 255), inactive_color=(50, 50, 50)):
        self.surface = surface
        self.width = width
        self.height = height
        self.scale = scale
        self.offset = offset
        self.active_color = active_color
        self.inactive_color = inactive_color

        self.columns = int(height / scale)
        self.rows = int(width / scale)

        self.grid = np.random.randint(0, 2, size=(self.rows, self.columns), dtype=bool)

    def run(self):
        
        """Update and redraw the current grid state"""
        
        self.draw_grid()
        self.update_grid()

    def draw_grid(self):
        
        """Drawing the grid"""
        
        for row in range(self.rows):
            for col in range(self.columns):
                if self.grid[row, col]:
                    pygame.draw.rect(self.surface, self.active_color, [row * self.scale, col * self.scale, self.scale - self.offset, self.scale - self.offset])
                else:
                    pygame.draw.rect(self.surface, self.inactive_color, [row * self.scale, col * self.scale, self.scale - self.offset, self.scale - self.offset])

    def update_grid(self):
        
        """Updating the gid according to Conway's Game of Life rules"""
        
        updated_grid = self.grid.copy()
        for row in range(updated_grid.shape[0]):
            for col in range(updated_grid.shape[1]):
                updated_grid[row, col] = self.update_cell(row, col)

        self.grid = updated_grid

    def update_cell(self, x, y):
        
        """Update single cell based on Conway's Game of Life rules"""
        
        current_state = self.grid[x, y]
        alive_neighbors = 0

        # Get number of alive neighbors
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if i == 0 and j == 0:
                        continue
                    elif self.grid[x + i, y + j]:
                        alive_neighbors += 1
                except:
                    continue

        # Update cell's state

        # Dies by underpopulation
        if current_state and alive_neighbors < 2:
            return False
        
        # Live to next generation
        elif current_state and (alive_neighbors == 2 or alive_neighbors == 3):
            return True

        # Dies by overpopulation
        elif current_state and alive_neighbors > 3:
            return False

        # Alive by reproduction
        elif ~current_state and alive_neighbors == 3:
            return True

        # Otherwise no change
        else:
            return current_state
