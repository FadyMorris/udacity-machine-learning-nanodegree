import numpy as np
from physics_sim import PhysicsSim

class Task():
    """Task (environment) that defines the goal and provides feedback to the agent."""
    def __init__(self, init_pose=None, init_velocities=None, 
        init_angle_velocities=None, runtime=5., target_pos=None):
        """Initialize a Task object.
        Params
        ======
            init_pose: initial position of the quadcopter in (x,y,z) dimensions and the Euler angles
            init_velocities: initial velocity of the quadcopter in (x,y,z) dimensions
            init_angle_velocities: initial radians/second for each of the three Euler angles
            runtime: time limit for each episode
            target_pos: target/goal (x,y,z) position for the agent
        """
        # Simulation
        self.sim = PhysicsSim(init_pose, init_velocities, init_angle_velocities, runtime) 
        self.action_repeat = 3

        self.state_size = self.action_repeat * 6
        self.action_low = 0
        self.action_high = 900
        self.action_size = 4

	# =========== Amendments : difference vector and distance ================
        self.initial_pose = np.array([0.0, 0.0, 10.0, 0.0, 0.0, 0.0]) if init_pose is None else np.copy(init_pose)
        self.diff = target_pos - self.initial_pose[:3]  #the difference vector between initial and target positions
        self.distance_total = np.linalg.norm(self.diff) #The distance between starting position and target position
	#============================================================================= 

        # Goal
        self.target_pos = target_pos if target_pos is not None else np.array([0., 0., 10.]) 

    def get_reward(self):
        """Uses current pose of sim to return reward."""
#       reward = 1.-.3*(abs(self.sim.pose[:3] - self.target_pos)).sum()

	# =========== Amendments : calculating reward ================
        x = self.sim.pose[:3] #current drone position

        reward = np.tanh((self.distance_total - np.linalg.norm(self.target_pos - x))/(self.distance_total + 0.001))
        #reward = 100 - 100 * np.tanh( np.linalg.norm(self.target_pos - x))
        # reward =  np.tanh(1 - 0.0005*(abs(self.target_pos - x)).sum())
        # reward = - np.linalg.norm(self.target_pos - x)**2 - np.linalg.norm(x - self.initial_pose[:3])

	#============================================================================= 

        return reward

    def step(self, rotor_speeds):
        """Uses action to obtain next state, reward, done."""
        reward = 0
        pose_all = []
        for _ in range(self.action_repeat):
            done = self.sim.next_timestep(rotor_speeds) # update the sim pose and velocities
            reward += self.get_reward() 
            pose_all.append(self.sim.pose)
        next_state = np.concatenate(pose_all)
        return next_state, reward, done

    def reset(self):
        """Reset the sim to start a new episode."""
        self.sim.reset()
        state = np.concatenate([self.sim.pose] * self.action_repeat) 
        return state
