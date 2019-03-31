import re

GREATER_THAN = 'is greater than'
SMALLER_THAN = 'is smaller than'
EQUAL_TO = 'is equal to'


def __parse_version_number_to_int(version):
    return int(re.sub("[v ]", "", version))


def __inverse_version_relation(relation):
    if relation == GREATER_THAN:
        return SMALLER_THAN
    elif relation == SMALLER_THAN:
        return GREATER_THAN
    else:
        return relation


def version_checker(v1, v2):
    is_versions_swaped = False
    v1_to_v2_is = EQUAL_TO
    v1_versions = v1.split('.')
    v2_versions = v2.split('.')

    if len(v1_versions) < len(v2_versions):
        v1_versions, v2_versions = v2_versions, v1_versions
        is_versions_swaped = True

    for version_index in range(len(v1_versions)):
        if version_index > len(v2_versions) - 1:
            v1_to_v2_is = GREATER_THAN
            break
        else:
            v1_parsed = __parse_version_number_to_int(v1_versions[version_index])
            v2_parsed = __parse_version_number_to_int(v2_versions[version_index])

            if v1_parsed < v2_parsed:
                v1_to_v2_is = SMALLER_THAN
                break
            elif v1_parsed > v2_parsed:
                v1_to_v2_is = GREATER_THAN
                break
            elif v1_parsed == v2_parsed:
                continue

    if is_versions_swaped:
        v1_to_v2_is = __inverse_version_relation(v1_to_v2_is)

    return f'{v1} {v1_to_v2_is} {v2}'


if __name__ == "__main__":
    print(version_checker('2', '2'))
    print(version_checker('2', '1.23.4'))
    print(version_checker('1.4.0', '1.4'))
    print(version_checker('1.3.254v', '1.4'))
    print(version_checker('1.3.2', '1.3.1.0'))
