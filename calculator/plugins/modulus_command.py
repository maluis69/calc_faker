from plugins.modulus_command import ModulusCommand

def test_modulus_command():
    modulus_command = ModulusCommand()
    assert modulus_command.execute(10, 3) == 1
    with pytest.raises(ValueError):
        modulus_command.execute(10)  # Less than two arguments