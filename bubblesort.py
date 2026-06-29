from manim import *
import random

class BubbleSort(Scene):
    def construct(self):
        arr = list(range(1,11))
        random.shuffle(arr)
        bars = VGroup(*[Rectangle(height=num * 0.25, width=0.3, color=RED, fill_opacity=0.7) for num in arr])

        bars.arrange(RIGHT, buff=0.1, aligned_edge=DOWN)
        bars.to_edge(DOWN, buff=2.5)

        self.add(bars)

        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                bar_j = bars[j]
                bar_j1 = bars[j+1]

                self.play(bar_j.animate.set_color(GREEN), bar_j1.animate.set_color(GREEN), run_time=0.1)
                h_j = bar_j.get_height()
                h_j1 = bar_j1.get_height()
                p_j = bar_j.get_center()
                p_j1 = bar_j1.get_center()
                if (h_j > h_j1):
                    self.play(bar_j.animate.move_to(p_j1).align_to(bars, DOWN), bar_j1.animate.move_to(p_j).align_to(bars, DOWN), run_time=0.3)
                    bars[j], bars[j+1] = bars[j+1], bars[j]
                self.play(bar_j.animate.set_color(RED), bar_j1.animate.set_color(RED), run_time=0.1)
            self.play(bars[n-i-1].animate.set_color(BLUE), run_time=0.1)
        self.wait(2)
