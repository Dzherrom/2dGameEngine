import glm
import sdl2
import sdl2.ext 
import sdl2.sdlimage
from ECS.ECS import Entity
from Modules import logger as mod
from components.components import TransformComponent

class GameClass:
    def __init__(self):
        sdl2.ext.init()
        self.logger = mod.Logger()
        
        #set display for fullScreen
        display = sdl2.SDL_DisplayMode()
        sdl2.SDL_GetCurrentDisplayMode(0, display)
        self.window = sdl2.ext.Window("Hello world", size=(display.w, display.h))
        self.window.show()
        
        if not self.window:
            self.logger.err(message="Failed to create window") # type: ignore
            self.running = False
            return
        
        #create global render so loop doesn't breaks
        self.renderer = sdl2.SDL_CreateRenderer(self.window.window, -1, sdl2.SDL_RENDERER_PRESENTVSYNC | sdl2.SDL_RENDERER_ACCELERATED)
        
        if not self.renderer:
            self.logger.err(message="Failed to create renderer") # type: ignore
            self.running = False
            return
        self.running = True
        
        self.logger.log(message="The game constructor was called!")
        #set instance of window to full screen
        sdl2.SDL_SetWindowFullscreen(self.window.window, sdl2.SDL_WINDOW_FULLSCREEN)
        self.fps = 60
        self.ms_per_frame = 1000 / self.fps
        self.mspreviousframe = 0
                
    def run(self):
        self.setup()    
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
    
    #initialize game objects
    def setup(self):
        self.playerpos = glm.vec2(10, 20)
        self.playervel = glm.vec2(50, 5)
        
        # tank = registry.CreateEntity(tank)
        # tank.AddComponent(TransformComponent())
        # tank.AddComponent(BoxColliderComponent())
        # tank.AddComponent(SpriteComponent("./assets/images/tank.png"))
        
    
    
    #updates window
    def update(self):
        # condition to manage target time per frame 
        # sdl.delay will use way less CPU resources
        self.ms_prev_frame = sdl2.SDL_GetTicks()
        WaitTime = self.ms_per_frame - (sdl2.SDL_GetTicks() - self.ms_prev_frame)
        
        if WaitTime > 0 or WaitTime <= self.ms_per_frame:
            sdl2.SDL_Delay(int(WaitTime))
        
        # deltatime = diff in ticks since last frame conv to seconds
        self.dt = (sdl2.SDL_GetTicks() - self.ms_prev_frame)/1000

        self.playerpos.x += self.playervel.x * self.dt
        self.playerpos.y += self.playervel.y * self.dt

    def render(self):
        sdl2.SDL_SetRenderDrawColor(self.renderer, 21, 21, 21, 255)
        sdl2.SDL_RenderClear(self.renderer)
        
        #load path parameter as bytes so IMG_Load works
        surface = sdl2.sdlimage.IMG_Load(b"./assets/images/tank-tiger-right.png")
        texture = sdl2.SDL_CreateTextureFromSurface(self.renderer, surface)
        sdl2.SDL_FreeSurface(surface)

        #rectangle destination of texture
        dstRect = sdl2.SDL_Rect(int(self.playerpos.x), int(self.playerpos.y), 200, 200)
        sdl2.SDL_RenderCopy(self.renderer, texture, None, dstRect)
        sdl2.SDL_DestroyTexture(texture)
        
        sdl2.SDL_RenderPresent(self.renderer)
        
    #destroys window
    def destroy(self):
        self.logger.err(message="game destructor was called!")
        sdl2.ext.quit()


game = GameClass()
game.run()