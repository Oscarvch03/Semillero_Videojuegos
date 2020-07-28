extends KinematicBody2D

const SPEED = 100
const MAX_SPEED = 1000
const GRAVITY = 500
const UP = Vector2(0, -1)
var velocity = Vector2(0, 0)

func _physics_process(delta):
	move()
	fall(delta)
	jump()
	velocity = move_and_slide(velocity, UP)


func move():
	if Input.is_action_pressed("move_left"):
		velocity.x = -SPEED
		# position.x -= SPEED * delta 
	elif Input.is_action_pressed("move_right"):
		velocity.x = SPEED
	else:
		velocity.x = 0


func fall(delta):
	if velocity.y < MAX_SPEED:
		velocity.y += GRAVITY * delta
	else: 
		velocity.y = 0
		

func jump():
	if Input.is_action_just_pressed("jump") and is_on_floor():
		velocity.y -= 3 * SPEED
		
