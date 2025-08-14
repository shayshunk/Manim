from manim import *
import random


class NeutronTrack(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=3*PI/8, theta=PI/6)
        axes = ThreeDAxes(x_range=(-8, 8),
                          y_range=(-8, 8), z_range=(-8, 8))
        labels = axes.get_axis_labels(
            Text(
                "x-axis").scale(0.7), Text("y-axis").scale(0.45), Text("z-axis").scale(0.45)
        )

        neutron_track = Line3D(start=axes.coords_to_point(
            0, 0, 0), end=axes.coords_to_point(-5.25, 0, 5.25), color=WHITE)

        dots = VGroup()

        for i in range(100):
            xrand = (-0.05 * i)
            zrand = xrand * -1
            xrand = xrand + random.uniform(-0.25, 0.25)
            yrand = random.uniform(-0.5, 0.5)
            zrand = zrand + random.uniform(-0.5, 0.5)

            dot = Dot3D(point=axes.coords_to_point(xrand, yrand, zrand),
                        radius=0.025, color=WHITE, fill_opacity=0.5)
            dots.add(dot)

        self.play(Create(axes), Create(labels))
        self.wait(0.5)

        readout_plane = Square(side_length=3.5, color=BLUE, fill_opacity=0.5)
        readout_plane.move_to(axes.coords_to_point(-2.6, 0, 0))
        self.play(DrawBorderThenFill(readout_plane))

        self.play(Create(dots))

        self.play(
            AnimationGroup(
                *[dot.animate.set_z(0) for dot in dots],
                lag_ratio=random.uniform(0.01, 0.025),
                rate_func=lambda t: t ** 2  # Use a quadratic rate function for the falling effect
            )
        )

        self.play(Indicate(readout_plane, scale_factor=1.1, color=WHITE))
        # self.play(FadeOut(dots))
        self.wait(1)
        # self.begin_ambient_camera_rotation(rate=0.1, about="theta")

        del dots
        dots = VGroup()

        for i in range(100):
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

            xrand = random.uniform(-5, -0.1)
            zrand = xrand * -1
            xrand = xrand + random.uniform(-0.25, 0.25)
            yrand = random.uniform(-0.5, 0.5)
            zrand = zrand + random.uniform(-0.5, 0.5)

            dot = Dot3D(point=axes.coords_to_point(xrand, yrand, zrand),
                        radius=0.025, color=dot_color, fill_opacity=0.5)
            dots.add(dot)

        self.play(Create(dots))
        self.wait(0.5)
        self.play(FadeIn(neutron_track))

        midpoint = Line3D(start=axes.coords_to_point(-2.625, -1, 2.625),
                          end=axes.coords_to_point(-2.625, 1, 2.625), color=WHITE)
        self.play(Create(midpoint))

        upper_dots = VGroup()

        for dot in dots:
            print(axes.point_to_coords(dot.get_center()))
            if dot.get_x() <= -2.5:
                upper_dots.add(dot)

        self.play(Indicate(upper_dots))

        self.wait(2)
