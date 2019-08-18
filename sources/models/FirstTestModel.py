params = {}

def reward_function_HelloWorld(params):

    #Read input variables
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    marker_1 = 0.1 * track_width
    marker_2 = 0.3 * track_width
    marker_3 = 0.5 * track_width


    firstMarkerScore = 1.0
    secondMarkerScore = 0.6
    thirdMarkerScore = 0.3
    progressReward = 0


    if distance_from_center <= marker_1:
        centerDistanceReward = firstMarkerScore
    elif marker_1 < distance_from_center <= marker_2:
        centerDistanceReward = secondMarkerScore
    elif marker_2 < distance_from_center <= marker_3:
        centerDistanceReward = thirdMarkerScore
    else:
        centerDistanceReward = 0

    if params["progress"] == 1:
        progressReward = 1

    if not all_wheels_on_track:
        # Penalize if the car goes off track
        reward = 1e-3
    else:
        # weight center distance to 0.6 and progress 0.4
        reward = (centerDistanceReward * 0.6) + (progressReward * 0.4)

    return reward
