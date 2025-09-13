import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from left.generalized_fol_parser import NCGeneralizedFOLPythonParser
from concepts.dsl.dsl_types import ObjectType, BOOL, INT64
from concepts.dsl.dsl_functions import Function, FunctionTyping
from concepts.dsl.function_domain import FunctionDomain
import csv

def run_test():
    domain = FunctionDomain()
    domain.define_type(ObjectType('Object'))
    domain.define_type(ObjectType('ObjectSet'))
    domain.define_type(ObjectType('Action'))

    domain.define_function(Function('equal', FunctionTyping[BOOL](INT64, INT64)))
    domain.define_function(Function('greater_than', FunctionTyping[BOOL](INT64, INT64)))
    domain.define_function(Function('less_than', FunctionTyping[BOOL](INT64, INT64)))

    parser = NCGeneralizedFOLPythonParser(
        domain,
        inplace_definition=True,
        inplace_polymorphic_function=True,
        inplace_definition_type=True
    )


    code_examples = {
        "example 1": ["exists(Object, lambda x: left(x, iota(Object, lambda y: target(y))))"],
        "example 2": ["forall(y, greater_than(y, 0))"]
    }

    with open('test_results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['prompt', 'code', 'success', 'parsing'])
        for prompt, code_list in code_examples.items():
            for code in code_list:
                try:
                    parsed = parser.parse_expression(code)
                    writer.writerow([prompt, code, True, str(parsed)])
                except Exception as e:
                    writer.writerow([prompt, code, False, str(e)])

    print("File test_results.csv đã được tạo.")

    with open('test_domain_summary.txt', 'w') as f:
        f.write(domain.format_summary())
    print("File test_domain_summary.txt đã được tạo.")

if __name__ == "__main__":
    run_test()