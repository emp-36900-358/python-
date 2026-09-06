import pygame

from screens.title import TitleScene
from screens.member_select import MemberSelectScene
from screens.ship_select_multi import MultiSelectShipScene
from screens.ship_select_single import SingleSelectShipScene
from screens.bullet_select_multi import MultiSelectbulletScene
from screens.bullet_select_single import SingleSelectbulletScene

pygame.init()

screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()

scene_name = "title"

title_scene = TitleScene()
member_scene = MemberSelectScene()
multi_select_ship_scene = MultiSelectShipScene()
single_select_ship_scene = SingleSelectShipScene()
multi_select_bullet_scene = MultiSelectbulletScene()
single_select_bullet_scene = SingleSelectbulletScene()

running = True

while running:

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if scene_name == "title":
        scene_name = title_scene.update(events)
        title_scene.draw(screen)

    elif scene_name == "member_select":
        scene_name = member_scene.update(events)
        member_scene.draw(screen)

    elif scene_name == "ship_select_multi":
        scene_name = multi_select_ship_scene.update(events)
        multi_select_ship_scene.draw(screen)

    elif scene_name == "ship_select_single":
        scene_name = single_select_ship_scene.update(events)
        single_select_ship_scene.draw(screen)

    elif scene_name == "bullet_select_multi":
        scene_name = multi_select_bullet_scene.update(events)
        multi_select_bullet_scene.draw(screen)

    elif scene_name == "bullet_select_single":
        scene_name = single_select_bullet_scene.update(events)
        single_select_bullet_scene.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()