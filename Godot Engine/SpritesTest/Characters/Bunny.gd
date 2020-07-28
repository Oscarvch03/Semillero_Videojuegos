extends KinematicBody2D

const SPEED = 100
const MAX_SPEED = 1000

onready var animation = get_node("AnimatedSprite")

var velocity = Vector2(0, 0)

func _physics_process(delta):
	move()
	animate()
	velocity = move_and_slide(velocity)


func move():
	if Input.is_action_pressed("move_left"):
		velocity.x = -SPEED
		# position.x -= SPEED * delta 
	elif Input.is_action_pressed("move_right"):
		velocity.x = SPEED
	else:
		velocity.x = 0


func animate():
	if velocity.x > 0:
		animation.set_flip_h(false)
		animation.play("walk")
		
	elif velocity.x < 0:
		animation.set_flip_h(true)
		animation.play("walk")
		
	else:
		animation.play("idle")
		
		
