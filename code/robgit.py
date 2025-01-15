import manim

class Scene1(manim.Scene):
    def construct(self):
        c = manim.Circle(2, color = manim.RED, fill_opacity = 0.6)
        self.play(manim.DrawBorderThenFill(c), run_time = 1.0)
        title = manim.Text("Bumpkin", font_size = 60, slant = "ITALIC").shift(manim.UP * 0.3)
        subtitle = manim.Text("Dynamics", font_size = 40, slant = "ITALIC").shift(manim.DOWN * 0.3)
        self.play(manim.Write(title), manim.Write(subtitle))
        self.wait(1)
        a = manim.Arc(3.0, manim.TAU * (1/2), -manim.TAU * (3/4), color = manim.GREEN, stroke_width = 30)
        self.play(manim.Create(a))
        self.wait(3)
        return

class Scene2(manim.Scene):
    def construct(self):
        c = manim.Circle(1, color = manim.BLUE, fill_opacity = 0.6)
        self.play(manim.DrawBorderThenFill(c), run_time = 1.0)
        return

class Scene3(manim.Scene):
    def construct(self):
        return

