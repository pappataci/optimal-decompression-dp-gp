import clr
from ctypes import string_at
from System.Runtime.InteropServices \
    import *  # importing GCHandle, GCHandleType
import sys
import numpy as np
sys.path.append(r'C:\Users\glddm'
                r'\Source\Repos\pappataci\OptimalDecompression'
                r'\TrinomialModel\bin\Debug\net462')


clr.AddReference('TrinomialModel')
from TrinomialModToPython import ToPython


dotnetToPython = ToPython
modelParams = dotnetToPython.modelParams


def to_numpy(src):
    """ Converts .NET arrays to python arrays

    :param src: .NET array
    :return: python array
    """
    src_handle = GCHandle.Alloc(src, GCHandleType.Pinned)
    try:
        src_ptr = src_handle.AddrOfPinnedObject().ToInt64()
        dest = np.frombuffer(string_at(src_ptr, len(src) * 8))
    finally:
        if src_handle.IsAllocated:
            src_handle.Free()
    return dest


def node_to_tissue_tensions(a_node):
    state = to_numpy(dotnetToPython.nodeToStateVec(a_node))
    return state[0:3]


def get_model_params():
    model_params = {'Rates': to_numpy(modelParams.Rates),
                    'Gains': to_numpy(modelParams.Gains),
                    'Thresholds':to_numpy(modelParams.Thresholds)}
    return model_params


def get_tables_n_table_strategies():
    return dotnetToPython.getTablesNoExc()


def get_tables():
    return get_tables_n_table_strategies().Item1


def get_tables_strategies():
    return get_tables_n_table_strategies().Item2
