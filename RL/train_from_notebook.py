from Deep_Q_learning import *
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
from env import SpaceInvadersEnv



# env = SpaceInvadersEnv(screen_width=600,screen_height=600,Display_mode=True,max_steps_per_episode=10_000)


# for episode in range(1):
#     current_observation = env.reset()
#     episode_over = False

#     while not episode_over:
#         action=env.action_space.sample()
#         new_observation, reward, terminated = env.step(action)

#         current_observation=new_observation
#         episode_over = terminated

# env.close()


n_episodes=600
start_eps=1.0
batch_size=128
update_weights_period=1000


display_train=10


env = SpaceInvadersEnv(screen_width=600,screen_height=600,Display_mode=False,max_steps_per_episode=10_000)


agent=Agent_DQN(
    env=env,

    start_learning_rate=0.002,
    start_factor_lr=1.0,
    end_factor_lr=0.2,
    total_iters_lr=int(n_episodes/2),
    
    start_epsilon=start_eps,
    epsilon_decay = start_eps / (n_episodes/2),
    final_epsilon=0.1,
    gamma=0.99
    )

buffer = ReplayBuffer(capacity=100_000)


count_update=0
Training_loss=[]
Liste_epsilon=[]


for episode in range(n_episodes):
    current_observation = env.reset()
    episode_over = False

    while not episode_over:
        action=agent.eps_greedy_action(state=current_observation)
        new_observation, reward, terminated = env.step(action)
        buffer.add(current_observation, action, reward, new_observation, int(terminated))

        current_observation=new_observation
        episode_over = terminated


        if (len(buffer)>batch_size):
            count_update+=1

            # Update method is One batch of Gradient Descent 
            loss=agent.update(*buffer.sample(batch_size))


        if (count_update>update_weights_period):
            count_update=0

            # Load the new weights on the target network each update_weights_period
            agent.network_copy.load_state_dict(agent.main_network.state_dict())

    epsilon=agent.update_epsilon()
    agent.scheduler.step()

    Training_loss.append(loss)
    Liste_epsilon.append(epsilon)

    if (episode != 0 and episode%display_train==0):
        current_lr = agent.optimizer.param_groups[0]['lr']

        print(f"\nEpisode {episode} | LR = {current_lr:.6f}")
        print(f"Episode {episode} | Reward = {np.array(env.return_queue[-display_train:]).mean():.6f}")
        print(f"Episode mean length: {np.array(env.length_queue)[-display_train:].mean()}")


agent.save_network("model_space")
stat_train_return=env.return_queue
stat_train_lenght=env.length_queue
np.savez(
    "stat_train.npz",
    returns=stat_train_return,
    lengths=stat_train_lenght
)

print("\nTraining done")
env.close()
