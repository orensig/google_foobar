import timeit
import numpy as np
from math import atan2, sqrt


def mirror_atlas(node, dimensions, distance):
    node_mirrored=[]
    for i in range(len(node)):
        points=[]
        for j in range(-(distance//dimensions[i])-1, (distance//dimensions[i]+2)):
            points.append(get_mirror(j, node[i], dimensions[i]))
        node_mirrored.append(points)
    return node_mirrored


def get_mirror(mirror, coordinates, dimensions):
    res=coordinates
    mirror_rotation=[2*coordinates, 2*(dimensions-coordinates)]
    if(mirror<0):
        for i in range(mirror, 0):
            res-=mirror_rotation[(i+1)%2]
    else:
        for i in range(mirror, 0, -1):
            res+=mirror_rotation[i%2]
    return res


def answer(dimensions, your_position, guard_position, distance):
    mirrored = [mirror_atlas(your_position, dimensions,
        distance),mirror_atlas(guard_position, dimensions, distance)]
    res=set()
    angles_dist={}
    for i in range(0, len(mirrored)):
        for j in mirrored[i][0]:
            for k in mirrored[i][1]:
                beam=atan2((your_position[1]-k), (your_position[0]-j))
                l=sqrt((your_position[0]-j)**2 + (your_position[1]-k)**2)
                if [j,k] != your_position and distance >= l:
                    if((beam in angles_dist and angles_dist[beam] > l) or beam not in angles_dist):
                        if i == 0:
                            angles_dist[beam] = l
                        else:
                            angles_dist[beam] = l
                            res.add(beam)
    return len(res)


def dist_between(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))


def angle_between(p1, p2):
    angle = np.math.atan2((p1[1] - p2[1]), (p1[0] - p2[0]))
    return angle


def get_possible_self_n_enemy_axis_positions(min_range, max_range, room_size, my_pos, enemy_pos, axis):
    possible_enemy_pos = []
    possible_self_pos = []
    for i in range(min_range, max_range):
        cell_top_pos = room_size[axis] * (i + 1)
        enemy_dist = 0
        my_dist = 0
        if i % 2 != 0:
            enemy_dist = abs(0 - enemy_pos[axis])
            my_dist = abs(0 - my_pos[axis])
        else:
            enemy_dist = abs(room_size[axis] - enemy_pos[axis])
            my_dist = abs(room_size[axis] - my_pos[axis])
        possible_enemy_pos.append(cell_top_pos - enemy_dist)
        possible_self_pos.append(cell_top_pos - my_dist)
    return [possible_self_pos, possible_enemy_pos]


def duplicate_me_and_enemy(my_position, enemy_position, room_size, max_distance):
    if dist_between(p1=my_position, p2=enemy_position) > max_distance:
        return 0
    min_width_dups = int(-np.ceil(float(max_distance)/float(room_size[0]))-1)
    max_width_dups = int(np.ceil(float(max_distance)/float(room_size[0]))+2)
    min_height_dups = int(-np.ceil(float(max_distance)/float(room_size[1]))-1)
    max_height_dups = int(np.ceil(float(max_distance)/float(room_size[1]))+2)
    possible_x_axis_locations = get_possible_self_n_enemy_axis_positions(
        min_range=min_width_dups, max_range=max_width_dups, room_size=room_size, my_pos=my_position,
        enemy_pos=enemy_position, axis=0
    )
    possible_y_axis_locations = get_possible_self_n_enemy_axis_positions(
        min_range=min_height_dups, max_range=max_height_dups, room_size=room_size, my_pos=my_position,
        enemy_pos=enemy_position, axis=1
    )
    ans = set()
    angles_and_distances = {}
    for i in range(len(possible_x_axis_locations)):
        for current_x in possible_x_axis_locations[i]:
            for current_y in possible_y_axis_locations[i]:
                current_beam_angle = angle_between(p1=my_position, p2=[current_x, current_y])
                current_beam_dist = dist_between(p1=my_position, p2=[current_x, current_y])
                if (
                        [current_x, current_y] != my_position and max_distance >= current_beam_dist and
                        ((current_beam_angle in angles_and_distances and angles_and_distances[current_beam_angle] > current_beam_dist) or
                        current_beam_angle not in angles_and_distances)
                ):
                    angles_and_distances[current_beam_angle] = current_beam_dist
                    if i != 0:
                        ans.add(current_beam_angle)
    return len(ans)


def is_valid_input(dimensions, your_position, guard_position, distance):
    if (
            any(not(isinstance(_x, list)) for _x in [dimensions, your_position, guard_position]) or
            not(isinstance(distance, int)) or not(1 < distance <= 10000) or
            not(1 < dimensions[0] <= 1250) or not(1 < dimensions[1] <= 1250) or
            not(0 < your_position[0] < dimensions[0]) or not(0 < your_position[1] < dimensions[1]) or
            not(0 < guard_position[0] < dimensions[0]) or not (0 < guard_position[1] < dimensions[1])
    ):
        return False
    return True


def solution(dimensions, your_position, guard_position, distance):
    err_msg = "One of the parameters: dimensions, your_position, guard_position, distance is malformed"
    _is_valid_input = is_valid_input(
        dimensions=dimensions, your_position=your_position, guard_position=guard_position, distance=distance
    )
    try:
        if not _is_valid_input:
            raise Exception
        return duplicate_me_and_enemy(
            my_position=your_position, enemy_position=guard_position, room_size=dimensions, max_distance=distance
        )
    except Exception as e:
        raise Exception("{}. {}".format(err_msg,e).strip(". "))


if __name__ == '__main__':
    starttime = timeit.default_timer()
    ans = solution(dimensions=[4,8], your_position=[1,1], guard_position=[3,6], distance=10000)
    print(ans)
    print("Solution runtime is :", timeit.default_timer() - starttime)
    starttime = timeit.default_timer()
    ans = answer(dimensions=[4,8], your_position=[1,1], guard_position=[3,6], distance=10000)
    print(ans)
    print("Answer runtime is :", timeit.default_timer() - starttime)



