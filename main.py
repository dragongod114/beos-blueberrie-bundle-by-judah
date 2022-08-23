def on_up_pressed():
    if beo.tile_kind_at(TileDirection.BOTTOM, assets.tile("""
        myTile
    """)):
        pass
    else:
        beo.vy += -105
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    pass
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def level_3():
    tiles.set_current_tilemap(tilemap("""
        level5
    """))
    beo.set_position(5, 8)
    tiles.place_on_random_tile(borange, assets.tile("""
        myTile5
    """))
def start_level_2():
    global borange, level
    tiles.set_current_tilemap(tilemap("""
        level2
    """))
    beo.set_position(2, 10)
    borange = sprites.create(img("""
            .......444..........
                    ....44444...........
                    ...44f444...........
                    .444444444...e......
                    d444444444..e.......
                    fff444444444e444....
                    .4444444444444444...
                    .....4444444444444..
                    ......4444444444444.
                    ....ee4444444444444.
                    ...e..444e444444445.
                    ......eee4444444455.
                    .....e4444444444455.
                    ......4444444444455.
                    ......4444444444555.
                    .......444444445554.
                    ........444444555444
                    .........4444555..44
                    ...........e..e.....
                    ..........ee.ee.....
        """),
        SpriteKind.enemy)
    tiles.place_on_random_tile(borange, assets.tile("""
        myTile5
    """))
    level += 1
    animation.run_image_animation(borange,
        [img("""
                .......444..........
                        ....44444...........
                        ...44f444...........
                        .444444444...e......
                        d444444444..e.......
                        fff444444444e444....
                        .4444444444444444...
                        .....4444444444444..
                        ......4444444444444.
                        ....ee4444444444444.
                        ...e..444e444444445.
                        ......eee4444444455.
                        .....e4444444444455.
                        ......4444444444455.
                        ......4444444444555.
                        .......444444445554.
                        ........444444555444
                        .........4444555..44
                        ...........e..e.....
                        ..........ee.ee.....
            """),
            img("""
                ....................
                        .......444..........
                        ....44444...........
                        ...44f444...........
                        .444444444...e......
                        d444444444..e.......
                        fff444444444e444....
                        .4444444444444444...
                        .....4444444444444..
                        ......4444444444444.
                        ....ee4444444444444.
                        ...e..444e444444445.
                        ......eee4444444455.
                        .....e4444444444455.
                        ......4444444444455.
                        ......4444444444555.
                        .......444444445554.
                        ........444444555444
                        .........4444555..44
                        ..........ee.ee.....
            """)],
        500,
        True)
BERRIES = 0
borange: Sprite = None
beo: Sprite = None
beo = sprites.create(assets.image("""
    beo
"""), SpriteKind.player)
controller.move_sprite(beo, 100, 0)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
scene.camera_follow_sprite(beo)
level = 1
health = 10

