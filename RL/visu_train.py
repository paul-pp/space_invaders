import numpy as np
import matplotlib.pyplot as plt

display_train=10

data = np.load("models/stat_train4.npz")

stat_train_return = data["returns"]
stat_train_lenght = data["lengths"]



def get_moving_avgs(arr, window, convolution_mode):
    """Compute moving average to smooth noisy data."""
    return np.convolve(
        np.array(arr).flatten(),
        np.ones(window),
        mode=convolution_mode
    ) / window

# Smooth over a 500-episode window
rolling_length = display_train*2
fig, axs = plt.subplots(ncols=3, figsize=(12, 5))

# Episode rewards (win/loss performance)
axs[0].set_title("Episode rewards")
reward_moving_average = get_moving_avgs(
    stat_train_return,
    rolling_length,
    "valid"
)

# epsilon_moving_avg=get_moving_avgs(
#     Liste_epsilon,
#     rolling_length,
#     "valid"
# )

x = range(len(reward_moving_average))
axs[0].plot(x, reward_moving_average, label="Average Reward")
axs[0].set_ylabel("Average Reward")
axs[0].set_xlabel("Episode")

# # Axe Y droit : Epsilon
# ax_epsilon = axs[0].twinx()
# ax_epsilon.plot(x, epsilon_moving_avg, color="orange", label="Epsilon")
# ax_epsilon.set_ylabel("Epsilon")
# ax_epsilon.legend(loc="upper right")

# Episode lengths (how many actions per hand)
axs[1].set_title("Episode lengths")
length_moving_average = get_moving_avgs(
    stat_train_lenght,
    rolling_length,
    "valid"
)
axs[1].plot(range(len(length_moving_average)), length_moving_average)
axs[1].set_ylabel("Average Episode Length")
axs[1].set_xlabel("Episode")

# # Training error (how much we're still learning)
# axs[2].set_title("Training Loss")
# training_loss_moving_average = get_moving_avgs(
#     Training_loss,
#     rolling_length,
#     "same"
# )
# axs[2].plot(range(len(training_loss_moving_average)), training_loss_moving_average)
# axs[2].set_ylabel("Training Loss")
# axs[2].set_xlabel("Step")

plt.tight_layout()
plt.show()