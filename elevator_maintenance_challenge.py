def split_version(_version_str):
    version_lst = _version_str.split(".")
    major = int(version_lst[0])
    minor = int(version_lst[1]) if len(version_lst) > 1 else -1
    revision = int(version_lst[2]) if len(version_lst) > 2 else -1
    return (major, minor, revision)

def create_versions_tuples_list(_versions_str_list):
    ans = [split_version(_ver_str) for _ver_str in _versions_str_list]
    return ans

def versions_sort(_versions_tuple_list):
    return sorted(_versions_tuple_list, key=lambda tup: (tup[0],tup[1], tup[2]))

def tuples_list_to_str_list(_versions_tuple_list):
    ans  = []
    for _tup in _versions_tuple_list:
        temp_str_list = []
        for _item in _tup:
            if _item != -1:
                temp_str_list.append(str(_item))
            else:
                break
        ans.append(".".join(temp_str_list))
    return ans

def solution(l):
    if (not isinstance(l,list)) or (not 1 <= len(l) <= 100):
        raise Exception("The parameter l is malformed")
    ver_tup_list = create_versions_tuples_list(_versions_str_list=l)
    sorted_ver_tup_list = versions_sort(_versions_tuple_list=ver_tup_list)
    sorted_ver_list = tuples_list_to_str_list(_versions_tuple_list=sorted_ver_tup_list)
    return sorted_ver_list
