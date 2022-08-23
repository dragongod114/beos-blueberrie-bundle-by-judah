controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (beo.tileKindAt(TileDirection.Bottom, assets.tile`myTile`)) {
    	
    } else {
        beo.vy += -105
    }
})
function level_3 () {
    tiles.setCurrentTilemap(tilemap`level5`)
    sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
    level += 1
    beo.setPosition(5, 8)
    tiles.placeOnRandomTile(borange, assets.tile`myTile5`)
}
function start_level_2 () {
    tiles.setCurrentTilemap(tilemap`level2`)
    beo.setPosition(2, 10)
    borange = sprites.create(img`
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
        `, SpriteKind.Enemy)
    tiles.placeOnRandomTile(borange, assets.tile`myTile5`)
    level += 1
    animation.runImageAnimation(
    borange,
    [img`
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
        `,img`
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
        `],
    500,
    true
    )
}
let BERRIES = 0
let borange: Sprite = null
let beo: Sprite = null
beo = sprites.create(assets.image`beo`, SpriteKind.Player)
controller.moveSprite(beo, 100, 0)
tiles.setCurrentTilemap(tilemap`level1`)
scene.cameraFollowSprite(beo)
let level = 1
let health = 100
forever(function () {
    music.playTone(262, music.beat(BeatFraction.Half))
    music.playTone(294, music.beat(BeatFraction.Half))
    music.playTone(330, music.beat(BeatFraction.Half))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.playTone(494, music.beat(BeatFraction.Half))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.playTone(330, music.beat(BeatFraction.Half))
    music.playTone(294, music.beat(BeatFraction.Half))
})
game.onUpdateInterval(100, function () {
    if (level == 2) {
        borange.vy += 30
    }
})
game.onUpdateInterval(100, function () {
    if (beo.x >= 2130) {
        borange.follow(beo)
        animation.runImageAnimation(
        borange,
        [img`
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
            `,img`
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
            `],
        500,
        true
        )
        info.player2.setScore(health)
        if (beo.overlapsWith(borange)) {
            health += -1
        }
    }
    if (level == 2) {
    	
    }
    if (health < 1) {
        game.over(false)
        pause(5000)
        game.reset()
    }
    beo.vy += 30
    if (beo.tileKindAt(TileDirection.Center, assets.tile`myTile9`)) {
        BERRIES += 1
        info.player1.setScore(BERRIES)
        tiles.setTileAt(beo.tilemapLocation(), assets.tile`myTile10`)
    }
    if (beo.tileKindAt(TileDirection.Center, assets.tile`myTile11`)) {
        game.over(false)
        pause(5000)
        game.reset()
    }
    if (level == 1 && BERRIES >= 12) {
        start_level_2()
    }
    if (controller.right.isPressed()) {
    	
    } else {
        animation.runImageAnimation(
        beo,
        [img`
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
            `,img`
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
            `],
        200,
        true
        )
    }
    if (controller.A.isPressed()) {
        animation.runImageAnimation(
        beo,
        [img`
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
            `,img`
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
            `,img`
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
            `],
        100,
        false
        )
    }
    if (level == 2 && BERRIES == 34) {
        level_3()
    }
    if (controller.A.isPressed() && beo.tileKindAt(TileDirection.Center, assets.tile`myTile5`)) {
        tiles.setTileAt(beo.tilemapLocation(), assets.tile`myTile16`)
    }
    if (controller.A.isPressed() && beo.tileKindAt(TileDirection.Center, assets.tile`myTile16`)) {
        tiles.setTileAt(beo.tilemapLocation(), assets.tile`myTile18`)
        tiles.setTileAt(beo.tilemapLocation(), assets.tile`myTile10`)
        borange.destroy(effects.bubbles, 500)
    }
})
