import rawpicture
import stddraw

p = rawpicture.read()
stddraw.setCanvasSize(p.width(),p.height())
stddraw.picture(p)
stddraw.show()
