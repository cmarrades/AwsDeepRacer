# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 15:40:28 2019

@author: Cesar.Marrades
"""
#Rewards
import math
def reward_function_using_closest_waypoints(params):
  '''
 Example of using waypoints and heading to make the car in the right direction
 '''
 
 #  Read input variables
 waypoints = params['waypoints']
 closest_waypoints = params['closest_waypoints']
 heading = params['heading']
 #  Initialize the reward with typical value
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
 reward *= 0.5
 return reward



def reward_function_using_distance_from_center(params):
 '''
 Example of using distance from the center
 '''
  #  Read input variable
 track_width = params['track_width']
 distance_from_center = params['distance_from_center']
  #  Penalize if the car is too far away from the center
 marker_1 = 0.1 * track_width
 marker_2 = 0.5 * track_width
 
 if distance_from_center <= marker_1:
     reward = 1.0
 elif distance_from_center <= marker_2:
     reward = 0.5
 else:
     reward = 1e-3 π likely crashed/ close to off track
 return reward
