import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm
from career import *
from compute_fp import compute_fixed_point

wp = workerProblem()
v_init = np.ones((wp.N, wp.N))*100
v = compute_fixed_point(bellman, wp, v_init)

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
tg, eg = np.meshgrid(wp.theta, wp.epsilon)
ax.plot_surface(tg, eg, v.T, rstride=2, cstride=2, cmap=cm.jet, alpha=0.5,
        linewidth=0.25)
ax.set_zlim(150, 200)
ax.set_xlabel('theta', fontsize=14)
ax.set_ylabel('epsilon', fontsize=14)
fig.show()
