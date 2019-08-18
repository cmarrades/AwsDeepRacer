#Created on Tue Jun 18 22:59:05 2019

#@author: Cesar.Marrades
#60% on kumokutaru

import math

def reward_function(params):
    
    #Read input variables
    speed = params['speed']
    all_wheels_on_track = params['all_wheels_on_track']
  
    closestWaypontsReward = calculate_closest_waypoints_reward(params)
    distanceFromCenterReward = calculate_distance_from_center_reward(params)
    progressReward = calculate_progress_reward(params)
    allWheelsOnTrackReward = calculate_all_wheels_on_track_reward(params)

    SPEED_THRESHOLD = 1.0
    speedPenalization = 1
    if speed < SPEED_THRESHOLD:
    # Penalize if the car goes too slow
        speedPenalization = 0.5    


    if not all_wheels_on_track:
        # Penalize if the car goes off track
        reward = 1e-3
    else:
        # weight center distance to 0.6 and progress 0.4
        reward = ((closestWaypontsReward * 0.15) + (distanceFromCenterReward * 0.35) + (progressReward * 0.27) + (allWheelsOnTrackReward * 0.33)) * speedPenalization
        
    return float(reward)


def calculate_all_wheels_on_track_reward(params):
    #Example of rewarding the agent to stay inside the two borders of the track
    
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    # Give a very low reward by default
    reward = 1e-3

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.05:
        reward = 1.0

    # Always return a float value
    return float(reward)
    

def calculate_progress_reward(params):
    if params["progress"] == 1:
        progressReward = 1
    else:
        progressReward  = 0
    
    return progressReward
    

def calculate_closest_waypoints_reward(params):
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    
    reward = 1.0
    #  Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
     # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    #  Convert to degree
    track_direction = math.degrees(track_direction)
     #  Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    #  Penalize the reward if the difference is too large
    DIRECTION_THRESHOLD = 10.0
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0
    return reward

def calculate_distance_from_center_reward(params):
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    
    marker_1 = 0.1 * track_width
    marker_2 = 0.3 * track_width
    marker_3 = 0.5 * track_width


    firstMarkerScore = 1.0
    secondMarkerScore = 0.6
    thirdMarkerScore = 0.3
    

    if distance_from_center <= marker_1:
        centerDistanceReward = firstMarkerScore
    elif marker_1 < distance_from_center <= marker_2:
        centerDistanceReward = secondMarkerScore
    elif marker_2 < distance_from_center <= marker_3:
        centerDistanceReward = thirdMarkerScore
    else:
        centerDistanceReward = 0        

    return centerDistanceReward
    
    

def reward_function_speed(params):
 '''
 Example of using all_wheels_on_track and speed
 '''
 # π Read input variables
 all_wheels_on_track = params['all_wheels_on_track']
 speed = params['speed']
 # Set the speed threshold based your action space
 SPEED_THRESHOLD = 1.0
 if not all_wheels_on_track:
 # Penalize if the car goes off track
     reward = 1e-3
 elif speed < SPEED_THRESHOLD:
 # Penalize if the car goes too slow
     reward = 0.5
 else:
 # High reward if the car stays on track and goes fast
    reward = 1.0
 return reward



