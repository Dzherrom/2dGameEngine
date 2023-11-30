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
        while self.running: 
            self.p_input()
            self.update()
            self.render()
    
    #proccess inputs 
    def p_input(self):
        event = sdl2.SDL_Event
        poll = sdl2.SDL_PollEvent
        
        for event in poll:
            if sdl2.SDL_EventType == sdl2.SDL_QUIT:
                self.running = False
                break
            
            elif sdl2.SDL_EventType == sdl2.SDL_KEYDOWN:
                key = event.key.keysym.sym == sdl2.SDLK_ESCAPE
                self.running = False
                break
        
    #updates window
    def update(self):
        pass
    
    def render(self):
        renderer = sdl2.ext.Renderer(self.window)
        renderer.clear()
        
        factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
        sprite = factory.from_text("Hello world", sdl2.ext.Color(255, 255, 255), sdl2.ttf.TTF_OpenFont("arial.ttf", 24))
        sprite.center = (400, 300)

        # Renderer.copy is used to rendedr a texture(sprite) 
        renderer.copy(sprite)
        renderer.present()
    #destroys window
    def destroy(self):
        print("game destructor was called!")
    
game = GameClass()
game.destroy()