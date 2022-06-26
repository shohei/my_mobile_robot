#!/usr/bin/env python
import actionlib
import rospy
import tf
from move_base_msgs.msg import  MoveBaseAction, MoveBaseGoal

def goal_pose(position, rotation):
    goal_pose = MoveBaseGoal()
    goal_pose.target_pose.header.frame_id = "map"

    goal_pose.target_pose.pose.position.x = position[0]
    goal_pose.target_pose.pose.position.y = position[1]
    goal_pose.target_pose.pose.position.z = position[2]

    q = tf.transformations.quaternion_from_euler(0, 0, rotation)
    goal_pose.target_pose.pose.orientation.x = q[0]
    goal_pose.target_pose.pose.orientation.y = q[1]
    goal_pose.target_pose.pose.orientation.z = q[2]
    goal_pose.target_pose.pose.orientation.w = q[3]
    return goal_pose

if __name__=="__main__":
    rospy.init_node("goal_pose")
    client = actionlib.SimpleActionClient("move_base",MoveBaseAction)
    client.wait_for_server()
    def shutdown():
        client.cancel_goal()
    rospy.on_shutdown(shutdown)
    position = (3.0, 3.0, 0.0)
    rotation = 0.0
    goal = goal_pose(position, rotation)
    client.send_goal(goal)

    client.wait_for_result(rospy.Duration(10))




