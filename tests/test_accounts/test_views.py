from tests.conftest import InitUsers


class TestUsers(InitUsers):
    def test_get_list_users(self):
        """Test user access for admin method"""
        url = '/api/accounts/users/'
        response = self.user_authorized.get(url)
        assert response.status_code == 200
