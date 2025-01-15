This folder is for Python code rendered as video content using `manim`. 
Quoting the [`nexus` page](https://github.com/robfatland/nexus/blob/gh-pages/manim/index.md):


* Install `manim` and `LaTeX`
* Edit some code `myvideo.py`


```
import manim as m
class Scene1(m.Scene):
    def construct(self):
        c = m.Circle(2, color = m.RED, fill_opacity = 0.6)
        self.play(m.DrawBorderThenFill(c), run_time = 1.0)
        return
```


* Render it


```python -m manim myvideo.py Scene1```


* Find the results, break out the popcorn
    * My destination proved to be `/home/myusername/manim/media/videos/myvideo/1080p60/Scene1.mp4`
 
