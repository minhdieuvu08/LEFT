from concepts.dsl.value import Value, ListValue
from concepts.dsl.dsl_types import ValueType, ListType


def test_value():
    print("--- Test Value ---")
    dtype = ValueType("int")
    v = Value(dtype, 88)

    print("Value object:", v)
    print("repr:", repr(v))
    print("dtype:", v.dtype)
    print("value:", v.value)


def test_list_value():
    print("\n--- Test ListValue ---")
    dtype = ListType(ValueType("int"))
    lv = ListValue(dtype, [2, 2, 5])

    print("ListValue object:", lv)
    print("repr:", repr(lv))
    print("dtype:", lv.dtype)
    print("values:", lv.values)
    print("length:", len(lv))
    print("element_type:", lv.element_type)


if __name__ == "__main__":
    test_value()
    test_list_value()