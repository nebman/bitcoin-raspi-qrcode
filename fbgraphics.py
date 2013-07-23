import pygame
import sys
import time
import os

class FbGraphics:

    black = (0, 0, 0)
    white = (255, 255, 255)

    def __init__(self):
        os.environ["SDL_FBDEV"] = "/dev/fb1"

        pygame.init()

        self.screen = pygame.display.set_mode((128,160))
        pygame.mouse.set_visible(0)

        self.screen.fill(self.black)

    def renderQR(self, topayBTC, address):
        import qrcode

        myfont1 = pygame.font.SysFont(None, 25)
        myfont2 = pygame.font.SysFont(None, 20)

        self.screen.fill(self.black)

        label = myfont1.render("BITCOIN", 0, self.white)

        topayBTC = round(topayBTC, 8)
        label2 = myfont2.render(str(topayBTC)+" BTC", 0, self.white)

        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data("bitcoin:"+address+"?amount="+str(topayBTC))
        qr.make(fit=True)
        
        image = qr.make_image()
        mode = "RGBA"
        size = image.size
        data = image.convert(mode).tostring()

        qrcode = pygame.image.fromstring(data, size, mode)
        qrcode = pygame.transform.scale(qrcode, (100,100))

        self.screen.blit(label, (10, 5))
        self.screen.blit(label2, (10, 40))
        self.screen.blit(qrcode, (14, 60))
        pygame.display.flip()
