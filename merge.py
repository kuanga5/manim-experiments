from manim import *
import random

class Merge(Scene):
    def construct(self):
        arr = list(range(1,21))
        random.shuffle(arr)
        arr1 = sorted(arr[:10])
        arr2 = sorted(arr[10:])

        bars1 = VGroup(*[Rectangle(height=num * 0.15, width=0.3, color=RED, fill_opacity=0.7) for num in arr1])
        bars2 = VGroup(*[Rectangle(height=num * 0.15, width=0.3, color=RED, fill_opacity=0.7) for num in arr2])

        bars1.arrange(RIGHT, buff=0.1, aligned_edge=DOWN)
        bars1.move_to([-4, -3.5, 0], aligned_edge = DOWN)

        bars2.arrange(RIGHT, buff=0.1, aligned_edge=DOWN)
        bars2.move_to([4, -3.5, 0], aligned_edge= DOWN)

        self.add(bars1)
        self.add(bars2)

        bars3 = VGroup()

        while len(bars1) > 0 and len(bars2) > 0:
            left_bar = bars1[0]
            right_bar = bars2[0]
            self.play(left_bar.animate.set_color(GREEN), right_bar.animate.set_color(GREEN), run_time=0.1)
            self.wait(0.25)
            if left_bar.get_height() < right_bar.get_height():
                bars1.remove(left_bar)
                if len(bars3) > 0:
                    self.play(bars3.animate.shift(LEFT * 0.2), run_time = 0.25)
                    self.play(left_bar.animate.next_to(bars3[-1], buff=0.1, aligned_edge=DOWN), run_time = 0.25)
                else:
                    self.play(left_bar.animate.move_to([0,0.75,0], aligned_edge=DOWN), run_time = 0.25)
                bars3.add(left_bar)
                bars1.remove(left_bar)
                self.play(left_bar.animate.set_color(BLUE), run_time = 0.1)

            else:
                if len(bars3) > 0:
                    self.play(bars3.animate.shift(LEFT * 0.2), run_time = 0.25)
                    self.play(right_bar.animate.next_to(bars3[-1], buff=0.1, aligned_edge=DOWN), run_time = 0.25)
                else:
                    self.play(right_bar.animate.move_to([0,0.75,0], aligned_edge=DOWN), run_time = 0.25)
                bars3.add(right_bar)
                bars2.remove(right_bar)
                self.play(right_bar.animate.set_color(BLUE), run_time = 0.1)
            self.wait(0.25)

        if len(bars1) > 0:
            self.play(bars1.animate.set_color(GREEN), run_time=0.1)
            self.play(bars3.animate.shift(LEFT * 0.2 * len(bars1)), run_time = 0.25)
            self.play(bars1.animate.next_to(bars3[-1], buff=0.1, aligned_edge=DOWN), run_time = 0.25)
            self.play(bars1.animate.set_color(BLUE), run_time = 0.1)
            bars3.add(bars1)
        else:
            self.play(bars2.animate.set_color(GREEN), run_time=0.1)
            self.play(bars3.animate.shift(LEFT * 0.2 * len(bars2)), run_time = 0.25)
            self.play(bars2.animate.next_to(bars3[-1], buff=0.1, aligned_edge=DOWN), run_time = 0.25)
            self.play(bars2.animate.set_color(BLUE), run_time = 0.1)
            bars3.add(bars2)
        self.play(bars3.animate.move_to(ORIGIN), run_time = 0.1)
        self.wait(0.25)