# def compare_versions(version1, version2):
#     version1 =version1.replace('.', '')
#     version2 = version2.replace('.', '')
#     len_version1 = len(version1)
#     len_version2 = len(version2)
#     diff = abs(len_version1 - len_version2)
#
#     if len_version1 > len_version2:
#         version2 += diff * '0'
#     else:
#         version1 += diff * '0'
#     return True if int(version1) >= int(version2) else False


def compare_versions(version1, version2):
    version1 = version1.split('.')
    version2 = version2.split('.')
    len_version1 = len(version1)
    len_version2 = len(version2)
    largest = max(len_version1, len_version2)

    for i in range(largest):
        if i == len_version1:
            return False
        if i == len_version2:
            return True
        if int(version1[i]) != int(version2[i]):
            return True if int(version1[i]) >= int(version2[i]) else False

    return True


print(compare_versions("10.4", "10.4.8"))
