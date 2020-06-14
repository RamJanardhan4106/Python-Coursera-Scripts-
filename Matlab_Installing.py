import matplotlib.pyplot as plt
import pandas as pd

# set directory
df = pd.read_excel('Angle difference plot.xlsx', 'Sheet1')


# set plot
plt.plot(df['Angle'], df['RE Angle'])

# set label
plt.xlabel('calculated angle')
plt.ylabel('ground truth)')
plt.title('angle accuracy plot')
plt.legend()

plt.show()

