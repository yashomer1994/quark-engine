import pytest

from quark.Objects.registerobject import RegisterObject


@pytest.fixture()
def variable_obj():
    variable_obj = RegisterObject("v3", "append()", None)

    yield variable_obj

    del variable_obj


class TestVariableObject:

    def test_init(self, variable_obj):
        with pytest.raises(TypeError):
            variable_obj_with_no_argu = RegisterObject()

        assert isinstance(variable_obj, RegisterObject)
        assert variable_obj.register_name == "v3"
        assert variable_obj.value == "append()"
        assert variable_obj.called_by_func == []

    def test_called_by_func(self, variable_obj):
        variable_obj_with_called_by_func = RegisterObject(
            "v3", "append()", "toString()",
        )

        assert variable_obj_with_called_by_func.called_by_func == [
            "toString()",
        ]

        variable_obj.called_by_func = "file_list"
        variable_obj.called_by_func = "file_delete"

        assert variable_obj.called_by_func == ["file_list", "file_delete"]

    def test_get_all(self, variable_obj):
        variable_obj.called_by_func = "file_list"
        variable_obj.called_by_func = "file_delete"
        assert repr(
            variable_obj,
        ) == "<VarabileObject-register:v3, value:append(), called_by_func:file_list,file_delete>"

    def test_hash_index(self, variable_obj):
        assert variable_obj.hash_index == 3
