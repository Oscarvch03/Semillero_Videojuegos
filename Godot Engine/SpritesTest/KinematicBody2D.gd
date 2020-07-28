extends KinematicBody2D

const SPEED = 100
const MAX_SPEED = 1000

onready var animation = get_node("Sprite/AnimationPlayer")

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
		animation.play("walk_right")
	elif velocity.x < 0:
		animation.play("walk_left")
	else:
		animation.play("idle")
