# Type of planner
import numpy as np

POINT_PLANNER=0; TRAJECTORY_PLANNER=1


class planner:
    def __init__(self, type_):

        self.type=type_

    
    def plan(self, goalPoint=[-1.0, -1.0]):
        print("INSIDE PLAN") # Debug print
        
        if self.type==POINT_PLANNER:
            return self.point_planner(goalPoint)
        
        elif self.type==TRAJECTORY_PLANNER:
            return self.trajectory_planner()


    def point_planner(self, goalPoint):
        print("INSIDE POINT PLANNER") # Debug print
        x = goalPoint[0]
        y = goalPoint[1]
        return x, y

    # TODO Part 6: Implement the trajectories here
    def trajectory_planner(self):
<<<<<<< HEAD
        PARABOLA = True
=======
        print("INSIDE TRAJECTORY PLANNER") # Debug print
        PARABOLA = False
>>>>>>> 82dda358b33b295f36f6fca7e6fa67da7c26d916
        y_vals = []
        if PARABOLA:
            x_vals = np.linspace(0, 1.5, 10)
            for x in x_vals:
<<<<<<< HEAD
                y_vals.append(x^2)
        else: # sigmoid 
=======
                y_vals.append(x**2)
        else: # sigmoid B)
>>>>>>> 82dda358b33b295f36f6fca7e6fa67da7c26d916
            x_vals = np.linspace(0, 2.5, 10)
            for x in x_vals:
                y_vals.append(2/(1 + np.exp(-2*x)) - 1)

<<<<<<< HEAD
        return_vals = zip(x_vals, y_vals)
        return return_vals
=======
        return_vals = tuple(zip(x_vals, y_vals))
        print(return_vals)
        return return_vals
>>>>>>> 82dda358b33b295f36f6fca7e6fa67da7c26d916
