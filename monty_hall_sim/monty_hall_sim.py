# This script is open source and can be used as is without giving
# any attribution whatsoever.
import numpy as np
import matplotlib.pyplot as plt


def create_game(num_doors=3):
    """Create and return number of doors with one car (represented by 1) in a
      random position and the rest with goats (represented by 0)."""

    # Initialize random number generator
    rng = np.random.default_rng(np.random.randint(123456789))
    doors = np.zeros((num_doors,), dtype=int)
    # 1 = car, 0 = goat. Initialize car behind one of the doors picked at random.
    doors[rng.integers(num_doors)] = 1
    return doors


def select_door(game):
    """Select a door from the game (player's choice at the beginning).
      Return the index of the selected door."""
    selected_door = np.random.randint(len(game))
    return selected_door


def reveal_goats(selected_door):
    """Function that returns an array representing the two doors after the game
      show host has revealed all the goats.
      The first element in the array represents the door that the player had
      picked in the beginning. The second element in the array represents the
      remaining door after rest of the doors were opened to reveal goats."""
    if selected_door == 1:
        return np.array([1, 0])
    else:
        return np.array([0, 1])


def result(doors, switch=True):
    """Function that returns the eventual choice of the player.
    If the player switches, return the second element in the array,
    else return the first."""
    if switch is True:
        return doors[1]
    else:
        return doors[0]


# Play 100 times the game of 3 doors.
accum_result_no_switch = []
accum_result_switch = []
res_no_switch = 0
res_switch = 0
for i in range(100):
    new_game = create_game(num_doors=3)
    selected_door = select_door(new_game)
    final_doors = reveal_goats(selected_door)
    res_no_switch += result(final_doors, switch=False)
    res_switch += result(final_doors, switch=True)
    accum_result_no_switch.append(res_no_switch)
    accum_result_switch.append(res_switch)

plt.plot(np.arange(len(accum_result_no_switch)),
         accum_result_no_switch, label='Accumulated Wins (No Switch)')
plt.plot(np.arange(len(accum_result_switch)),
         accum_result_switch, label='Accumulated Wins (Switch)')
plt.xlabel("Number of games played")
plt.ylabel("Wins")
plt.title("Number of Doors = 3")
plt.legend()
plt.savefig("100games3doors.png")
