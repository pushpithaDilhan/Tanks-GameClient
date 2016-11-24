import pygame
from pygame.locals import *
import sys
from board import Board
from socketclient import ServerClient
import SocketServer

pygame.init()

screen = pygame.display.set_mode((800, 800))

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        try:
            data = self.request.recv(1024)
            print data
        except:
            print "Exception at server"
            
sc = ServerClient(ThreadedTCPRequestHandler)

sc.start_server()

sc.connect_client("192.168.1.5", 6000)

sc.send_message("JOIN#")

board = Board()

board.set_terrain([(0,0),(0,1),(0,2),(0,3),(10,0),(11,15),(11,16),(10,12),(17,17),(18,18),(19,19),(1,1),],-1)

board.draw_board()

board.cells.draw(screen)


while 1:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    
    pygame.display.update()
