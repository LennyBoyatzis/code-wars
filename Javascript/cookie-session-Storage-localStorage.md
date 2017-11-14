### Cookie vs SessionStorage vs LocalStorage
-----

- All of the above a key-value storage mechanisms on the client side
- Values can only be stored as strings

1. Cookies
- Can be created on the client or the server
- Can set an expiry time
- Is associated with a domain
- Cookies are sent via http cookie header
- 4kb capacity
- Can be used in any window

2. localStorage
- Only created in client
- Doesn't expire (must be deleted)
- Persists across sessions
- 5MB Capacity
- Any Window

3. SessionStorage
- Created by client
- Expires when tab closes
- Not persistent across browser sessions
- 5MB
