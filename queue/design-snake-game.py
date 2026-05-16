from collections import deque

class SnakeGame:

    def __init__(self, width: int, height: int, food: list[list[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.food_idx = 0
        self.snake = deque([(0, 0)])  # head is at the end
        self.snake_set = {(0, 0)}  # quick check for collision
        self.directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    def move(self, direction: str) -> int:
        current_head = self.snake[-1]
        dx, dy = self.directions[direction]
        new_head = (current_head[0] + dx, current_head[1] + dy)

        # Check for border collision
        if not (0 <= new_head[0] < self.height and 0 <= new_head[1] < self.width):
            return -1

        # Check if snake bites itself (ignoring tail, which moves away unless eating food)
        tail = self.snake[0]
        if new_head in self.snake_set and new_head != tail:
            return -1

        # Check if snake eats food
        if (self.food_idx < len(self.food)) and (new_head == tuple(self.food[self.food_idx])):
            self.food_idx += 1
            # Snake grows, no removal of tail
        else:
            # Move snake forward by removing tail
            self.snake.popleft()
            self.snake_set.remove(tail)

        # Add new head position
        self.snake.append(new_head)
        self.snake_set.add(new_head)

        return len(self.snake) - 1
