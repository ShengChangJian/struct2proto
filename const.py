# -*- encode:utf-8 -*-


class LineType:
    def __init__(self):
        pass

    LINE_ARRAY = 0               #content array
    LINE_VALUE = 1               #just value
    LINE_STRUCT = 2              #is a structure
    LINE_STARTOREND_STRUCT = 3   # end of a structure
    LINE_VECTOR = 4              # is a vector
    LINE_MAP = 5              # is a map
    LINE_FUNCTION = 6              # is a function
    LINE_ENUM = 7              # is a function
    LINE_MAP_MAP = 7              # is a function
    LINE_OTHER = -1


class CommonPattern:
    def __init__(self):
        pass

    type_name_pattern = r'((\w*)|(_*)|(\d*)|(\+)|( *))\*{0,1}'
    map_type_name_pattern = r'.*'
    value_name_pattern = r'\*{0,1}(\w*)|(\d*)'
    length_name_pattern = r'((\w)|(\d)|(\+)|_|( ))*'
    function_pattern = r'( *)((\w*)( *))*\(.*\)'
    enum_pattern = r'( *)enum( *)'


class StructPattern:
    def __init__(self):
        pass

    '''struct define'''
    struct_name = 'structName'
    typedef_struct_name = 'typedefStructName'
    struct_name_pattern = r'(typedef)*( *)struct( +)(?P<%s>(%s)){*' % (struct_name, CommonPattern.type_name_pattern)

class ValuePattern:
    def __init__(self):
        pass

    value_name = 'valueName'
    value_type_name = 'valueTypeName'

    '''value_type_array = 'valueTypeArray' '''
    value_type_array_length_dimen_one = 'valueTypeArrayLengthDimenOne'
    value_type_array_length_dimen_two = 'valueTypeArrayLengthDimenTwo'
    value_name_defineline_pattern = r'( *)(?P<%s>(%s))( +)(?P<%s>(%s))(\[(?P<%s>(%s))\]){0,1}(\[(?P<%s>(%s))\]){0,1}' \
                                    % (value_type_name, CommonPattern.type_name_pattern,
                                       value_name, CommonPattern.value_name_pattern,
                                       value_type_array_length_dimen_one, CommonPattern.length_name_pattern,
                                       value_type_array_length_dimen_two, CommonPattern.length_name_pattern)
    value_pattern_vector = r'( *)(vector\<(?P<%s>(%s))\>( +)(?P<%s>(%s)))' \
                           % (value_type_name, CommonPattern.map_type_name_pattern, value_name,
                              CommonPattern.value_name_pattern)
    value_pattern_set = r'( *)(set\<(?P<%s>(%s))\>( +)(?P<%s>(%s)))' \
                           % (value_type_name, CommonPattern.map_type_name_pattern, value_name,
                              CommonPattern.value_name_pattern)
    value_pattern_list = r'( *)(list\<(?P<%s>(%s))\>( +)(?P<%s>(%s)))' \
                           % (value_type_name, CommonPattern.map_type_name_pattern, value_name,
                              CommonPattern.value_name_pattern)
    value_pattern_map = r'( *)(map\<(?P<%s>(%s))\>( +)(?P<%s>(%s)))' \
                           % (value_type_name, CommonPattern.map_type_name_pattern, value_name,
                              CommonPattern.value_name_pattern)

class Constants:
    def __init__(self):
        pass

    '''restore eight length variable'''
    TOBYTES = "TOBYTES"
    COMMON_MACRO = "VRM_MAX_ID_LEN"
    eight_length_value = []
    '''four spaces'''
    PRE_BLANK = "    "


type_map = {
    "VOS_UCHAR":        "uint32",
    "VOS_UCHAR_BYTES":   "bytes",
    "VOS_UCHAR_STRING": "string",
    "VOS_CHAR":         "int32",
    "VOS_CHAR_BYTES":   "bytes",
    "VOS_CHAR_STRING":  "string",
    "VOS_UINT8":        "uint32",
    "VOS_UINT16":      "uint32",
    "VOS_UINT64":       "uint64",
    "VOS_DOUBLE":       "double",
    "VOS_UINT32":       "uint32",
    "VOS_BOOL":         "uint32",

}

vector_type_map = {
    '''struct               PROTO'''
    "VOS_UCHAR":        "string",
    "VOS_CHAR":         "string",
    "TBCDID":           "bytes",
}

