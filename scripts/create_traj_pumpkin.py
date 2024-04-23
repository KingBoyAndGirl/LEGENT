from legent import Environment, ResetInfo, TaskCreator, Controller, TrajectorySaver

# env = Environment(env_path=None, use_animation=False) # significantly increase the sampling rate without using animations
env = Environment(env_path="auto", use_animation=False, camera_resolution=448) # significantly increase the sampling rate without using animations

def generate_tasks():
    from legent import generate_scene

    tasks = []
    for i in range(100):
        task = {
            "task": "Go to the Pumpkin.",
            "plan": ["Go to the Pumpkin."]
        }
        scene = generate_scene({"LowPolyInterior_Pumpkin": 1}) # Ensure that the generated scene contains a pumpkin.
        object_id = get_pumpkin_object_index(scene)
        task['solution'] = [f"goto({object_id})"]
        task['scene'] = scene

        tasks.append(task)
    return tasks


# Get the index of the Pumpkin object in the scene
def get_pumpkin_object_index(scene):
    instances = scene['instances']
    pumpkin_index = None

    for i, instance in enumerate(instances):
        if instance['prefab'] == 'LowPolyInterior_Pumpkin':
            pumpkin_index = i
            break

    if pumpkin_index is not None:
        object_id = pumpkin_index
    else:
        # Pumpkin object not found in the scene.
        raise ValueError(f'Warning: Pumpkin object not found in the scene.')

    return object_id


try:
    saver = TrajectorySaver()
    tasks = generate_tasks()
    for task in tasks:
        # 如果未找到 Pumpkin 实例，跳过该任务
        if task['solution'] is None:
            continue

        env.reset(ResetInfo(scene=task['scene']))
        controller = Controller(env, task['solution'])
        traj = controller.collect_trajectory(task)

        if traj:
            # The task has been completed successfully
            saver.save_traj(traj=traj)
            print(f'Complete task "{task["task"]}" in {traj.steps} steps.')
        else:
            print(f'Complete task "{task["task"]}" failed. Deserted.')
    saver.save()
finally:
    env.close()
