class Allocator:

    def __init__(self, n: int):
        self.memory=[0]*n
        

    def allocate(self, size: int, mID: int) -> int:
        free_count=0

        for i in range(len(self.memory)):
            if self.memory[i]==0:
                free_count+=1

                if free_count==size:
                    start_idex=i-size+1

                    self.memory[start_idx:start_idx+size]=[mID]*size
                    return start_idex

                else:
                    free_count=0
            else:
                free_count=0
        return -1

        

    def freeMemory(self, mID: int) -> int:
        clear=0

        for i in range(len(self.memory)):
            if self.memory[i]==mID:
                self.memory[i]=0
                clear+=1

        return clear

        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)