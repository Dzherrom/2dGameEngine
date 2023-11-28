import sys
import sdl2.ext 

class Game:
    def __init__(self, int):
        self.int = int
        self.running = False
        if self.int % 2: 
            self.running = True
            return 0
    
    def run(self):
        print("runs the game")
    
    #proccess inputs
    def p_input(self):
        pass
        
    #updates window
    def update(self):
        pass
    
    def  render(self):
        pass
    
    #destroys window
    def destroy(self):
        print("destroys window")
    
if __name__ == "__main__":
    game = Game(2)
    game.run() 

# def main():
#     print("Hello World!")

# if __name__ == "__main__":
#     main()