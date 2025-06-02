import gymnasium as gym

# 1. Initialize the environment
env = gym.make("CartPole-v1", render_mode="human")  # Renders with GUI
obs, info = env.reset(seed=42)

print("Observation space:", env.observation_space)
print("Action space:", env.action_space)

# 2. Run a single episode with random actions
total_reward = 0
for step in range(200):
    action = env.action_space.sample()  # Random policy
    obs, reward, terminated, truncated, info = env.step(action)
    total_reward += reward

    if terminated or truncated:
        print(f"Episode ended at step {step + 1}")
        break

print("Total reward collected:", total_reward)
env.close()
