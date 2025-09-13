import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

import torch
from LEFT.left.generalized_fol_executor import (
    NCGeneralizedFOLExecutor,
    _get_self_mask,
    _do_apply_self_mask
)
from Concepts.concepts.dsl.function_domain import FunctionDomain
from Concepts.concepts.dsl.parsers import parser_base
#from Concepts.concepts.dsl.executors.function_domain_executor import FunctionDomainExecutor 

def main():
    domain = FunctionDomain()
    executor = NCGeneralizedFOLExecutor(domain)

    x = torch.randn(4, 4)
    print("Input matrix:\n", x)
    print("Self mask:\n", _get_self_mask(x))

    print("After applying self mask:\n", _do_apply_self_mask(x))
    
    # args = [1, [2, 3], 4]
    # print("Expand args:", executor.expand_argument_values(args))

    # try:
    #     result = executor._execute("COUNT")  
    #     print("Execute result:", result)
    # except Exception as e:
    #     print("Execute failed:", e)

    # print("Execution trace:", executor._execution_trace)

if __name__ == "__main__":
    main()
