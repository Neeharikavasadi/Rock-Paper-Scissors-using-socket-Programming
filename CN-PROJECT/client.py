import pygame
from network import Network
import pickle

pygame.font.init()

width = 650
height = 650
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), border_radius=15)
        font = pygame.font.SysFont("segoeuisemibold", 36)  # Modern font with better readability
        text = font.render(self.text, 1, (255, 255, 255))
        win.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2), 
                        self.y + round(self.height / 2) - round(text.get_height() / 2)))

    def click(self, pos):
        x1, y1 = pos
        return self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height

def redrawWindow(win, game, p):
    win.fill((50, 50, 150))  # Deep blue background for contrast

    if not game or not game.connected():
        font = pygame.font.SysFont("segoeuisemibold", 60)
        text = font.render("Waiting for Player...", 1, (255, 255, 0))
        win.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))
    else:
        font = pygame.font.SysFont("segoeuisemibold", 48)
        text = font.render("Your Move", 1, (0, 200, 100))
        win.blit(text, (80, 200))

        text = font.render("Opponent's Move", 1, (0, 200, 100))
        win.blit(text, (380, 200))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if game.bothWent():
            text1 = font.render(move1, 1, (0, 0, 0))
            text2 = font.render(move2, 1, (0, 0, 0))
        else:
            text1 = font.render("Locked In" if game.p1Went and p == 1 else "Waiting...", 1, (0, 0, 0))
            text2 = font.render("Locked In" if game.p2Went and p == 0 else "Waiting...", 1, (0, 0, 0))

        if p == 1:
            win.blit(text2, (100, 350))
            win.blit(text1, (400, 350))
        else:
            win.blit(text1, (100, 350))
            win.blit(text2, (400, 350))

        for btn in btns:
            btn.draw(win)

    pygame.display.update()

btns = [Button("Rock", 50, 500, (70, 70, 220)), 
        Button("Scissors", 250, 500, (220, 70, 70)), 
        Button("Paper", 450, 500, (70, 220, 70))]

def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print("You are player", player)

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
            if game is None:
                print("Game data not received. Ending session.")
                run = False
                break
        except Exception as e:
            print(f"Couldn't get game: {e}")
            run = False
            break

        if game.bothWent():
            redrawWindow(win, game, player)
            pygame.time.delay(500)
            try:
                game = n.send("reset")
                if game is None:
                    print("Failed to reset game. Ending session.")
                    run = False
                    break
            except Exception as e:
                print(f"Couldn't reset game: {e}")
                run = False
                break

            font = pygame.font.SysFont("segoeuisemibold", 72)
            result_text = "You Won!" if (game.winner() == player) else "Tie Game!" if game.winner() == -1 else "You Lost..."
            text = font.render(result_text, 1, (255, 255, 255))
            win.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and game and game.connected():
                        if player == 0 and not game.p1Went:
                            n.send(btn.text)
                        elif player == 1 and not game.p2Went:
                            n.send(btn.text)

        redrawWindow(win, game, player)

def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill((30, 30, 100))
        font = pygame.font.SysFont("segoeuisemibold", 54)
        text = font.render("Click to Play!", 1, (255, 255, 0))
        win.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()

while True:
    menu_screen()
