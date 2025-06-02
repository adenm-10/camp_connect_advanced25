import gymnasium as gym

from stable_baselines3 import DQN

env = gym.make("CartPole-v1", render_mode="human")

# hyperparams as according to:
#   https://github.com/DLR-RM/rl-baselines3-zoo/blob/master/hyperparams/dqn.yml
model = DQN("MlpPolicy", env, verbose=1,
            learning_rate=2.3e-3,
            batch_size=64,
            buffer_size=100000,
            learning_starts=1000,
            gamma=0.99,
            target_update_interval=10,
            train_freq=256,
            gradient_steps=128,
            exploration_fraction=0.16,
            exploration_final_eps=0.04,
            policy_kwargs=dict(net_arch=[256, 256])
            )

model.learn(total_timesteps=10000, log_interval=4)
model.save("dqn_cartpole")

del model # remove to demonstrate saving and loading

model = DQN.load("dqn_cartpole")

obs, info = env.reset()
while True:
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        obs, info = env.reset()