def on_forever():
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.play_tone(494, music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
forever(on_forever)

def on_update_interval():
    if level == 2:
        borange.vy += 30
game.on_update_interval(100, on_update_interval)

def on_update_interval2():
    global health, BERRIES
    if beo.x >= 2130:
        borange.follow(beo)
        animation.run_image_animation(borange,
            [img("""
                    .......444..........
                                ....44444...........
                                ...44f444...........
                                .444444444...e......
                                d444444444..e.......
                                fff444444444e444....
                                .4444444444444444...
                                .....4444444444444..
                                ......4444444444444.
                                ....ee4444444444444.
                                ...e..444e444444445.
                                ......eee4444444455.
                                .....e4444444444455.
                                ......4444444444455.
                                ......4444444444555.
                                .......444444445554.
                                ........444444555444
                                .........4444555..44
                                ...........ee.e.....
                                ..........ee.e......
                """),
                img("""
                    .......444..........
                                ....44444...........
                                ...44f444...........
                                .444444444...e......
                                d444444444..e.......
                                fff444444444e444....
                                .4444444444444444...
                                .....4444444444444..
                                ......4444444444444.
                                ....ee4444444444444.
                                ...e..444e444444445.
                                ......eee4444444455.
                                .....e4444444444455.
                                ......4444444444455.
                                ......4444444444555.
                                .......444444445554.
                                ........444444555444
                                .........4444555..44
                                .........e.e..e.....
                                ..........e..ee.....
                """)],
            500,
            True)
        info.player2.set_score(health)
        if beo.overlaps_with(borange):
            pause(500)
            health += -1
    if level == 2:
        pass
    if health < 1:
        game.over(False)
        pause(5000)
        game.reset()
    beo.vy += 30
    if beo.tile_kind_at(TileDirection.CENTER, assets.tile("""
        myTile9
    """)):
        BERRIES += 1
        info.player1.set_score(BERRIES)
        tiles.set_tile_at(beo.tilemap_location(), assets.tile("""
            myTile10
        """))
    if beo.tile_kind_at(TileDirection.CENTER, assets.tile("""
        myTile11
    """)):
        game.over(False)
        pause(5000)
        game.reset()
    if level == 1 and BERRIES >= 12:
        start_level_2()
    if controller.right.is_pressed():
        pass
    else:
        animation.run_image_animation(beo,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . a a a 8 8 8 8 8 . . . . 
                                . . . a a a 8 8 8 8 8 8 8 . . . 
                                . . a a a 8 8 f 8 8 f 8 8 6 . . 
                                . . a a 8 c 8 8 8 8 8 8 6 6 . . 
                                . . a 8 c 8 8 8 8 8 8 6 6 6 . . 
                                . . . 8 c 8 8 8 8 8 6 6 6 . . . 
                                . . . . c 8 8 8 8 6 6 6 c . . . 
                                . . . . c . c . . c . . c . . . 
                                . . . . . . c c . c c . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . a a a 8 8 8 8 8 . . . . 
                                . . . a a a 8 8 8 8 8 8 8 . . . 
                                . . a a a 8 8 f 8 8 f 8 8 6 . . 
                                . . a a 8 c 8 8 8 8 8 8 6 6 . . 
                                . . a 8 8 c 8 8 8 8 8 6 6 6 . . 
                                . . . 8 8 c 8 8 8 8 6 6 6 . . . 
                                . . . . 8 c 8 8 8 6 6 6 c . . . 
                                . . . . . c c . . c . c . c . . 
                                . . . . . c . . . . c . . . . .
                """)],
            200,
            True)
    if controller.A.is_pressed():
        animation.run_image_animation(beo,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . a a a 8 8 8 8 8 . . . . 
                                . . . a a a 8 8 8 8 8 8 8 . . . 
                                . . a a a 8 8 f 8 8 f 8 8 6 . . 
                                . . a a 8 c 8 8 8 8 8 8 6 6 . . 
                                . . a 8 c 8 8 8 8 8 8 6 6 6 . . 
                                . . . 8 c 8 8 8 8 8 6 6 6 . . . 
                                . . . . c 8 8 8 8 6 6 6 c . . . 
                                . . . . c . c . . c . . c . . . 
                                . . . . . . c c . c c . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . a a a 8 8 8 8 8 . . . . 
                                . . . a a a 8 8 8 8 8 8 8 . . . 
                                . . a a a 8 8 f 8 8 f 8 8 6 . . 
                                . . a a 8 c 8 8 8 8 8 8 6 6 . . 
                                . . a 8 8 8 c 8 8 8 8 6 6 6 . . 
                                . . . 8 8 8 8 c 8 8 6 6 6 . . . 
                                . . . . 8 8 8 8 c 6 6 6 c . . . 
                                . . . . . . c . . c . . c . . . 
                                . . . . . . c c . c c . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . a a a 8 8 8 8 8 . . . . 
                                . . . a a a 8 8 8 8 8 8 8 . . . 
                                . . a a a 8 8 f 8 8 f 8 8 6 . . 
                                . . a a 8 c c c c c 8 8 6 6 . . 
                                . . a 8 8 8 8 8 8 8 8 6 6 6 . . 
                                . . . 8 8 8 8 8 8 8 6 6 6 . . . 
                                . . . . 8 8 8 8 8 6 6 6 c . . . 
                                . . . . . . c . . c . . c . . . 
                                . . . . . . c c . c c . . . . .
                """)],
            100,
            False)
    if level == 2 and BERRIES == 34:
        level_3()
    if controller.A.is_pressed() and beo.tile_kind_at(TileDirection.CENTER, assets.tile("""
        myTile5
    """)):
        tiles.set_tile_at(beo.tilemap_location(), assets.tile("""
            myTile16
        """))
    if controller.A.is_pressed() and beo.tile_kind_at(TileDirection.CENTER, assets.tile("""
        myTile16
    """)):
        tiles.set_tile_at(beo.tilemap_location(), assets.tile("""
            myTile18
        """))
        tiles.set_tile_at(beo.tilemap_location(), assets.tile("""
            myTile10
        """))
        borange.destroy(effects.bubbles, 500)
game.on_update_interval(100, on_update_interval2)
