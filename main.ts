scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile1`, function (sprite, location) {
    game.over(true, effects.slash)
})
let mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
tiles.setTilemap(tilemap`level_1`)
tiles.placeOnRandomTile(mySprite, assets.tile`myTile2`)
scene.cameraFollowSprite(mySprite)
info.startCountdown(10)
controller.moveSprite(mySprite)
