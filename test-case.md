# Test Case Documentation

## Test Environment
- **URL:** https://automationexercise.com/login
- **Browser:** Chrome (automated via webdriver-manager)
- **Test Framework:** Pytest with Selenium
- **Python Version:** 3.7+
---

## Login Tests

### Test Case 1: Valid Login
- **ID:** 1
- **Title:** Verify user can login with valid credentials
- **Preconditions:** 
  - User account exists with valid email and password
  - User is on the login page  
- **Expected Result:** Login successful
- **Actual Result:** Login successful
- **Status:** PASSED
- **Test Data:**
  - Email: `valid@email.com`
  - Password: `validpassword`

### Test Case 2: Invalid Login
- **ID:** 2
- **Title:** Verify login fails with invalid credentials
- **Preconditions:** 
  - User is on the login page
  - Invalid email/password combination is used
- **Expected Result:** Login fails with error message
- **Actual Result:** Login fails with error message
- **Status:** PASSED
- **Test Data:**
  - Email: `wrong@email.com`
  - Password: `wrongpassword`

---

## Signup Tests

### Test Case 3: Signup with Empty Fields
- **ID:** 3
- **Title:** Verify signup validation with empty fields
- **Preconditions:** 
  - User is on the signup page
  - All form fields are empty
- **Expected Result:** Form validation error appears & Signup is not processed
- **Actual Result:** Signup not processed
- **Status:** PASSED
- **Test Data:**
  - Name: (empty)
  - Email: (empty)

### Test Case 4: Signup with Invalid Email
- **ID:** 4
- **Title:** Verify signup validation with invalid email format
- **Preconditions:** 
  - User is on the signup page
  - Invalid email format is used
- **Expected Result:** Email validation error appears Signup is not processed
- **Actual Result:** ✅ PASS
- **Status:** PASSED
- **Test Data:**
  - Name: `Test User`
  - Email: `invalidemail` (invalid format, missing @)
