class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        xs = {}
        ys = {}

        for p in points:
            if not p[0] in xs.keys():
                xs[p[0]] = [p[1]]
            else:
                xs[p[0]].append(p[1])

            if not p[1] in ys.keys():
                ys[p[1]] = [p[0]]
            else:
                ys[p[1]].append(p[0])


        min_diffs_x = {}
        min_diffs_y = {}
        deltas_x = {}
        deltas_y = {}
        for x in xs.keys():
            xs[x] = sorted(xs[x])     
            i = 0
            while i < len(xs[x]) -1:
                if not x in deltas_x.keys():
                    deltas_x[x] = [(xs[x][i+1] - xs[x][i], [xs[x][i], xs[x][i+1]])]
                else:
                    deltas_x[x].append( (xs[x][i+1] - xs[x][i], [xs[x][i], xs[x][i+1]] ) )     
                i += 1
            if x in deltas_x.keys():
                deltas_x[x] = sorted(deltas_x[x], key=lambda item: item[0])    
            

        for y in ys.keys():
            ys[y] = sorted(ys[y])
            i = 0
            while i < len(ys[y]) -1:
                if not y in deltas_y.keys():
                    deltas_y[y] = [(ys[y][i+1] - ys[y][i], [ys[y][i], ys[y][i+1]] )]
                else:
                    deltas_y[y].append( (ys[y][i+1] - ys[y][i], [ys[y][i], ys[y][i+1]] ) )     
                i += 1
            if y in deltas_y.keys():
                deltas_y[y] = sorted(deltas_y[y], key=lambda item: item[0])

            min_ver_area = self.find_min_area(deltas_x, deltas_y)
            min_hor_area = self.find_min_area(deltas_y, deltas_x)

            if min_ver_area == min_hor_area == None:
                return 0
            else:
                if min_ver_area is None or min_ver_area > min_hor_area:
                    return min_hor_area
                else:
                    return min_ver_area
         
    # Find the smallest vertical line that forms a rectangle
    def find_min_area(self, deltas_x, deltas_y) -> int:
        min_ver_area = None
        i = 0
        for x in deltas_x.keys():
            while i < len(deltas_x[x]):
                delta_vert = deltas_x[x][i][0]
                y1 = deltas_x[x][i][1][0]
                y2 = deltas_x[x][i][1][1]

                if y1 in deltas_y.keys() and y2 in deltas_y.keys():
                    j = 0
                    k = 0
                    while j < len(deltas_y[y1]) and k < len(deltas_y[y2]):
                        if x in deltas_y[y1][j][1] and x in deltas_y[y2][k][1]:
                            
                            if deltas_y[y1][j][1][0] == deltas_y[y2][k][1][0] and \
                            deltas_y[y1][j][1][1] == deltas_y[y2][k][1][1]:
                                
                                curr_ver_area = deltas_y[y1][j][0] * deltas_x[x][i][0]
                                if min_ver_area is None or curr_ver_area < min_ver_area:
                                    min_ver_area = curr_ver_area
                                break
                            else:
                                if deltas_y[y1][j][0] > deltas_y[y2][k][0]:
                                    k += 1
                                else:
                                    j += 1
                        else:
                            k += 1
                            j += 1


                i += 1

        return min_ver_area
