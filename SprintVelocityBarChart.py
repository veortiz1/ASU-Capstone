import matplotlib.pyplot as plt
import numpy as np

# Define the data
team_velocity = [11, 11]
# one small task is one point bascially
individual_velocities = {
    'Bruce': [0, 3, 0, 0],
    'Brent': [0, 0, 0, 3],
    'Nathan': [2, 0, 1, 0],
    'Vincent': [2, 0, 0, 0]
}

# Define the sprint tasks
sprint = [
    'Task 1',
    'Task 2',
    'Task 3',
    'Task 4'
]

# Create a list of colors for each team member
colors = ['b', 'g', 'r', 'c']

# Create a bar chart
bar_width = 0.2
index = np.arange(len(sprint))

for i, (name, velocities) in enumerate(individual_velocities.items()):
    plt.bar(index + bar_width * i, velocities,bar_width, label=name, color=colors[i])

# Add labels and title
plt.xlabel('Sprints')
plt.ylabel('Velocity')
plt.title('Sprint Velocity Chart')

# Add a legend
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)

# Display the overall team velocity
team_velocity_text = f'Team Velocity: {team_velocity[0]} out of {team_velocity[1]}'
plt.text(0.05, 7, team_velocity_text, fontsize=12, fontweight='bold')

# Set the x-axis labels
plt.xticks(index + bar_width * (len(individual_velocities) / 2), sprint)
plt.yticks(np.arange(0, max(6, max(max(velocities) for velocities in individual_velocities.values())) + 1, 1))

# Add grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Customize the background color
plt.gca().set_facecolor('lightgray')

# Remove top and right spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Adjust the plot layout
plt.tight_layout()

# Add some padding to the legend
legend = plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0.)
frame = legend.get_frame()
frame.set_facecolor('white')

# Show the chart
plt.show()
