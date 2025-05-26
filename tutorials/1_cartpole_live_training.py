import gymnasium as gym
from stable_baselines3 import DQN
from gymnasium.wrappers import RecordEpisodeStatistics

# Create environment with render_mode
env = gym.make("CartPole-v1", render_mode="human")
env = RecordEpisodeStatistics(env)

# Create model
model = DQN("MlpPolicy", env, verbose=1)

# Train with rendering callback
model.learn(total_timesteps=20_000)

env.close()
