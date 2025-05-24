import gymnasium as gym

# Initialise the environment
env = gym.make("LunarLander-v3", render_mode="human")

# Reset the environment to generate the first observation
observation, info = env.reset(seed=42)

episode_reward = 0
episode = 0
total_steps = 100000

for step in range(total_steps):
    # this is where you would insert your policy
    action = env.action_space.sample()

    # step (transition) through the environment with the action
    # receiving the next observation, reward and if the episode has terminated or truncated
    observation, reward, terminated, truncated, info = env.step(action)

    # print(f"Step: {step}, Reward: {reward:.2f}, Cumulative Reward: {episode_reward + reward:.2f}")
    episode_reward += reward

    # If the episode has ended then we can reset to start a new episode
    if terminated or truncated:
        print(f"Episode: {episode:4d}, Episode Reward: {episode_reward + reward:.2f}, Total Steps = {step:5d} / {total_steps}")
        episode_reward = 0
        episode += 1
        observation, info = env.reset()

env.close()