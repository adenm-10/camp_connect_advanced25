import gymnasium as gym
from stable_baselines3 import DQN
from gymnasium.wrappers import RecordEpisodeStatistics

# Create environment with human rendering
env = gym.make("LunarLander-v3", render_mode="human")
env = RecordEpisodeStatistics(env)

# Create model
model = DQN("MlpPolicy", env, verbose=1)

# Train with visual rendering
model.learn(total_timesteps=50_000)

env.close()
