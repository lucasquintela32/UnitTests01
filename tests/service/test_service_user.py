import pytest

from src.service.service_user import ServiceUser


class TestServiceUser:

    @pytest.fixture
    def setup(self):
        service = ServiceUser()
        service.add_user("Geyson", "software engineer")
        yield service

    @pytest.mark.parametrize("name, job, result",
                             [
                                 ("Marcos", "manager", "success: User has been added"),
                                 ("Geyson", "software engineer", "error:This user exists in the list"),
                                 (123, "software engineer", "error: Invalid, should be String"),
                                 (None, "software engineer", "error: Invalid, cannot be None"),
                             ])
    def test_add_user(self, setup, name, job, result):
        service = setup
        expected_outcome = result
        solution = service.add_user(name, job)

        assert solution == expected_outcome

    @pytest.mark.parametrize("name, result",
                             [
                                 ("Geyson", "success: User has been removed"),
                                 ("Marcos", "error: This user does not exist in the list"),
                                 (123, "error: Invalid, should be String"),
                                 (None, "error: Invalid, cannot be None"),
                             ])
    def test_remove_user(self, setup, name, result):
        service = setup
        expected_outcome = result
        solution = service.remove_user(name)
        assert solution == expected_outcome

    @pytest.mark.parametrize("name, job, result",
                             [
                                 ("Geyson", "manager", "success: User has been updated"),
                                 ("Marcos", "manager", "error: This user does not exist in the list"),
                                 (123, "manager", "error: Invalid, should be String"),
                                 (None, "manager", "error: Invalid, cannot be None"),
                             ])
    def test_update_user(self, setup, name, job, result):
        service = setup
        expected_outcome = result
        solution = service.update_user(name, job)
        assert solution == expected_outcome

    @pytest.mark.parametrize("name, result",
                             [
                                 ("Geyson", "success:"+"\n"+"Nome: Geyson"+"\n"+"Work: software engineer"),
                                 ("Marcos", "error: This user does not exist in the list"),
                                 (123, "error: Invalid, should be String"),
                                 (None, "error: Invalid, cannot be None"),
                             ])
    def test_get_user_name(self, setup, name, result):
        service = setup
        expected_outcome = result
        solution = service.get_user_by_name(name)
        assert solution == expected_outcome
