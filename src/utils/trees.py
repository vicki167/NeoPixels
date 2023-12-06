from utils.ColorUtil import *
from utils.matrix import Matrix
from utils.decorations import MatrixDecoration


# todo - idea one... (spiral effect) white at top, color at bottom with spirals of black going down
#        https://youtu.be/JsLs6MVpWOM?si=f2s7l5nnD28b0mFo
# todo - idea two... alternating bands of colors with each band brighter at bottom than at top, scrolling down
#        maybe change colors as it proceeds
# todo - idea three...  shoot a "beam" up the center and then have it ricochet down.

class SpiralTree(MatrixDecoration):

    def __init__(self, matrix: Matrix, gap=3):
        super().__init__(matrix)
        self.gap = 3

    def execute(self, top_color=(255, 255, 255), bottom_color=GREEN, offset=0):
        """

        :param top_color:
        :param bottom_color:
        :param offset: this would be an incrementing value like a counter per cycle
        :return:
        """
        y_lim = self.matrix.height
        # get difference to WHITE (255, 255, 255)
        #print(top_color)
        #print(bottom_color)
        diff_r = WHITE[0] - bottom_color[0]
        diff_g = WHITE[1] - bottom_color[1]
        diff_b = WHITE[2] - bottom_color[2]
        # get delta per pixel
        del_r = diff_r/y_lim
        del_g = diff_g/y_lim
        del_b = diff_b/y_lim

        # set up the tree (essentially gradient tree)
        # todo - make a gradient tree method
        cc = WHITE
        for y in range(0, y_lim):
            self.matrix.row(cc, y)
            cc = (cc[0] - del_r, cc[1] - del_g, cc[2] - del_b)

        # starting from the top, make spiraling bands of black going down the tree
        # for each column, add segments, incrementing by one each time
        counter = 0
        while counter + self.gap < (self.matrix.height+3):
            x = counter % (self.matrix.width)
            y = counter
            counter += 1
            for n in range(self.gap):
                #print(f'Computed y: {y+offset+n}')
                #print(f'Height: {self.matrix.height-1}')
                self.matrix.setPixel(x, (y+offset+n) % (self.matrix.height), OFF)
        self.matrix.show()


class FireworkTree(MatrixDecoration):

    def __init__(self, matrix: Matrix, star=[], cols=[RED, GREEN, DBLUE], star_color=YELLOW):
        super().__init__(matrix)
        self.cols = cols
        self.i = 0
        self.star = star
        self.star_color = star_color
        self.center_col = self.matrix.width / 2
        self.matrix.fill(self.cols[self.i])
        self.next_color = self.cols[self.i+1]
        self.direction = 1
        self.star[0:] = [self.star_color] * len(self.star)
        self.matrix.show()

    def execute(self, offset=0):
        """

        :param offset: this would be an incrementing value like a counter per cycle
        :return:
        """
        if self.direction > 0:
            self.matrix.setPixel(self.center_col, self.matrix.height - (offset % self.matrix.height), self.next_color)
            if offset % self.matrix.height == 0:
                self.direction = -1
        if self.direction < 1:
            y = offset % self.matrix.height
            self.matrix.row(y, self.next_color)
            if y == self.matrix.height:
                self.direction = 1
                self.i = (self.i + 1) % len(self.cols)
                self.next_color = self.cols[self.i]
        self.matrix.show()
