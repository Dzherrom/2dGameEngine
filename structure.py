import sys
import sdl2.ext 
import sdl2.sdlttf

class GameClass:
    def __init__(self):
        sdl2.ext.init()
        sdl2.sdlttf.TTF_Init()
        self.window = sdl2.ext.Window("Hello world", size=(800,600))
        self.window.show()
        print("game constructor called")
        self.running = True
        
        
    def run(self):
        while self.running == True: 
            self.p_input()
            self.render()
            # self.destroy()
    
    #proccess inputs 
    def p_input(self):
        pass
    
    #updates window
    def update(self):
        pass
    
    def render(self):
        renderer = sdl2.ext.Renderer(self.window)
        renderer.clear()
        
        factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
        sprite = factory.from_text("Hello world", sdl2.ext.Color(255, 255, 255), sdl2.ttf.TTF_OpenFont("arial.ttf", 24))
        sprite.center = (400, 300)

        renderer.rendertarget(sprite)
        renderer.present()
    #destroys window
    def destroy(self):
        print("game destructor was called!")
    
game = GameClass()
game.destroy()