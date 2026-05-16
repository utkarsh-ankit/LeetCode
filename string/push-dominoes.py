class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        forces = [0] * N
        
        # Pass from left to right (force going rightward)
        force = 0
        for i in range(N):
            if dominoes[i] == 'R':
                force = N
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force
        
        # Pass from right to left (force going leftward)
        force = 0
        for i in range(N-1, -1, -1):
            if dominoes[i] == 'L':
                force = N
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force
        
        # Determine final state based on forces
        result = []
        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else:
                result.append('.')
        
        return ''.join(result)
