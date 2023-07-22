def on_overlap_tile(sprite, location):
    game.over(True, effects.slash)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
    """),
    on_overlap_tile)

mySprite = sprites.create(img("""
        . . f f f f f f f f f f . . . . 
            . . f 1 1 1 1 1 1 1 1 f . . . . 
            . . f 1 1 1 1 1 1 1 1 f . . . . 
            . . f 1 1 f 1 1 f 1 1 f . . . . 
            . . f 1 1 1 1 1 1 1 1 f . . . . 
            . . f 1 f f f f f f 1 f . . . . 
            . . f 1 f 2 2 2 2 f 1 f . . . . 
            . . f 1 1 f 2 2 f 1 1 f . . . . 
            . . f 1 1 f f f f 1 1 f . . . . 
            . . f 1 1 1 1 1 1 1 1 f . . . . 
            . . f 1 1 1 1 1 1 1 1 f . . . . 
            . . f f f f f f f f f f . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
tiles.set_tilemap(tilemap("""
    level_1
"""))
tiles.place_on_random_tile(mySprite, assets.tile("""
    myTile2
"""))
scene.camera_follow_sprite(mySprite)
info.start_countdown(10)
controller.move_sprite(mySprite)