import pygame

from bin.camera import Camera
from bin.game_map import GameMap
from bin.game_over import GameOver

CELL_SIZE = 50


# класс игрового процесса
class GameProcess:
    def __init__(self, settings, registry, audio, screen, lvl):
        self.settings = settings
        self.registry = registry
        self.audio = audio
        self.is_reboot = False
        self.size = self.width, self.height = self.settings.resolution
        self.screen = screen
        self.running = True
        self.lvl = lvl
        self.clock = pygame.time.Clock()

        self.game_map = GameMap(self.registry, self.settings, self.audio, self.lvl)

        self.all_bullets_blue = self.game_map.all_bullets_blue
        self.all_characters_blue = self.game_map.all_characters_blue

        self.all_castle_blue = self.game_map.all_castle_blue
        self.all_castle_red = self.game_map.all_castle_red

        self.all_tower_blue = self.game_map.all_tower_blue
        self.all_tower_red = self.game_map.all_tower_red

        self.all_bullets_red = self.game_map.all_bullets_red
        self.all_characters_red = self.game_map.all_characters_red

        self.all_tree = self.game_map.all_tree
        self.all_indicator_red = self.game_map.all_indicator_red
        self.all_indicator_blue = self.game_map.all_indicator_blue
        self.all_bush = self.game_map.all_bush

        self.all_solid_objects = self.game_map.all_solid_objects
        self.all_not_solid_objects = self.game_map.all_not_solid_objects

        self.player = self.game_map.player

    def control_player(self, key_pressed_is):
        if key_pressed_is[pygame.K_a]:
            self.player.control['left'] = True
            self.player.control['right'] = False
        elif key_pressed_is[pygame.K_d]:
            self.player.control['left'] = False
            self.player.control['right'] = True
        else:
            self.player.control['left'] = False
            self.player.control['right'] = False

        if key_pressed_is[pygame.K_w]:
            self.player.control['up'] = True
            self.player.control['down'] = False
        elif key_pressed_is[pygame.K_s]:
            self.player.control['up'] = False
            self.player.control['down'] = True
        else:
            self.player.control['up'] = False
            self.player.control['down'] = False

        if key_pressed_is[pygame.K_SPACE]:
            self.player.control['attack'] = True
        else:
            self.player.control['attack'] = False

    # Игровой цикл
    def game(self):
        camera = Camera(self.settings)
        show_rect_player = False
        while self.running:
            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            key_pressed_is = pygame.key.get_pressed()
            mouse_pos = pygame.mouse.get_pos()

            # Обновления
            self.all_castle_blue.update()
            self.all_castle_red.update()
            self.all_tree.update()
            self.all_tower_blue.update(self.all_bullets_blue, self.all_solid_objects, self.all_characters_red)
            self.all_tower_red.update(self.all_bullets_red, self.all_solid_objects, self.all_characters_blue)
            self.all_characters_blue.update(mouse_pos, self.all_bullets_blue, camera, self.all_solid_objects)
            self.all_characters_red.update(mouse_pos, self.all_bullets_red, camera, self.all_solid_objects)
            self.all_bullets_blue.update(self.all_characters_red, self.all_castle_red,
                                         self.all_tower_red, self.all_solid_objects)
            self.all_bullets_red.update(self.all_characters_blue, self.all_castle_blue,
                                        self.all_tower_blue, self.all_solid_objects)

            if self.player:
                self.control_player(key_pressed_is)
                camera.update(self.player)
            for sprite in self.all_not_solid_objects:
                camera.apply(sprite)
            for sprite in self.all_bush:
                camera.apply(sprite)
            for sprite in self.all_tree:
                camera.apply(sprite)
            for sprite in self.all_indicator_blue:
                camera.apply(sprite)
            for sprite in self.all_indicator_red:
                camera.apply(sprite)
            for sprite in self.all_solid_objects:
                camera.apply(sprite)
            for sprite in self.all_castle_blue:
                camera.apply(sprite)
            for sprite in self.all_castle_red:
                camera.apply(sprite)
            for sprite in self.all_tower_blue:
                camera.apply(sprite)
            for sprite in self.all_tower_red:
                camera.apply(sprite)
            for sprite in self.all_characters_blue:
                camera.apply(sprite)
            for sprite in self.all_characters_red:
                camera.apply(sprite)
            for sprite in self.all_bullets_blue:
                camera.apply(sprite)
            for sprite in self.all_bullets_red:
                camera.apply(sprite)

            # Отрисовка
            self.screen.fill('black')
            self.all_not_solid_objects.draw(self.screen)
            self.all_solid_objects.draw(self.screen)
            self.all_tree.draw(self.screen)
            self.all_indicator_red.draw(self.screen)
            self.all_indicator_blue.draw(self.screen)
            self.all_bush.draw(self.screen)
            self.all_castle_blue.draw(self.screen)
            self.all_castle_red.draw(self.screen)
            self.all_tower_blue.draw(self.screen)
            self.all_tower_red.draw(self.screen)
            self.all_characters_blue.draw(self.screen)
            self.all_characters_red.draw(self.screen)
            self.all_bullets_blue.draw(self.screen)
            self.all_bullets_red.draw(self.screen)

            # Отрисовка бордюра игрока
            if show_rect_player:
                player_rect = self.player.rect
                pygame.draw.rect(self.screen, (255, 0, 0), player_rect, 2)

            # Отображение
            pygame.display.flip()
            self.clock.tick(60)

        self.running = True
        if self.player and len(self.all_castle_red) == 0:
            print('jjj')
            set_show = GameOver(self.settings, self.registry, self.audio, self.screen)
            set_show.set_display()
            # while self.running:
            #     self.screen.fill((0, 0, 0))
            #     # Обработка событий
            #     for event in pygame.event.get():
            #         if event.type == pygame.QUIT:
            #             self.running = False
            #         if event.type == pygame.KEYDOWN:
            #             if event.key == pygame.K_ESCAPE:
            #                 self.running = False

                # Отображение
                # pygame.display.flip()
                # self.clock.tick(60)
        elif not self.player or self.player.health <= 0:
            print("fnikdfnif")         
            while self.running:
                self.screen.fill((0, 0, 0))
                # Обработка событий
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.running = False

                # Отображение
                pygame.display.flip()
                self.clock.tick(60)

