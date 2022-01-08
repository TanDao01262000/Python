extends KinematicBody2D

const ACCELERATION = 500
const MAX_SPEED = 400
const FRICTION = 450


var velocity = Vector2.ZERO
onready var animationPlayer = $AnimationPlayer
onready var animationTree = $AnimationTree
onready var animationState = animationTree.get("parameters/playback")
func get_direction() -> Vector2:
	return Vector2(Input.get_action_strength("Right") - Input.get_action_strength("Left"), 
							Input.get_action_strength("Down")- Input.get_action_strength("Up"))

func new_velocity_calculator(direction:Vector2, linear_velocity: Vector2) -> Vector2:
	var new_velocity = linear_velocity
	new_velocity.x = direction.x 
	new_velocity.y = direction.y
	new_velocity = new_velocity.normalized()
	return new_velocity 
	
func _physics_process(delta) :

	var direction = get_direction()
	if new_velocity_calculator(direction, velocity) != Vector2.ZERO:
		animationTree.set("parameters/Idle/blend_position", direction)
		animationTree.set("parameters/Move/blend_position", direction)
		animationState.travel("Move")
		velocity = velocity.move_toward(new_velocity_calculator(direction, velocity) * MAX_SPEED, ACCELERATION * delta )
	else: 
		animationState.travel("Idle")
		velocity = velocity.move_toward(Vector2.ZERO, FRICTION * delta)
	velocity = move_and_slide(velocity)
