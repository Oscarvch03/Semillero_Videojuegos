extends KinematicBody2D

const SPEED = 50
var velocity = Vector2(0, 0)

func _process(delta):
	var direction_x = Input.get_action_strength("move_right") - Input.get_action_strength("move_left")
	var direction_y = Input.get_action_strength("move_down") - Input.get_action_strength("move_up")
	velocity.x = direction_x * SPEED
	velocity.y = direction_y * SPEED
	velocity.normalized()
	velocity = move_and_slide(velocity) 
