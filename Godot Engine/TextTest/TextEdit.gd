extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	var input = $TextEdit.text
	# $TextEdit.grab_focus()
	var array = input.split("\n", true, $TextEdit.get_line_count())
	for i in array:
		print(i)
		# print(i.length())
