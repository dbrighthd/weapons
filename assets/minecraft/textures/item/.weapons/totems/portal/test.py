import json

def count_animation_time(mcmeta_path):
    with open(mcmeta_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    animation = data.get("animation", {})
    frametime = animation.get("frametime", 1)
    frames = animation.get("frames")

    total_time = 0

    # If no explicit frames list, Minecraft assumes all frames
    # in the texture use the default frametime — but we cannot
    # infer frame count from mcmeta alone.
    if frames is None:
        raise ValueError("No 'frames' field found; total time cannot be inferred.")

    for frame in frames:
            total_time += frame.get("time", frametime)

    return total_time


files = [
        "wheatley_eye.png.mcmeta",
        "wheatley_eye_lids.png.mcmeta"
]

for path in files:
    try:
        total = count_animation_time(path)
        print(f"{path}: total time = {total}")
    except Exception as e:
        print(f"{path}: ERROR - {e}")
