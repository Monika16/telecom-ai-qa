# Customer Test Cases
## TC-001 — Create Customer with Valid Data
**Priority:** High
### Preconditions
User is on the Add Customer page.
### Test Data
- First Name: John
- Last Name: Smith
- Email: john@test.com
- Address: 123 Main Street
- Phone: 4255551234
### Steps
1. Enter first name.
2. Enter last name.
3. Enter email.
4. Enter address.
5. Enter phone number.
6. Submit the form.
### Expected Result
Customer should be created successfully and a Customer ID should be displayed.

## TC-002 — Add multiple customers with different valid details.
**Priority:** High
### Preconditions
User is on the Add Customer page.
### Test Data
- First Name: John
- Last Name: Smith
- Email: john@test.com
- Address: 123 Main Street
- Phone: 4255551234
- First Name: Noel
- Last Name: Shaun
- Email: noel@test.com
- Address: 345 Main Street
- Phone: 6255771234
### Steps
1. Enter first name.
2. Enter last name.
3. Enter email.
4. Enter address.
5. Enter phone number.
6. Submit the form.

Follow the steps with both test data
### Expected Result
Customers should be created successfully and 2 different Customer ID should be displayed.
## TC-003 — Submit form with all fields blank.
**Priority:** High
### Preconditions
User is on the Add Customer page.
### Steps
1. Leave the fields blank.
2. Submit the form.
### Expected Result
Alert with message "please fill all fields" is displayed.

## TC-004 — Enter numbers in First Name.
**Priority:** High
### Preconditions
User is on the Add Customer page.
### Test Data
-  First Name: 1234.
### Steps
Enter First Name
### Expected Result
A Validation of "Numbers are not allowed" is displayed.

## TC-005 — Enter numbers in Last Name.
**Priority:** High
### Preconditions
User is on the Add Customer page.
### Test Data
- Last Name: 234.
### Steps
Enter Last Name
### Expected Result
A Validation of "Numbers are not allowed" is displayed.

## TC-006 — Enter special characters in First Name.
**Priority:** High
### Preconditions
User is on the Add Customer page.
### Test Data
- First Name: ////.
### Steps
Enter First Name
## Expected Result
A Validation of "Special characters are not allowed" is displayed.

## TC-007 — Enter special characters in Last Name.
**Priority:** High
### Preconditions
User is on the Add Customer page.
### Test Data
- Last Name: !!!!.
### Steps
Enter Last Name
## Expected Result
A Validation of "Special characters are not allowed" is displayed.

## TC-008 — Enter invalid email format.
**Priority:** High
### Preconditions
User is on the Add Customer page.
### Test Data
- Email: hhhh@gb.
### Steps
Enter Email
## Expected Result
A Validation of "Email-ID is not valid" is displayed.

## TC-009 — Enter invalid telephone format.
**Priority:** High
### Preconditions
User is on the Add Customer page.
### Test Data
- Mobile Number: hhhh.
### Steps
Enter Mobile Number
## Expected Result
A Validation of "Characters are not allowed" is displayed.

## TC-010 — Enter leading spaces in a required text field.
**Priority:** High
### Preconditions
User is on the Add Customer page.
### Test Data
- First Name: give spaces.
### Steps
Enter First Name
## Expected Result
A Validation of "First character can not have space" is displayed.

## TC-011 — Refresh the page after successful customer creation.
**Priority:** Medium
### Preconditions
User is on the Add Customer page.
### Test Data
- First Name: John
- Last Name: Smith
- Email: john@test.com
- Address: 123 Main Street
- Phone: 4255551234
### Steps
1. Enter first name.
2. Enter last name.
3. Enter email.
4. Enter address.
5. Enter phone number.
6. Submit the form.
7. Click refresh once the Customer ID is generated
## Expected Result
After refreshing the page, the Customer ID continues to be displayed and no additional customer account is created.




