from matplotlib.pyplot import *
from numpy import *

t = arange(1,3,.02)
y = 6*log(t)-7*exp(0.2*t)

figure(1)
clf()
plot(t,y)

xlabel('Time (min)')
ylabel('Temperature (C)')
title('Hanson-Plot')

savefig('ass4fig.png',dpi = 300)

show()
