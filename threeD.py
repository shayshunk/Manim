from manim import *
import random


class NeutronTrack(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=3*PI/8, theta=PI/6)
        axes = ThreeDAxes(x_range=(-10, 10),
                          y_range=(-10, 10), z_range=(-10, 10))
        labels = axes.get_axis_labels(
            Text(
                "x-axis").scale(0.7), Text("y-axis").scale(0.45), Text("z-axis").scale(0.45)
        )

        neutron_track = Arrow3D(start=axes.coords_to_point(
            0, 0, 0), end=axes.coords_to_point(-5.5, 0, 5.5), color=WHITE)

        dots = VGroup()
        x_locs = []
        y_locs = []
        z_locs = []

        for i in range(100):
            xrand = (-0.05 * i)
            zrand = xrand * -1
            xrand = xrand + random.uniform(-0.25, 0.25)
            yrand = random.uniform(-0.5, 0.5)
            zrand = zrand + random.uniform(-0.5, 0.5)
            rand_color = random.randint(1, 10)
            dot_color = BLUE

            if rand_color == 1:
                dot_color = YELLOW
            elif rand_color == 2:
                dot_color = YELLOW_A
            elif rand_color == 3:
                dot_color = YELLOW_B
            elif rand_color == 4:
                dot_color = YELLOW_C
            elif rand_color == 5:
                dot_color = YELLOW_D
            elif rand_color == 6:
                dot_color = BLUE_A
            elif rand_color == 7:
                dot_color = BLUE_B
            elif rand_color == 8:
                dot_color = BLUE_C
            elif rand_color == 9:
                dot_color = BLUE_D

            dot = Dot3D(point=axes.coords_to_point(xrand, yrand, zrand),
                        radius=0.025, color=dot_color, fill_opacity=0.5)
            dots.add(dot)

            x_locs.append(xrand)
            y_locs.append(yrand)
            z_locs.append(zrand)

        self.play(Create(axes), Create(labels))
        self.wait(0.5)
        # self.begin_ambient_camera_rotation(rate=0.1, about="theta")

        for i in range(100):
            self.play(Create(dots[i], run_time=0.07))

        self.wait(0.5)

        target_z = 0

        def set_z_coord(point):
            # The point is a numpy array [x, y, z]
            x, y, _ = point
            return axes.coords_to_point(x, y, target_z)

        self.play(dots.animate.apply_function(set_z_coord))

        self.wait(0.5)
        self.play(FadeIn(neutron_track))
        self.wait(2)
