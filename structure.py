import sdl2
import sdl2.ext 
class GameClass:
    def __init__(self):
        sdl2.ext.init()
        
        #set display for fullScreen
        display = sdl2.SDL_DisplayMode()
        sdl2.SDL_GetCurrentDisplayMode(0, display)
        self.window = sdl2.ext.Window("Hello world", size=(display.w, display.h))
        self.window.show()
        
        #create global render so loop doesn't breaks
        self.renderer = sdl2.SDL_CreateRenderer(self.window.window, -1, sdl2.SDL_RENDERER_PRESENTVSYNC | sdl2.SDL_RENDERER_ACCELERATED)
        self.running = True
        
        #set instance of window to full screen
        sdl2.SDL_SetWindowFullscreen(self.window.window, sdl2.SDL_WINDOW_FULLSCREEN)
        
    def run(self):
        while self.running:
            self.events = sdl2.ext.get_events()
            for event in self.events:
                if event.type == sdl2.SDL_QUIT:
                    self.running = False
                    break
            self.p_input()    
            self.update()
            self.render()
        self.destroy()

    #proccess inputs 
    def p_input(self):
        for event in self.events:
            if event.type == sdl2.SDL_QUIT:
                self.running = False
                break

            elif event.type == sdl2.SDL_KEYDOWN:
                key = event.key.keysym.sym == sdl2.SDLK_ESCAPE
                self.running = False
                break
            
    #updates window
    def update(self):
        pass
    
    def render(self):
        sdl2.SDL_SetRenderDrawColor(self.renderer, 255, 0, 0, 255)
        sdl2.SDL_RenderClear(self.renderer)
        sdl2.SDL_RenderPresent(self.renderer)
      
    #destroys window
    def destroy(self):
        print("game destructor was called!")
        sdl2.ext.quit()
    
game = GameClass()
game.run()