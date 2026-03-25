def login(username, password):
    """
    Simple login function that validates username and password.
    
    Args:
        username (str): The username to validate
        password (str): The password to validate
    
    Returns:
        dict: A dictionary containing success status and message
    """
    
    # Basic validation
    if not username or not password:
        return {
            'success': False,
            'message': 'Username and password are required'
        }
    
    # Simple authentication check (in production, use proper authentication)
    valid_users = {
        'admin': 'admin123',
        'user': 'password'
    }
    
    if username in valid_users and valid_users[username] == password:
        return {
            'success': True,
            'message': f'Login successful for {username}',
            'username': username
        }
    else:
        return {
            'success': False,
            'message': 'Invalid username or password'
        }


if __name__ == '__main__':
    # Test the login function
    print(login('admin', 'admin123'))
    print(login('user', 'password'))
    print(login('invalid', 'wrong'))
