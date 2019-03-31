def sort_line_segment(x1, x2):
    return (x1, x2) if x1 < x2 else (x2, x1)


def is_lines_segments_overlap(x1, x2, x3, x4):
    try:
        line_1 = sort_line_segment(x1, x2)
        line_2 = sort_line_segment(x3, x4)

        if line_1[0] > line_2[0]:
            line_1, line2 = line_2, line_1

        if line_1[0] <= line_2[0] <= line_1[1]:
            return True

        return False
    except TypeError:
        raise Exception('Please verify that inputs are numbers')
    except Exception as e:
        raise Exception('An unknown error occurred ', e)


if __name__ == "__main__":
    print(is_lines_segments_overlap(1, 5, 2, 6))
    print(is_lines_segments_overlap(1, 5, 6, 8))
    print(is_lines_segments_overlap(2, 6, 1, 5))
    print(is_lines_segments_overlap(6, 2, 5, 1))
    print(is_lines_segments_overlap(1, 5, 6, 2))
